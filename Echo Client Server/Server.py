import socket

print("Starting the EchoServer")
ss = socket.socket()
ss.bind(("localhost", 8091))
ss.listen(5)

while True:

    print("Waiting for client")
    socket, add = ss.accept()
    print("Connected to ", add)

    data = ""
    while data != "q":
        data = socket.recv(1024).decode()
        print("Client sent -> ", data)
        # sending data back /\
        #                   ||
        socket.send(data.encode(encoding='utf_8', errors='strict'))

    socket.close()

ss.close()
