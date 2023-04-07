from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter


"""

"""
def receive():
    stop = False
    while True and not stop:
        try:
            msg = clientSocket.recv(BUFFSIZE).decode('utf8')
            msgList.insert(tkinter.END,msg+'\n')
        except OSError:
            cleanAndClose()
            break

"""

"""
def send(event=None):
    msg = myMsg.get()
    myMsg.set("")
    clientSocket.send(bytes(msg,'utf8'))
    if msg is "'exit'":
        clientSocket.close()
        cleanAndClose()
        top.quit()

"""

"""
def cleanAndClose(event=None):
    myMsg.set("'exit'")
    send()
    top.destroy()
    stop = True

if __name__ == '__main__':
    top = tkinter.Tk()
    top.title('hdidou and tahiri')
    messageFrame = tkinter.Frame(top)
    scrollbar = tkinter.Scrollbar(messageFrame)

    msgList = tkinter.Text(messageFrame, width = 50, yscrollcommand = scrollbar.set)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    msgList.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
    msgList.pack(fill = tkinter.X)
    messageFrame.pack()

    myMsg = tkinter.StringVar()
    myMsg.set("Click to type")
    entryField = tkinter.Entry(top,textvariable = myMsg)
    entryField.bind("<Return>", send)
    entryField.pack()
    sendButton = tkinter.Button(top, text = 'Send', command = send, height = 1, width = 7)
    sendButton.pack()

    top.protocol("WM_DELETE_WINDOW", cleanAndClose)

    HOST = input('IP Address: ')
    PORT = input('Entrer PORT : ')
    PORT = 5545 if not PORT else int(PORT)

    BUFFSIZE = 1024
    ADDR = (HOST, PORT)
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(ADDR)

    receiveThread = Thread(target=receive)
    receiveThread.start()
    tkinter.mainloop()  
    receiveThread.join()