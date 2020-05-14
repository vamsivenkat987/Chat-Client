                                                    TCP-CHAT-ROOM
The server file and client file should be in same folder.

First run the server python file as “python server.py hostname port” in command prompt. The hostname is the ipv4 address of the device you are using. To find the hostname on your device run “ipconfig” command on it CMD shows the ipv4 address of your device. The given port number should be free on you device otherwise give default port number as 8888.

After running server file run client file as “python client.py hostname port NICKNAME”. The hostname and port are the same details of the server. 

If everything runs successfully then server sends Hello message to clients. Single Server can accept multiple clients. Nickname of the client should be given in the form of “NICK nickname”. The message should be given in the form of “MSG message”. The client broadcasts its messages in the form of “MSG nickname message”.

If you want to exit from the chat-room run “MSG quit” in the client, then that client automatically disconnects from the chat-room. 

