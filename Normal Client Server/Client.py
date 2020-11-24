"""import socket

print('Inside Client')
conn = socket.socket()
conn.connect(("localhost", 8091))
print('Connection Established')

data = input('Please send the message to server - > ')
conn.send(data.encode(encoding='utf_8', errors='strict'))
print('Out of Client')
"""


import socket

conn = socket.socket()
conn.connect(("localhost", 8091))

data = ""
while data != "q":
    data = input("Enter a Message - > ")
    conn.send(data.encode(encoding='utf_8', errors='strict'))
