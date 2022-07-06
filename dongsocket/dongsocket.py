import socket


class DongSocket:
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = '!DISCONNECT'

    def __init__(self, server_ip: str):
        self.server_ip: str = server_ip
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
