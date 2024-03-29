# Python Socket Programming Done By : Palash Roy and MD Moniruzzaman
#!/usr/bin/env python3
<<<<<<< HEAD

"""Server for multithreaded (asynchronous) chat application."""
=======
>>>>>>> update1
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome to live chat!! Type your name and press Enter!!", "utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()
<<<<<<< HEAD

=======
>>>>>>> update1

def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

<<<<<<< HEAD
=======
def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

>>>>>>> update1
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you want to quit, please type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        try:
            msg = client.recv(BUFSIZ)
            if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
            else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break
        except OSError:
            break

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = '' 
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Connection in progress......")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
