import socket

MAX_CONNECTIONS = 2
address_to_server = ('localhost', 8686)

clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
for client in clients:
    client.connect(address_to_server)

for i in range(MAX_CONNECTIONS):
    clients[i].send(bytes("hello from client number " + str(i), encoding='UTF-8'))

while 1:
    for client in clients:
        data = client.recv(1024)
        print(str(data))