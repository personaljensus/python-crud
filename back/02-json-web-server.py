#!/usr/bin/python3

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

hostName = "localhost"
hostPort = 8000

class MyServer(BaseHTTPRequestHandler):
	# Ceci est un dictionnaire Python, c'est pas encore du JSON
	data = {
		"personnages": [
			{
				"nom": "Rincevent",
				"rôle": "Mage"
			},
			{
				"nom": "Mémé Ciredutemps",
				"rôle": "Sorcière"
			}
		]
	}

	# Contient les headers standards pour répondre du JSON
	def _set_headers(self):
		self.send_header('Access-Control-Allow-Origin', '*')
		self.send_header('Content-Type', 'application/json')
		self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
		self.send_header('Access-Control-Allow-Headers', 'X-Requested-With')
		self.send_header('Access-Control-Allow-Headers', 'Content-Type')
		self.end_headers()

	# Nécessaire pour le POST.
	def do_OPTIONS(self):
		self.send_response(200)
		self._set_headers()

	#	GET
	def do_GET(self):
		self.send_response(200)
		self._set_headers()
		# json.dumps converti le dictionnaire python en JSON
		self.wfile.write(bytes(json.dumps(self.data), "utf-8"))

	#	POST is for submitting data.
	def do_POST(self):
		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) # <--- Gets the data itself

		print("Le serveur a reçu un POST!", self.path, post_data)

		# on lit le JSON et on ajoute l'objet au tableau des personnages (data)
		# notez qu'une fois le serveur tué, les modifications dans data seront perdues!
		new_characters = json.loads(post_data.decode('utf8'))
		self.data["personnages"].append(new_characters)

		self.send_response(201)
		self._set_headers()
		self.wfile.write(bytes(json.dumps(self.data), "utf-8"))


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
