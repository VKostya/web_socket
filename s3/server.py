import socket

def start_server():
    server = socket.socket()
    server.bind(('127.0.0.1', 5000))
    server.listen(4)
    while True:
        client_socket, address = server.accept()
        data = client_socket.recv(1024).decode('utf-8')
        if not data.split(' ')[1] == '/favicon.ico':
            content = load_page(data)
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)


def load_page(request):
    HTTP_HEADER = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HTTP_HEADER404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    path = request.split(' ')[1]
    response = ''
    try:
        with open('6 lab/s3/templates' + path + '.html', 'rb') as file: 
            response = file.read()
        return HTTP_HEADER.encode('utf-8') + response
    except FileNotFoundError:
        return (HTTP_HEADER404 + 'No such page').encode('utf-8')



if __name__ == '__main__':
    start_server()