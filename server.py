from dongsocket import Server

SERVER = '112.214.29.95'

server = Server(server_ip=SERVER)
server.start()
print('[STARTED] Server started...')
