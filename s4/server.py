import socket, threading

server = socket.socket()
server.bind(('127.0.0.1', 5000))
server.listen()

clients = []
nicknames = []

def broadcast_message(message):
    for client in clients:
        client.send(message)

def handle_message(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast_message(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast_message(f'{nickname} left the chat'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def start():
    while True:
        client, address = server.accept()

        client.send("NICK_CODE".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')

        nicknames.append(nickname)
        clients.append(client)

        broadcast_message(f"{nickname} joined the chat".encode('utf-8'))

        thread = threading.Thread(target= handle_message, args = (client,))
        thread.start()

if __name__ == "__main__":
    print("started")
    start()


