import socket
import threading

print("Starting the ConcurrentServer")


class Conversation(threading.Thread):
    def __init__(self, nis):
        threading.Thread.__init__(self)
        self.nis = nis

    def run(self):
        data = ""
        while data != "q":
            data = self.nis.recv(1024).decode()
            print("Client sent -> ", data)
            self.nis.send(data.encode(encoding='utf_8', errors='strict'))
        self.nis.close()


soc = socket.socket()

soc.bind(("localhost", 8091))

soc.listen(5)

while True:
    print("Waiting for client")
    client, add = soc.accept()
    print("Connected to ", add)
    Conversation(client).start()

soc.close()
print("ConcurrentServer Shutting Down")
