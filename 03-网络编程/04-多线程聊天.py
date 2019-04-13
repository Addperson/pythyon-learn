
from threading import Thread
from socket import *

udpSocket=None
destIp=""
destPort=0

#收数据
def recvData():
    while True:
        recvInfo=udpSocket.recvfrom(1024)
        print("[%s]:%s"%(str(recvInfo[1]),recvInfo[0].decode("gb2312")))

#发数据
def sendData():
    while True:
        sendInfo=input("<<")
        udpSocket.sendto(sendInfo.encode("gb2312"),(destIp,destPort))



def main():
    global udpSocket
    global destIp
    global destPort
    destIp = input()
    destPort=int(input("发生的端口:"))
    udpSocket=socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind(("", 2345))


    tr=Thread(target=recvData)
    ts=Thread(target=sendData)

    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__=="__main__":
    main()
