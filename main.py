#code_cote_serveur
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import sqlite3

""" 





"""

clients  = {}
addresses = {}
private={}
names=[]
HOST = '127.0.0.1'
PORT = 5545
BUFFSIZE = 1024
ADDR = (HOST,PORT)
SERVER = socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADDR)

"""

"""
def privee(client,name):
    client.send(f"donner le nom de destinateur".encode('utf-8'))
    nom = client.recv(BUFFSIZE).decode("utf8")
    msg=" "
    while msg!=bytes("'\end'", "utf8"):
        msg = client.recv(BUFFSIZE)
        client.send(bytes("privee:"+name+": ",'utf8')+msg)
        private[nom].send(bytes("privee:"+name+": ",'utf8')+msg)
        

def connected() :
    onlin=""
    for row in names:
        onlin+=f"{row}\n"
   
    return onlin

def history(name):
    base=sqlite3.connect("test server.DB")
    pointeur=base.cursor()
    print("base de donne connecte")
    pointeur.execute('SELECT * FROM server')
    hist=""
    for row in pointeur:
        msg,use=row
        hist+=f"{msg} {use}\n"
    base.commit()
    base.close()
    return hist
def acceptIncomingConnections():
    while True:
        client, clientAddress = SERVER.accept()
        print("%s:%s has connected." % clientAddress)
        client.send(bytes("Welcome , entrer le nom", "utf8"))
        addresses[client] = clientAddress
        Thread(target=handleClient, args=(client,)).start()


"""

"""
def handleClient(client):
    name = client.recv(BUFFSIZE).decode("utf8")
    client.send(bytes("bonjour %s, ecrire\n'\history':historique\n'\online': les utilisateurs connectes\n'\private' : privee" % name,'utf8'))
    msg = '%s connected' % name
    broadcast(bytes(msg, 'utf8'))
    clients[client] = name
    private[name]=client
    names.append(name)
    
    while True:
        msg = client.recv(BUFFSIZE)
        if msg == bytes("'exit'", "utf8"):
            client.send(bytes("'exit'", "utf8"))
            client.close()
            del clients[client]
            del private[name]
            names.remove(name)

            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break
        elif msg== bytes("'\history'","utf8"):
            historique=history(name)
            client.send(f"{historique}".encode('utf-8'))
        elif msg== bytes("'\online'","utf8"):
             onlin=connected()
             client.send(f"{onlin}".encode('utf-8'))
        elif msg== bytes("'\private'","utf8"):
            privee(client,name)
        else:
            broadcast(msg, name+": ")
            msg=msg.decode('utf8')
            base=sqlite3.connect("test server.DB")
            pointeur=base.cursor()
            pack=(msg,name)
            request=pointeur.execute(' INSERT INTO server VALUES (?,?)',pack)
            base.commit()
            base.close()

           

"""

"""

def broadcast(msg,prefix = ""):
    for client in clients:
        client.send(bytes(prefix,'utf8')+msg)


if __name__ == "__main__":
    SERVER.listen(5)  # Listens for 5 connections at max.
    print("Waiting for a new connection...")
    ACCEPT_THREAD = Thread(target=acceptIncomingConnections)
    ACCEPT_THREAD.start()  # Starts the infinite loop.
    ACCEPT_THREAD.join()
    SERVER.close()
