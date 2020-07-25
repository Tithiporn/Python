import socket
server= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(('localhost',8000))

while True:               
	data, address = server.recvfrom(1024)
	if data:
		server.sendto(data.upper(),address)
server.close()
