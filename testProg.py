#!/usr/bin/env python3
import unittest
import threading
import socket
from chat_server import SERVER, accept_incoming_connections

def create_test_server():
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = threading.Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()

class ServerTest(unittest.TestCase):
        
    def test_server(self):
        print('Creating Test Server')
        # Start server in a background thread
        server_thread = threading.Thread(target=create_test_server)
        server_thread.start()

        fake_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        fake_client.settimeout(1)
        fake_client.connect(('127.0.0.1', 33000))
        
        while True:
            try:
                msg = fake_client.recv(1024).decode("utf8")
                if msg != "":
                    print(msg)
            except OSError:  # Possibly client has left the chat.
                break

        fake_client.send(bytes("Admin", "utf8"))
        while True:
            try:
                msg = fake_client.recv(1024).decode("utf8")
                if msg != "":
                    print(msg)
            except OSError:  # Possibly client has left the chat.
                break

        fake_client.send(bytes("{quit}", "utf8"))
        while True:
            try:
                msg = fake_client.recv(1024).decode("utf8")
                if msg != "":
                    print(msg)
                    if msg == "{quit}":
                        fake_client.close()
            except OSError:  # Possibly client has left the chat.
                break

class ClientTest(unittest.TestCase):
        
    def run_server(self):
        # Run a server to listen for a connection and then close it
        server_sock = socket.socket()
        server_sock.bind(('127.0.0.1', 33000))
        server_sock.listen(0)
        server_sock.accept()
        server_sock.close()

    def test_client(self):
        print("Creating Test Client")
        # Start fake server in background thread
        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

        # Test the clients basic connection and disconnection
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 33000))
        client.close()

        # Ensure server thread ends
        server_thread.join()


if __name__ == '__main__':
    unittest.main()
