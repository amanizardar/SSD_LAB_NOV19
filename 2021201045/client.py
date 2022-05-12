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
    msg=input("Send the msg to send to the server : ")
    if(msg=="tata"):
        s.send(msg.encode())
        break
    s.send(msg.encode())
    print (s.recv(39).decode())
    print (s.recv(1024).decode())

s.close()