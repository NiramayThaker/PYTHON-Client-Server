import socket

conn = socket.socket()
conn.connect(("localhost", 8091))

data = ""
while data != "q":
    data = input("Enter a Message> ")
    conn.send(data.encode(encoding='utf_8', errors='strict'))
    print("Server Echoing -> ", conn.recv(1024).decode())
    # getting data back          /\
    #                            ||
