import socket, threading

nickname = input('Enter your nickname')

client = socket.socket()
client.connect(('127.0.0.1', 5000))

def recieve_stream():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "NICK_CODE":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            client.close()
            break

def write_message():
    while True:
        message = f"{nickname} - {input()}"
        client.send(message.encode('utf-8'))

recieve_thread = threading.Thread(target = recieve_stream)
recieve_thread.start()

write_thread = threading.Thread(target = write_message)
write_thread.start()
