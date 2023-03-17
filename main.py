import socket
import threading

# Configuration du serveur
server = "chat.freenode.net"
port = 6667

# Configuration de l'utilisateur
nickname = "DALM1"
channel = "#DALM1_channel"

# Connexion au serveur IRC
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send(f"USER {nickname} {nickname} {nickname} :Python IRC\r\n".encode())
irc.send(f"NICK {nickname}\r\n".encode())
irc.send(f"JOIN {channel}\r\n".encode())

# Fonction pour envoyer les messages aux autres utilisateurs
def send_message(message):
    irc.send(f"PRIVMSG {channel} :{message}\n".encode())

# Fonction pour lire les messages entrants
def read_messages():
    while True:
        data = irc.recv(2048).decode()
        if data.startswith("PING"):
            irc.send("PONG\n".encode())
        else:
            username = data.split('!')[0][1:]
            message = data.split('PRIVMSG')[1].split(':')[1].strip()
            print(f"[{username}] {message}")

# Démarrage du thread pour lire les messages entrants
thread = threading.Thread(target=read_messages)
thread.start()

# Boucle principale pour envoyer les messages
while True:
    message = input("")
    send_message(message)
