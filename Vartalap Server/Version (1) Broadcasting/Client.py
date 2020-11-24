
import socket
from threading import Thread

print("Welcome to Concurrent Client")
soc = socket.socket()
host = "localhost"
soc.connect((host, 8090))
print("Connection Established")


def Receive():
    global soc
    message = soc.recv(1024)
    message = message.decode()
    while message != "q":
        print("Server Echoing {}".format(message))
        message = soc.recv(1024)
        message = message.decode()
    soc.close()


message = ""
receiver = Thread(target=Receive)
receiver.start()
while message != "q":
    message = input()
    soc.send(message.encode())
receiver.join()
soc.close()
print("Client Shutting Down")
