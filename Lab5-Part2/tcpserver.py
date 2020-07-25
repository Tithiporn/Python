import socket
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('localhost',13245))
server.listen(5)

while True:
	print('Waiting for connection . . . ')
	client, address = server.accept()
	print('... connected from:', address)                
	data = client.recv(1024)
	if data:

	client.send(data.upper())
	client.close()

server.close()
