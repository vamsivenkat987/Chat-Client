import select
import socket
import sys
import time
import re
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
        self.server_sock.setblocking(1)
    def server_run(self):
        client_list = [self.server_sock]
        w=[]
        nick_list =[]
        new_=[]
        dic = {}
        while True:
            read_list,write_list,error_list = select.select(client_list,w,[])
            if self.server_sock in read_list:
                connection ,address = self.server_sock.accept()
                print('New_connection {} established',format(address))
                nick_name = connection.recv(1024)
                sys.stdout.flush()
                nick_len = len(nick_name)
                msg = 'Hello'
                msg = bytes(msg,'utf-8')
                connection.send(msg)
                connection.setblocking(0)
                nick_list.append(nick_name)
                clint = (connection,address)
                client_list.append(connection)
                dic [connection] = 1
                print('ok')
            for client in read_list:
                if client != self.server_sock:
                    try:
                        data = client.recv(1024)
                        print(data)
                        if dic[client] == 1:
                            data = data.decode('utf-8')
                            data1 = data.strip('NICK')
                            print(data)
                            if data[0:4] !='NICK':
                                msg = 'Error occured in nick name'
                                msg = bytes(msg,'utf-8')
                                client.send(msg)
                            else:
                                 if len(data1)<=12 and len(data1)>=0:
                                    list = ['!','@','#','$','%','^','&','*','(',')','{','}','[',']',':','/','>','<','~']
                                    count = 0
                                    for i in range(len(list)):
                                        if list[i] in data1:
                                            count = count +1
                                    if count==0:
                                        msg = 'ok'
                                        msg = bytes(msg,'utf-8')
                                        client.send(msg)
                                        dic[client] = 0
                                    else:
                                        print('error')
                                        msg = ('error')
                                        msg = bytes(msg,'utf-8')
                                        client.send(msg)
                        else:
                            msg = data.decode('utf-8')
                            msg1 = msg.strip('MSG')
                            print(msg)
                            if msg[0:3] != 'MSG':
                                data = 'Message should be send in MSG and text'
                                data = bytes(data,'utf-8')
                                client.send(data)
                            else:
                                if len(msg) <= 255:
                                    count =0
                                    for i in msg[:-1]:
                                        if ord(i)<31:
                                            count = count +1
                                        else:
                                            pass
                                    if count != 0:
                                        data = 'Error occured in in control characters'
                                        data = bytes(data,'utf-8')
                                        client.send(data)
                                    else:
                                        print('okkk')
                                        for i in client_list:
                                            if i!=self.server_sock and i!=client:
                                                i.send(data)
                                elif len(msg) >256:
                                    data = 'message should be less than 256 characters'
                                    data = bytes(data,'utf-8')
                                    client.send(data)
                    except IOError:
                        continue
                        
def main():
    ser = socket_server(sys.argv[1],int(sys.argv[2]))
    ser.server_run()
if __name__ == "__main__":
    main()

