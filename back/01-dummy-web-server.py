#!/usr/bin/python3

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = ""
hostPort = 8000

class MyServer(BaseHTTPRequestHandler):

	def _set_headers(self):
		self.send_header('Access-Control-Allow-Origin', '*')
		self.send_header('Content-Type', 'text/plain')
		self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
		self.send_header('Access-Control-Allow-Headers', 'X-Requested-With')
		self.send_header('Access-Control-Allow-Headers', 'Content-Type')
		self.end_headers()

	#	GET is for clients geting the predi
	def do_GET(self):
		self.send_response(200)
		self._set_headers()
		self.wfile.write(bytes("You accessed path: %s" % self.path, "utf-8"))

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
