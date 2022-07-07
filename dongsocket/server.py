import socket
from threading import Thread

from dongsocket.dongsocket import DongSocket


class Server(DongSocket):
    def __init__(self, server_ip: str):
        super(Server, self).__init__(server_ip)
        self.socket.bind((self.server_ip, DongSocket.PORT))

    def start(self):
        self.socket.listen()
        print(f'[LISTENING] Server is listening on {self.server_ip}')
        while True:
            conn, addr = self.socket.accept()
            thread = Thread(target=self.handle_client, args=(conn, addr), daemon=True)
            thread.start()

    def handle_client(self, conn: socket, addr: str):
        print(f'[NEW CONNECTION] {addr} connected.')

        while True:
            # get message
            msg = self.receive(connection=conn)
            if msg == DongSocket.DISCONNECT_MESSAGE:
                break

            print(f'[{addr}] {msg}')

        conn.close()
