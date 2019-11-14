import socket

print('Produtor no ar')

dest = ('10.0.4.187',5000)

s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('Digite a mensagem: ')
    s_udp.sendto(msg.encode(),dest)


