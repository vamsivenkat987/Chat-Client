import select
import socket
import sys
import time
import re


class socket_server:
    def __init__(self, host, port,):
        self.host = host
        self.port = port
        
        s = []
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            print('socket created')
        except socket.error:      
            print('Socked not created')
            sys.exit()
            
        
        s.bind((self.host,self.port))
        s.listen(10)
        
        
        new_clients=[]
        new_clients.append(s)
    def client_connection(connection,address):
        while True:
            try:
                nick_name = connection.recv(2048).decode('utf-8')
                nick_name1 = nick_name.strip("NICK")
                regex = re.compile('[@!#$%^&*()?/|}{~:]')
                
                if(regex.search(nick_name1) == None) and (0<len(nick_name1)<=12) and 'NICK' in nick:
                    connection.sendall('OK'.encode('utf-8'))
                    break
                elif len(nick_name1) or regex.search(nick_name1) != None:
                    connection.sendall("Error has occured nick name".encode('utf-8'))
                else:
                    connection.close()
                    print(address[0]+"has been disconnected")
                    new_clients.remove(connection)
                    del new_clients[connection]
                    break
            except:
                break
        
        
        while True:
            try:
                if connection in new_clients:
                    msg1= connection.recv(2048).decode('utf-8')
                    msg2= msg1.strip(' MSG ')
                    
                if not msg1:
                    connection.close()
                    print(addr[0]+ 'has been disconnected')
                    new_clients.remove(connection)
                    break
                elif ' MSG ' not in msg1:
                    conn.sendall('Error has been occured'.encode('utf-8'))
                else:
                    if len(msg2) <= 255:
                        j=0
                        for i in msg2[:-1]:
                            if ord(i) < 31:
                                j +=1
                            else:
                                pass
                        if (j!=0):
                            connection.sendall('Errorgiven wrong characters'.encode('utf-8'))
                        else:
                            msg_to_send = ' MSG ' + nick_name1+ ''+ msg2[:-1]
                            broadcasting (msg_to_send, connection, nick_name1)
                    elif len(msg2) > 255:
                        connection.sendall('Error that length of message has exceding')
                        
            except KeyboardInterrupt:
                connection.close()
                break
            
    def broadcasting (msg1, connection, nick_name1,s):
        for i in new_clients:
            if i != s:
                try:
                    i.sendall(msg1.encode('utf-8'))
                except:
                    new_clients.remove(i)
                    break
    while True:
        
        connection ,address = s.accept()
        connection.sendall('hello'.encode('utf-8'))
        new_clients.append(connection)
        print(address[0]+'has been conneted')
        new_connection(client_connection,(connection,address))
        
    connection.close()
    s.close()
                    
                         
                        
               
                
                    
                    
                    
                
    
        
   


