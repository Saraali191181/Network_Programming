from socket import *
import os
from _thread import *
import threading

alias = input("Choose an alias >>> ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host="127.0.0.1"
port = 2004

print (" waiting for the connection response ")

client.connect((host,port))

def client_receive():
    while True:
        try:
           message = client.recv(1024).decode('utf-8')
           if message == "alias?":
            client.send(alias.encode('utf-8'))
           else:
            print(message)
        except:
           print('Error!')
           client.close()
           break

def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))
        receive_thread =threading.Thread(target=client_receive)
        receive_thread.start()
        send_thread = threading.Thread(target=client_send)
        send_thread.start()

'''
recv_data = s.recv(1024)

while True :
    input_data = input ("client : ")
    s.send(str.encode(input_data))
    recv_data = s.recv(1024)

    print(recv_data.decode("utf=8"))

    
    '''
client.close()

