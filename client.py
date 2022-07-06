from dongsocket import Client

SERVER = '112.214.29.95'

client = Client(server_ip=SERVER)

client.send('Hello World!')
input()
client.send('Hello Everyone!')
input()
client.send('Hello Tim!')

client.disconnect()
