from socket import *
import os
from _thread import *
import threading


server= socket(AF_INET , SOCK_STREAM) #  ipv4 and tcp connection

host ="127.0.0.1"
port= 2004
Threadcount = 0

server.bind((host , port))
server.listen(5)

print("Server is listening now")

clients = []
aliases = []
def broadcast(message): 
    for client in clients: 
        client.send(message)

# Function to handle clients'connections
def handle_client(client):
    while True:
        try:
           message = client.recv(1024)
           broadcast(message)
        except:
           index = clients.index(client)
           clients.remove(client)
           client.close()
           alias = aliases[index]
           broadcast(f'{alias} has left the chat room!'.encode('utf-8')) 
           aliases.remove(alias)
           break

# Main function to receive the clients connection
def receive():
    while True:
        print("Server is running and listening ...")
        client, address = server.accept()
        print(f"connection is established with {str(address)}" )  # address of client
        client.send('alias?'.encode('utf-8')) # put name for every client
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'The alias of this client is {alias}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,)) 
        thread.start()
if __name__ == "__main__": receive()

'''
def multithread_client(connection):
    connection.send(str.encode(" server is working "))

    while True :
        data = connection.recv(2048)
        response = " server message : " + data.decode("utf=8")

        if not data :
            break
        connection.sendall(str.encode(response))
    connection.close()

    while True :

        client , address = s.accept()
        print ("connection to : " + address[0] + ':' + str(address[1]))
        start_new_thread(multithread_client , (client, ))
        Threadcount +=1
        print('Thread number : ' + str(Threadcount))
        '''

server.close()

