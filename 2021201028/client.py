# Import socket module
import socket  
import sys

n=len(sys.argv)
if(n != 2):
    print("Please Enter Valid cmd")
    exit

s = socket.socket()      
port = int(sys.argv[1])             
s.connect(('127.0.0.1', port))

while(1):
    msg=input("Type the msg to send to the server : ")
    if(msg=="exit"):
        s.send(msg.encode())
        break
    s.send(msg.encode())
    print (s.recv(17).decode())
    print (s.recv(25).decode())

s.close()