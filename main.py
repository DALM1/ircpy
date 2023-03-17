import socket

server = "chat.freenode.net"
port = 6667
nickname = "my_nickname"
channel = "#my_channel"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send(f"USER {nickname} {nickname} {nickname} :Python IRC\r\n".encode())
irc.send(f"NICK {nickname}\r\n".encode())
irc.send(f"JOIN {channel}\r\n".encode())

while True:
    data = irc.recv(1024).decode()
    if data.startswith("PING"):
        irc.send("PONG\n".encode())
    else:
        print(data)
