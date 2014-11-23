import bluetooth
import select
import socket

host = '192.168.0.30'
port_ip=50007


hostMACAddress = '0C:84:DC:E5:AF:04'
port = 0x1001
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.L2CAP)
s.bind((hostMACAddress, port))
s.listen(backlog)

so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.bind((host,port_ip))
so.listen(backlog)


try:
  client,clientInfo = s.accept()
  conn,addr = so.accept()

  while 1:

    rlist,wlist,elist=select.select([client,conn],[],[],25)

    if [rlist,wlist,elist] == [[],[],[]]:
      print "25 segundos sem troca de mensagens"
    else:
      for sock in rlist:
        message = sock.recv(size)
        print message
        try:
          conn.send(message)
        except:
          pass


except:
  client.close()
  conn.close()
  s.close()
  so.close()
  print "saindo!"
