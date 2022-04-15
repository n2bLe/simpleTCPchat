import socket
import threading


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',5555))
server.listen()
print('Waiting for connection...')


clients = []

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handle_clients(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        
        except:
            clients.remove(client)
            client.close()
            break


def receive():
    while True:
        
        client,addr = server.accept()
        print(f'connected with {addr}')
        clients.append(client)
        client.send('Connected to the server'.encode('utf-8'))
        
        threading.Thread(target=handle_clients,args=(client,)).start()

receive()