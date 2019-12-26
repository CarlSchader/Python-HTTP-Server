import sys
import os
import re
from tcp import *
from http import *

BUFFER_SIZE = 8192
SERVER_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR_NAME = "PawPrint"
PROJECT_DIR = SERVER_DIR[:SERVER_DIR.find(PROJECT_DIR_NAME) + len(PROJECT_DIR_NAME)] + '/'
VALID_PATH_REGEX = "^(html/.*)|(resources/.*)$"

def process_http_request(request):
	if request.path == '/':
		return http_response(PROJECT_DIR + "html/index.html", 200)
	elif re.search(VALID_PATH_REGEX, request.path):
		return http_response(PROJECT_DIR + request.path, 200)
	else:
		return http_response(PROJECT_DIR + "html/whoops.html", 404)

def connection_thread(socket, address):
	request = HTTPrequest(socket.recv(BUFFER_SIZE).decode("utf-8"))
	socket.sendto(process_http_request(request), address)
	socket.close()

def main(port, backlog):
	tcp_server_loop(port, backlog, connection_thread)

if __name__ == "__main__":
	main(int(sys.argv[1]), int(sys.argv[2]))