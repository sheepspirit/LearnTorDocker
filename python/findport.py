import socket

def find_free_port(start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', port))
        if result != 0:
            return port
        sock.close()
    return None

# Задайте диапазон портов для поиска
start_port = 49153
end_port = 65535

# Найти свободный порт в заданном диапазоне
free_port = find_free_port(start_port, end_port)

if free_port:
    print("Свободный порт:", free_port)
else:
    print("В указанном диапазоне портов нет свободных портов.")