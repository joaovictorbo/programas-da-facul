# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import socket
import codecs
import cript

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print ("Successful connection. ")

while True:
    
    print("Enter a message: ")
    msg = input()
    msg = cript.cript(msg)
    msg_as_bytes = str.encode(msg)
    s.sendall(msg_as_bytes)
    print('Sent: ', msg)    
    
    data = s.recv(1024)
    codecs.decode(data)
    
    print('Received: ', cript.uncript(data))

