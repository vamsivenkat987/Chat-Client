import select
import socket
import sys
import time
import errno
import read
class client_socket:
    def __init__(self):
        try:
            self.client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)         
            print('socket created')
        except socket.error :
            print('Socked not created')
            sys.exit()
        self.host = sys.argv[1]
        self.port = int(sys.argv[2])
        self.nick_name = str(sys.argv[3])
        if(len(sys.argv)!=4):
            sys.exit()
        try:
            self.client_sock.connect((self.host,self.port))
            print('client connected')
        except socket.error :
            print('server not found')
            sys.exit()
        first_message = self.client_sock.recv(2048).decode('utf-8'))
        print(first_message)
        self.nick_name = 'NICK' +self.nick_name
        self.nick_name = bytes(self.nick_name ,'utf-8')
        self.client_sock.send(self.nick_name)
        self.client_sock.setblocking(False)
        okay_message = self.client_sock.recv(2048).decode('utf-8'))
        if okay_message == "OK":
            pass
        elif okay_message == "Error malformed":
            print("please enter nick name with in 12 letters with specific characters")
            sys.exit()
          
        
    def run_client(self):
        while True:
            try:
                data = input()
                data = bytes(data,'utf-8')
                self.client_sock.send(data)
            except IOError:
                continue
            list_sock = [sys.stdin , self.client_sock]
            read_sockets,write_sockets,error_sockets=select.select(list_sock[])
                
            try:
                for i in read_sockets:
                    if sockets == self.client_sock:
                    data = self.client_sock.recv(1024)
                    print(data)
                else:
                    data = sys.stdin.readline()
                    data= ' MSG '+ data
                    if data == '\n':
                        continue
                    else:
                        self.client_sock.sendall(messgae.encode('utf-8'))
             
            except IOError:
                continue   
        self.client_sock.close()     
def main():
    client_obj = client_socket()
    client_obj.run_client()
if __name__ == "__main__":
    main()
