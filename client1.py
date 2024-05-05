import socket
import asyncio
import random 


class Client():
    def __init__(self, ip="localhost", port=3000) -> None:
        self.ip = ip
        self.port = port
        self.HOST = (self.ip, self.port)

    def connect(self):
        host = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        host.connect(self.HOST)
        return host

    async def write_host_socket(self, host: socket.socket):
        ascii_values = [ord(char) for char in "PINK"]
        host.send(bytes(ascii_values))
    
    async def read_host_socket(self, host: socket.socket):
        return host.recv(4)
    

async def main():
    client = Client()
    socket = client.connect()
    while 1:
        await asyncio.sleep(random.uniform(0.3, 3))
        await client.write_host_socket(socket)
        data = await client.read_host_socket(socket)
        print(data)

asyncio.run(main())
