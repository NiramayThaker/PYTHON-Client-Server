"""import socket

print('Inside Server\n'
      'Server socket gets created')
ss = socket.socket()

# content of tuple can't be changed
# endpoint = ("localhost", 8081)
ss.bind(("localhost", 8091))
ss.listen(5)
# only 5 request

socket, add = ss.accept()
print('Connection ACCEPTED by :- ', add)
data = socket.recv(1024)
print('Client has send -> ', data.decode())
print('Singing OFF')

ss.close()
"""

import socket

print("Starting the Socket")
ss = socket.socket()

ss.bind(("localhost", 8091))

ss.listen(5)

print("Waiting for client")
socket, add = ss.accept()
print("Connected to ", add)

data = ""
while data != "q":
    data = socket.recv(1024).decode()
    print("Client sent -> ", data)

ss.close()
