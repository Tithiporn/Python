import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
client.connect(('localhost',13245))
data = str(raw_input("input data:"))
client.send(data)
recv = client.recv(1024)
if recv:
	print(time.asctime(time.localtime()))
	print(recv)

client.close()

