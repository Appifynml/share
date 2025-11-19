import socket
import os

PORT = 9999
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

print(os.path.realpath(os.path.abspath(__file__)))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

file = open("C:\\Users\\Pawan Kumar\\Documents\\Programming Files\\Python\\imgs\\bg.png", "rb")
file_size = os.path.getsize("C:\\Users\\Pawan Kumar\\Documents\\Programming Files\\Python\\imgs\\bg.png")

client.send(str(file_size).encode())

client.sendall(file.read())

file.close()
client.close()