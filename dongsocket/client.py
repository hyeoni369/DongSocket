import socket

from dongsocket.dongsocket import DongSocket


class Client(DongSocket):
    def __init__(self, server_ip: str):
        super(Client, self).__init__(server_ip)
        self.socket.connect((self.server_ip, DongSocket.PORT))

    def disconnect(self):
        self.send(DongSocket.DISCONNECT_MESSAGE)

    def __del__(self):
        self.disconnect()
