import select
import socket
import sys
import time
class socket_server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        try:
            self.server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            print('socket created')
        except socket.error:      
            print('Socked not created')
            sys.exit()
        self.server_sock.bind((self.host,self.port))
        self.server_sock.listen(10)
    
    def server_run(self):
        client_list = [self.server_sock]
        nick_list =[]
    
        while True:
            read_list,write_list,error_list = select.select(client_list,[],[])
            if self.server_sock in read_list:
                connection ,address = self.server_sock.accept()
                nick_name = connection.recv(1024)
                print('New_connection {} established',format(nick_name))
                
                data = 'hello '
                data = bytes(data,'utf-8')
                data = data + nick_name
                connection.send(data)
                nick_list.append(nick_name)
                client_list.append(connection)
            for client in read_list:
                if client != self.server_sock:
                    try:
                        data = client.recv(1024)
                        if(len(data)!=0):
                            print(data)
                        if(len(client_list)>2):
                            for i in client_list:
                                if i != client and i !=self.server_sock:
                                    i.send(data)
                    except IOError:
                        continue
def main():
    ser = socket_server(sys.argv[1],int(sys.argv[2]))
    ser.server_run()
if __name__ == "__main__":
    main()



