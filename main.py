import socket
import threading

server = "chat.freenode.net"
port = 6667
nickname = "DALM1"
channel = "#DALM1_channel"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send(f"USER {nickname} {nickname} {nickname} :Python IRC\r\n".encode())
irc.send(f"NICK {nickname}\r\n".encode())
irc.send(f"JOIN {channel}\r\n".encode())

def read_messages():
    while True:
        data = irc.recv(1024).decode()
        if data.startswith("PING"):
            irc.send("PONG\n".encode())
        elif "PRIVMSG" in data:
            try:
                message = data.split('PRIVMSG')[1].split(':')[1].strip()
                print(message)
            except IndexError:
                pass

def send_message(message):
    irc.send(f"PRIVMSG {channel} :{message}\r\n".encode())

threading.Thread(target=read_messages).start()

while True:
    message = input("")
    send_message(message)
