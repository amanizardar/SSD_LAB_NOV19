#!/usr/bin/python
import socket #Import socket module
s = socket.socket() #Create a socket object
host = socket.gethostname() #create a local machine name
port = 12345 #Reserve a port for your service
s.bind((host, port)) #Bind to the port
s.listen(15) # Now wait for client connection.
while True:
    c, addr = s.accept() #Establish connection with client
    print('Got connection from', addr)
    c.send('Thank you for connecting')
    c.close()   #Close the connection