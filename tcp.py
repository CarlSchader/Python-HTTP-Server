import sys
from socket import *
from multiprocessing import Process

def tcp_listen_socket(port, backlog):
	listen_socket = socket(AF_INET, SOCK_STREAM)
	listen_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	listen_socket.bind(('', port))
	listen_socket.listen(backlog)
	return listen_socket

def tcp_server_loop(port, backlog, thread_function):
	listen_socket = tcp_listen_socket(port, backlog)
	while True:
		connection_socket, address = listen_socket.accept()
		thread = Process(target=thread_function, args=(connection_socket, address))
		thread.start()
	listen_socket.close()
