import socket
from threading import Thread

print("Welcome to Echo Client")
soc = socket.socket()
host = "localhost"
soc.connect((host, 8091))
print("Connection Established")


def Receive():
    global soc
    message = ""
    while message != "q":
        message = soc.recv(1024)
        message = message.decode()
        print("Server Echoing {}".format(message))


message = ""
receiver = Thread(target=Receive)
receiver.start()
while message != "q":
    message = input()
    soc.send(message.encode())
receiver.join()
soc.close()
print("Client Shutting Down")
