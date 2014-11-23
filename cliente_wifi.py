# Echo client program
import socket
import select


HOST = '192.168.0.30'    # The remote host
PORT = 50007      # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while 1:
  r,w,e = select.select([s],[],[],0)
  for meia in r:
    if meia==s:
      data=meia.recv(1024)
      print data
  text=raw_input()
  if text == "quit":
    s.send(text)
    break
  s.send(text)
s.close()
