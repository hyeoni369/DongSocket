import json
import socket


class DongSocket:
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = '!DISCONNECT'

    def __init__(self, server_ip: str):
        self.server_ip: str = server_ip
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, data: any, connection: socket = None):
        conn = connection if connection is not None else self.socket

        serialized_data = json.dumps(data)
        encoded_data = serialized_data.encode(DongSocket.FORMAT)
        encoded_data_length = len(encoded_data)
        encoded_encoded_data_length = str(encoded_data_length).encode(DongSocket.FORMAT)
        data_length_header = encoded_encoded_data_length.ljust(DongSocket.HEADER, b' ')
        conn.send(data_length_header)
        conn.send(encoded_data)

    def receive(self, connection: socket = None) -> any:
        conn = connection if connection is not None else self.socket

        # get message length
        msg_length_str: str = conn.recv(DongSocket.HEADER).decode(DongSocket.FORMAT)
        msg_length: int = int(msg_length_str) if msg_length_str else 0

        # get message
        msg = conn.recv(msg_length).decode(DongSocket.FORMAT)

        return json.loads(msg)
