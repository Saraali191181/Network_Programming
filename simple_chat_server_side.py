from socket import *

s = socket(AF_INET , SOCK_STREAM )
host = "127.0.0.1"
port= 7002

s.bind((host,port))
s.listen(5)

print (" server is listenning now ")

client , address = s.accept()

print("connection from : " , address[0])

while True :
    received_data=client.recv(2048)

    if received_data.decode("utf=8") == "Q" :
        break

    print("client : " , received_data.decode("utf=8"))

    send_data = input("server : ")  # to receive input from user 

    client.send(send_data.encode("utf=8"))

    if send_data == "Q" :
        break
    
    
s.close() # close the sockect
