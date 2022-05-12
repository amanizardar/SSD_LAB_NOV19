import socket
import _thread

import sys

n=len(sys.argv)
if(n != 2):
    print("Please Enter Valid cmd")
    exit


def on_new_client(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        msg.decode('ascii')
        print("Client Sent :",msg.decode())
        if(msg=="exit"):
            clientsocket.close()
            break

        clientsocket.send('Ack to the client'.encode())
        msg="Server Send HTTP Response".encode()
        clientsocket.send(msg)
              
s = socket.socket()  

port=int(sys.argv[1])
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', port)) 
s.listen(5)

while True:

  c, addr = s.accept()    
  print ('Got connection from', addr )
  _thread.start_new_thread(on_new_client,(c,addr))
  print("Serving This Client...")
 
 
