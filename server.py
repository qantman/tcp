import socket
import asyncio
import random 
import select


class Server():
    def __init__(self, ip="localhost", port=3000) -> None:
        self.ip = ip
        self.port = port
        self.HOST = (self.ip, self.port)
        self.ascii_values = [ord(char) for char in "PONK"]
        self.MAX_CONNECTIONS = 2
        self.INPUTS = list()
        self.OUTPUTS = list()

    def start_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.setblocking(0)
        self.socket.bind(self.HOST)
        self.socket.listen(self.MAX_CONNECTIONS)
        print("Server has been started")
        return self.socket


    async def read(self, rs:list):
        self.data = []
        for socket in rs:
            if socket == self.socket:
                connection, client_address = socket.accept()
                connection.setblocking(0)
                self.INPUTS.append(connection)
            else:
                if socket not in self.OUTPUTS:
                    self.OUTPUTS.append(socket)
                if random.randint(0, 9) == 0:
                    self.data.append("Игног")
                self.data.append(socket.recv(4))
        return self.data

    async def write(self, ws:list, data:str):
        for socket in ws:
            socket.send(bytes(data))

async def main():
    server_socket = Server()
    socket = server_socket.start_socket()
    server_socket.INPUTS.append(socket)
    while 1:
        rs, ws, es = select.select(
            server_socket.INPUTS,
            server_socket.OUTPUTS,
            server_socket.INPUTS
        )
        data = await server_socket.read(rs)
        if data == 0:
            socket.close()
        print(data)
        if data == "Игног":
            continue
        await asyncio.sleep(random.uniform(0.1, 1))
        await server_socket.write(ws, server_socket.ascii_values)


asyncio.run(main())