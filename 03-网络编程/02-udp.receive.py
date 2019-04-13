from socket import *

udpSocket=socket(AF_INET,SOCK_DGRAM)

udpSocket.bind(('',7788))

udpSocket.sendto(b"haha",("10.13.2.189",8080))
 
recvdata=udpSocket.recvfrom(1024)
print(recvdata)

udpSocket.close()
