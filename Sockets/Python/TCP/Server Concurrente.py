from multiprocessing import Process
import time

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
#sock.listen(1)

def recibirDatos():
	
	while True:
		# Wait for a connection
		print('waiting for a connection')
		connection, client_address
		try:
			print('connection from', client_address)

			# Receive the data in small chunks and retransmit it
			while True:
				data = connection.recvfrom(20)
				print('received {!r}'.format(data))
				if data:
					print('sending data back to the client')
					connection.sendall(data)
				else:
					print('no data from', client_address)
					break

		finally:
			# Clean up the connection
			connection.close()

def pruebaPrint():
	while True:
		print('Leyendo datos')
		time.sleep(1)
		

t1 = Process(target=recibirDatos, args=())
t2 = Process(target=pruebaPrint, args=())

t1.start()
t2.start()
