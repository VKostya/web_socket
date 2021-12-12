import socket

s = socket.socket()
s.bind(("127.0.0.1", 5000))
s.listen(5)
c, addr = s.accept()

while True:
    rcvd_data = c.recv(1024).decode()
    sendData = "hi client"
    c.send(sendData.encode())
    if(rcvd_data == "disc"):
        break
c.close()

