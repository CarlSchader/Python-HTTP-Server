from email.utils import formatdate
import os

status_codes = {200: "OK", 400: "Bad Request", 404: "Not Found"}

content_types = {".html": "text/html", ".jpg": "image/jpeg"}

class HTTPrequest:
	def __init__(self, string):
		lines = string.split("\r\n")
		firstline = lines[0].split(' ')
		self.method = firstline[0]
		self.path = firstline[1]
		self.version = firstline[2]
		self.fields = {}
		for line in lines[1:]:
			if ':' in line:
				self.fields[line[:line.index(':')]] = line[line.index(':') + 2:]

def http_response(content_path, status_code):
	content = open(content_path, "rb").read()
	content_type = content_types.get(os.path.splitext(content_path)[1], "text/html")
	header = "HTTP/1.1 {} {}\r\nDate: {}\r\nServer: Carl Schader Python Server\r\nContent-Length: {}\r\nContent-Type: {}\r\nConnection: Closed\r\n\r\n".format(status_code, status_codes[status_code], formatdate(timeval=None, localtime=False, usegmt=True), len(content), content_type)
	print(header)
	header = header.encode("utf-8")
	return header + content



