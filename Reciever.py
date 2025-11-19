import socket
import tqdm

PORT = 9999
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()

client, addr = server.accept()

file_size = client.recv(1024).decode()

print(f"Connected from user: {addr}")

file_name = str(input("Enter the file name: "))

file = open(file_name, "wb")

bytes_data = b""

progress = tqdm.tqdm(range(0, int(file_size)), ncols= 100)

while True:
    bytes_received = client.recv(1024)
    
    if not bytes_received:
        break;

    bytes_data += bytes_received
    progress.update(len(bytes_received))

file.write(bytes_data)

file.close()
client.close()
server.close()