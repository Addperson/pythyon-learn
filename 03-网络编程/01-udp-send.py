from socket import *

udpSocket=socket(AF_INET,SOCK_DGRAM)

udpSocket.sendto(b"haha",("10.13.2.189",8080))
