import socket
from tkinter import *
from threading import Thread

print("Welcome to Concurrent GUI Client")
soc = socket.socket()
host = "localhost"
soc.connect((host, 8091))
print("Connection Established")


def Receive():
    global soc
    global root
    message = soc.recv(1024)
    message = message.decode()
    taData.set("{} \n {}".format(taData.get(), message))
    while message != "q":
        message = soc.recv(1024)
        message = message.decode()
        taData.set("{} \n {}".format(taData.get(), message))
    soc.close()
    root.quit()


receiver = Thread(target=Receive)
receiver.start()

root = Tk()

root.geometry("400x400")

root.title("Chat Client")

taData = StringVar()
taData.set("")


def sendMessage(event):
    global tf
    message = tf.get()
    soc.send(message.encode())
    tf.delete(0, END)


p1 = Frame(root)

tf = Entry(p1)
ta = Label(root, textvariable=taData)

send = Button(p1, text="Send")
send.bind("<Button>", sendMessage)

tf.pack(side="left")
ta.pack()
send.pack(side="left")
p1.pack()

root.mainloop()
