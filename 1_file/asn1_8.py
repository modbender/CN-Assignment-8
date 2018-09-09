import os
import sys
import argparse
import struct
from socket import *

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
    global sip
    global sport
    global cport
    global data
    aparser = argparse.ArgumentParser(description = 'Modify UDP message to show the same checksum')
    aparser.add_argument('-s' , type = str , dest = 'sip', nargs = 1, help = 'Server IP Address', required = True)
    aparser.add_argument('-p' , type = int, nargs = 1, dest = 'sport', help = 'Server Port Number', required = True)
    aparser.add_argument('-P' , type = int, nargs = 1, dest = 'cport', help = 'Client Port Number', required = True)
    aparser.add_argument('-d' , type = str , dest = 'data', nargs = 1, help = 'data', required = True)
    options = aparser.parse_args()
    sip = options.sip
    sport = options.sport
    cport = options.cport
    data = options.data
    server()
    client()

def client():
    csock = socket(socket.AF_INET,socket.SOCK_DGRAM)
    msg = raw_input(data)
    csock.sendto(msg,(sip,sport))
    mmsg.sip=csock.recvfrom(2048)
    print(mmsg)
    csock.close()

def server():
    ssock = socket(AF_INET,SOCK_DGRAM)
    ssock.bind((sip,sport))
    print("The server is ready to recieve")
    while True:
        msg.ClientAddress = ssock.recvfrom(2048)
        mmsg = msg.uppercase()
        ssock.sendto(mmsg,cport)
    ssock.close()

if __name__ == '__main__':
    if(len(sys.argv)==1):
        sys.exit("Enter all arguments\nExpected Format : asn1_8.py -s <server ip address> -p <server port number> -P <client port number> -d <data>")
    elif(len(sys.argv)>9):
        sys.exit("Unknown extra arguments added. Please check the arguments provided, properly")
    else:
        sys.exit(main())
