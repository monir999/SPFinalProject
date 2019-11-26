from appJar import gui 
import socket #import AF_INET, socket, SOCK_STREAM
from threading import Thread

def receive():
    """This function are taking care receiving messages"""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            if msg != "":
                app.addListItem("History", msg)
        except OSError:  # Possibly client has left the chat.
            break

def send():  # event is passed by binders.
    """This function are taking care sending messages"""
    msg = app.getEntry("send_txt")
    if msg != "":
        app.clearEntry("send_txt")
        client_socket.send(bytes(msg, "utf8"))
        if msg == "{quit}":
            client_socket.close()
            app.clearEntry("send_txt")
            app.stop()

# Create Appjar GUI window
app = gui("Scoket chat window", "500x250", sticky="ew", expand="all", bg="grey")
# This is Listbox for history of chat
app.listbox("History", [], pos=(0, 0, 1, 4), bg="white") 
# Input option: By pressing 'Enter', text will forward to the server
app.entry("send_txt", pos=(4, 0), bg="white", submit=send, default=":: Type your text ::")
app.addButtons(["Cancel"], [app.stop])

# Implementing Socket
HOST = input('Enter host:')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDR)


receive_thread = Thread(target=receive)
receive_thread.start()

"""This a final execution to run GUI Appjar"""
app.go()




