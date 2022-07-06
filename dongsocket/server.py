import socket
from threading import Thread

from dongsocket.dongsocket import DongSocket


class Server(DongSocket):
    def __init__(self, server_ip: str):
        super(Server, self).__init__(server_ip)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.server_ip, DongSocket.PORT))

    def start(self):
        self.server.listen()
        print(f'[LISTENING] Server is listening on {self.server_ip}')
        while True:
            conn, addr = self.server.accept()
            thread = Thread(target=self.handle_client, args=(conn, addr), daemon=True)
            thread.start()

    @staticmethod
    def handle_client(conn: socket, addr: str):
        print(f"[NEW CONNECTION] {addr} connected.")

        while True:
            # get message length
            msg_length_str: str = conn.recv(DongSocket.HEADER).decode(DongSocket.FORMAT)
            msg_length: int = int(msg_length_str) if msg_length_str else 0

            # get message
            msg = conn.recv(msg_length).decode(DongSocket.FORMAT)
            if msg == DongSocket.DISCONNECT_MESSAGE:
                break

            print(f'[{addr}] {msg}')

        conn.close()
