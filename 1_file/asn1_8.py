import os
import sys
import argparse
import struct
import socket
from multiprocessing import Process

def checksum_func(data):
    checksum = 0
    data_len = len(data)
    if (data_len%2) == 1:
        data_len += 1
        data += struct.pack('!B', 0)

    for i in range(0, len(data), 2):
        w = (data[i] << 8) + (data[i + 1])
        checksum += w

    checksum = (checksum >> 16) + (checksum & 0xFFFF)
    checksum = ~checksum&0xFFFF
    return checksum

def main():
    aparser = argparse.ArgumentParser(description = 'Modify UDP message to show the same checksum')
    aparser.add_argument('-s' , type = str , dest = 'sip', nargs = 1, help = 'Server IP Address', required = True)
    aparser.add_argument('-p' , type = int, nargs = 1, dest = 'sport', help = 'Server Port Number', required = True)
    aparser.add_argument('-P' , type = int, nargs = 1, dest = 'cport', help = 'Client Port Number', required = True)
    aparser.add_argument('-d' , type = str , dest = 'data', nargs = 1, help = 'data', required = True)
    options = aparser.parse_args()
    sip = str(options.sip[0])
    sport = options.sport[0]
    cport = options.cport[0]
    data = options.data[0]
    print("Given Arguments\nSIP : "+str(sip)+" SPORT : "+str(sport)+" CPORT : "+str(cport)+" DATA : "+str(data))
    p1 = Process(target=server(sip,sport,cport,data))
    p2 = Process(target=client(sip,sport,cport,data))
    p1.start()
    p2.start()

def client(sip,sport,cport,data):
    csock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    msg = raw_input(data)
    print("Client Sending Data : "+data)
    csock.sendto(msg,(sip,sport))
    mmsg.sip=csock.recvfrom(2048)
    print(mmsg)
    csock.close()

def server(sip,sport,cport,data):
    ssock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ssock.bind((sip,sport))
    print("The server is ready to recieve!")
    while True:
        data, sip = ssock.recvfrom(2048)
        mmsg = msg.uppercase()
        print("Message : "+data)
        ssock.sendto(mmsg,cport)
    ssock.close()

if __name__ == '__main__':
    if(len(sys.argv)==1):
        sys.exit("Enter all arguments\nExpected Format : asn1_8.py -s <server ip address> -p <server port number> -P <client port number> -d <data>")
    elif(len(sys.argv)>9):
        sys.exit("Unknown extra arguments added. Please check the arguments provided, properly")
    else:
        sys.exit(main())
