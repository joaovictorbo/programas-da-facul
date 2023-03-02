import socket
import codecs
import cript

HOST = '127.0.0.1'  # localhost
PORT = 65432        # Port to listen on 

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((HOST, PORT))
ss.listen()
print("Listem ip:" + HOST + " port: " + str(PORT))

s, addr = ss.accept()

info = socket.getnameinfo(addr, socket.NI_NUMERICSERV)

print("Connected by ", info)

while True:
   
    data = s.recv(1024)
    codecs.decode(data)
    
    print('Received: ', cript.uncript(data))
   
    print("Enter a message: ")
    msg = input()
    msg = cript.cript(msg)
    msg_as_bytes = str.encode(msg)
    s.sendall(msg_as_bytes)
    print('Sent: ', msg)
