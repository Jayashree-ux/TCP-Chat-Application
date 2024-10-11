import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on

clients = []

# Function to handle individual clients
def handle_client(client_socket, address):
    print(f"[NEW CONNECTION] {address} connected.")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            print(f"[MESSAGE FROM {address}] {message}")
            broadcast_message(f"{address}: {message}", client_socket)
        except:
            print(f"[ERROR] Failed to receive message from {address}")
            break

    print(f"[DISCONNECT] {address} disconnected.")
    clients.remove(client_socket)
    client_socket.close()

# Function to broadcast messages to all clients
def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                print("[ERROR] Failed to send message.")

# Start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[LISTENING] Server is running on {HOST}:{PORT}")

    while True:
        client_socket, address = server.accept()
        clients.append(client_socket)

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
