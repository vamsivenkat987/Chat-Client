import select
import socket
import sys
import time
import errno
class client_socket:
    def __init__(self):
        try:
            self.client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print('socket created')
        except socket.error :
            print('Socked not created')
            sys.exit()
        self.host = sys.argv[1]
        self.port = int(sys.argv[2])
        self.nick_name = sys.argv[3]
        if(len(sys.argv)!=4):
            sys.exit()
        try:
            self.client_sock.connect((self.host,self.port))
            print('client connected')
        except socket.error :
            print('server not found')
            sys.exit()
        self.nick_name = bytes(self.nick_name ,'utf-8')
        self.client_sock.send(self.nick_name)
        self.client_sock.setblocking(False)
    def run_client(self):
        while True:
            try:
                data = input()
                data = bytes(data,'utf-8')
                self.client_sock.send(data)
            except IOError:
                continue
            try:
                data = self.client_sock.recv(1024)
                print(data)
            except IOError:
                continue   
        self.client_sock.close()     
def main():
    client_obj = client_socket()
    client_obj.run_client()
if __name__ == "__main__":
    main()
