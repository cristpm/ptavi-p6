#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

class ServerHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        # Leyendo 
        line = self.rfile.read()
        data = line.decode('utf-8')
        data.split(' ')
        print("El cliente nos manda:")
        print(data)


if __name__ == "__main__":
    # Creamos servidor de eco y escucham
    try:
        IP = sys.argv[1]
        PORT = int(sys.argv[2])
        serv = socketserver.UDPServer((IP, PORT), ServerHandler)
        print("Listening...")
        serv.serve_forever()
    
    except IndexError:
        sys.exit("Usage: python server.py IP port audio_file")
