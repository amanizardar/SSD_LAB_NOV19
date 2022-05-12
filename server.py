import socket
import _thread

import sys

n=len(sys.argv)
if(n != 2):
    print("Please Enter Valid cmd")
    exit


def Serving_client(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        msg=msg.decode('ascii')
        print("Client said",msg)
        if(msg=='tata'):
            clientsocket.close()
            break

        clientsocket.send('Hello Client im Server and i got ur msg'.encode())
        msg=msg[::-1]
        clientsocket.send(msg.encode())
              
s = socket.socket()  

port=int(sys.argv[1])
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', port)) 
s.listen(5)

while True:

  c, addr = s.accept()    
  print ('Got connection from', addr )
  _thread.start_new_thread(Serving_client,(c,addr))
  print("New Thread Active for this Client.")
 
 
