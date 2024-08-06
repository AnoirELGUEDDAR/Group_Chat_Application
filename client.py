import socket
import threading
import random
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.bind(("localhost",random.randint(8000,9000)))
name=input("Nickname : ")
def receive():
    while True :
        try :
            message, _ =client.recvfrom(1024) #_ is used to ignore something we don't need ,here we don't care about the address'
            print(message.decode())
        except :
            pass
t=threading.Thread(target=receive)
t.start()
client.sendto(f"WELCOME :{name}".encode(),("localhost",9999)) #because for every client,the first message is welcome message
while True :
    message = input(" ")
    if message =="!q" :
        exit()
    else :
        client.sendto(f"{name}: {message}".encode(),("localhost",9999))

