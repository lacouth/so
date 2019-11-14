import socket

orig = ('',5000)

s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s_udp.bind(orig)

print('Servidor no ar...')

while True:
    msg,cliente = s_udp.recvfrom(1024)
    print('Recebi do cliente ', cliente, msg.decode())



