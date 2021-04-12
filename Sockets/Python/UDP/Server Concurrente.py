from multiprocessing import Process
import time
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def recibirDatos():
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("received message: %s" % data)

def pruebaPrint():
	while True:
		print('Leyendo datos')
		time.sleep(1)
		

t1 = Process(target=recibirDatos, args=())
t2 = Process(target=pruebaPrint, args=())

t1.start()
t2.start()
