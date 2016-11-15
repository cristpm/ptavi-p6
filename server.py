#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

class ServerHandler(socketserver.DatagramRequestHandler):
    """
    Server SIP
    """

    def handle(self):
        # Leyendo 
        line = self.rfile.read()
        data = line.decode('utf-8')
        METODO = data.split(' ')[0]
        print("El cliente nos manda:")
        print(data)
        METODOS = ['INVITE','BYE','ACK']
        if METODO in METODOS:
            if METODO == 'INVITE':
                self.wfile.write(b"SIP/2.0 100 Trying\r\n\r\n")
                self.wfile.write(b"SIP/2.0 180 Ring\r\n\r\n")
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        else:
            self.wfile.write(b"SIP/2.0 405 Method Not Allowed\r\n\r\n") 
            
            


if __name__ == "__main__":
    try:
        IP = sys.argv[1]
        PORT = int(sys.argv[2])
        serv = socketserver.UDPServer((IP, PORT), ServerHandler)
        print("Listening...")
        serv.serve_forever()
    
    except IndexError:
        sys.exit("Usage: python server.py IP port audio_file")
