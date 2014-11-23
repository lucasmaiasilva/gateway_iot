from lightblue import *

s = socket(L2CAP)
s.connect(("0c:84:dc:e5:af:04",0x1001))
while 1:
  text= raw_input()
  if text == "quit":
    s.send(text)
    break
  s.send(text)
s.close()
