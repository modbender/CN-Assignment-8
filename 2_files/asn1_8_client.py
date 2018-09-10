import os
import sys
import argparse
import struct
import socket

def main():
    aparser = argparse.ArgumentParser(description = 'Client - Modify UDP message to show the same checksum')
    aparser.add_argument('-s' , type = str , dest = 'sip', nargs = 1, help = 'Server IP Address', required = True)
    aparser.add_argument('-p' , type = int, nargs = 1, dest = 'sport', help = 'Server Port Number', required = True)
    aparser.add_argument('-P' , type = int, nargs = 1, dest = 'cport', help = 'Client Port Number', required = True)
    aparser.add_argument('-d' , type = str , dest = 'data', nargs = 1, help = 'data', required = True)
    options = aparser.parse_args()
    sip = options.sip[0]
    sport = options.sport[0]
    cport = options.cport[0]
    data = options.data[0]

    csock = socket.socket()
    csock.connect((sip,sport))
    print("Connected to server : "+str(sip))
    msg = data
    print("Sending to Server: "+data)
    csock.sendto(msg.encode('utf-8'),(sip,sport))
    mmsg,sip = csock.recvfrom(2048)
    mmsg = mmsg.decode('utf-8')
    print("Received Modified Message : "+str(mmsg))

if __name__ == '__main__':
    if(len(sys.argv)==1):
        sys.exit("Enter all arguments\nExpected Format : asn1_8.py -s <server ip address> -p <server port number> -P <client port number> -d <data>")
    elif(len(sys.argv)>9):
        sys.exit("Unknown extra arguments added. Please check the arguments provided, properly")
    else:
        sys.exit(main())
