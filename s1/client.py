import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 5000))


while str:
   str = input('enter ')
   s.send(str.encode())
   if(str == "disc"):
      break
   print(s.recv(1024).decode())
s.close()