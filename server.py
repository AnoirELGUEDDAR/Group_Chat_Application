import socket
import threading
import queue
messages=queue.Queue() #Queue to store messages received from clients
clients=[]
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('localhost',9999)) #bind=link the server to the specified IP and port
def receive(): #receive messages from clients and put them into the queue
    while True:
        try :
            message,address=server.recvfrom(1024)  #Receives a message of up to 1024 bytes and the address it came from.(ordered tuple,python detect msg data and address auto)
            messages.put((message,address)) #put the reiceived message and address as a tuple to "the queue"
        except :
            pass

def broadcast(): #take the messages from queue and broadcast them to all clients
    while True:
        while not messages.empty(): #check if there are any messages in the queue
            message,addr=messages.get() #get the message and address from the queue
            print(message.decode()) #Decodes and prints the message to the server console.
            if addr not in clients :
                clients.append(addr)
            for client in clients:
                try:
                    if message.decode().startswith("WELCOME :"):  #If the client is new,check client.py to figure it out
                        name =message.decode()[message.decode().index(":")+1:] #to detect the name,(open Readme to understand)
                        server.sendto(f"{name} joined!".encode(),client)#we use decoding to find the name,and now we have to encode it(from string(human-readable to bytes(machine-readable)
                    else :
                        server.sendto(message,client)
                except:
                    clients.remove(client)
t1=threading.Thread(target=receive)
t2=threading.Thread(target=broadcast)    #Threading allows you to have different parts of your process run at the same time
t1.start()
t2.start()




