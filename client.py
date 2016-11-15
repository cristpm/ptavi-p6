#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
# Cliente UDP simple.


METODO = sys.argv[1]
RECEPTOR = sys.argv[2].split('@')
# Login, Dirección IP, Puerto del servidor.
LOGIN = RECEPTOR[0]
IP = RECEPTOR[1].split(':')[0]
PORT = int(RECEPTOR[1].split(':')[-1])



# Contenido que vamos a enviar
LINEA = ' sip:' + LOGIN + '@' + IP + ' SIP/2.0\r\n'
MENSAJE = METODO + LINEA
print(MENSAJE)
# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IP, PORT))
    

my_socket.send(bytes(MENSAJE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
