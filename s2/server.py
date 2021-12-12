import socket
 
server = socket.socket()
server.bind(('127.0.0.1', 5000))
server.listen(4)
while True:
    client_socket, address = server.accept()
    data = client_socket.recv(1024).decode('utf-8').split(' ')
    print(data)
    try:
        answer = "Площадь равна " + str(int(data[0])*int(data[1]))
        print(answer)
        client_socket.send(answer.encode('utf-8'))
    except Exception:
        client_socket.send('error'.encode('utf-8'))
    client_socket.shutdown(socket.SHUT_WR)