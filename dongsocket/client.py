import socket

from dongsocket.dongsocket import DongSocket


class Client(DongSocket):
    def __init__(self, server_ip: str):
        super(Client, self).__init__(server_ip)
        self.socket.connect((self.server_ip, DongSocket.PORT))

    def disconnect(self):
        self.send(DongSocket.DISCONNECT_MESSAGE)

    def send(self, data: any):
        encoded_data = data.encode(DongSocket.FORMAT)
        encoded_data_length = len(encoded_data)
        encoded_encoded_data_length = str(encoded_data_length).encode(DongSocket.FORMAT)
        data_length_header = encoded_encoded_data_length.ljust(DongSocket.HEADER, b' ')
        self.client.send(data_length_header)
        self.client.send(encoded_data)

    def __del__(self):
        self.disconnect()
