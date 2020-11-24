import socket
import threading

print("Welcome to Concurrent Server 1.0")

clist = []


class Conversation(threading.Thread):
    def __init__(self, soc):
        threading.Thread.__init__(self)
        self.soc = soc

    def run(self):
        global clist
        clist.append(self.soc)
        msg = self.soc.recv(1024)
        msg = msg.decode()
        while msg != "q":
            [soc.send(msg.encode()) for soc in clist]
            print(msg)
            msg = self.soc.recv(1024)
            msg = msg.decode()
        print("Client Disconnected")
        clist.remove(self.soc)
        self.soc.send("q".encode())
        self.soc.close()


ss = socket.socket()
hname = "localhost"
print("host name", hname)
port = 8090
ss.bind((hname, port))
ss.listen(5)
while True:
    c, addr = ss.accept()
    print("Connection Established with ", addr)
    Conversation(c).start()
ss.close()
print("Server Shutting Down")
