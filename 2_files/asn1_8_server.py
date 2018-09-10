import os
import sys
import argparse
import struct
import socket

def main():
    aparser = argparse.ArgumentParser(description = 'Server - Modify UDP message to show the same checksum')
    aparser.add_argument('-s' , type = str , dest = 'sip', nargs = 1, help = 'Server IP Address', required = True)
    aparser.add_argument('-p' , type = int, nargs = 1, dest = 'sport', help = 'Server Port Number', required = True)
    options = aparser.parse_args()
    sip = str(options.sip[0])
    sport = options.sport[0]

    ssock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ssock.bind((sip,sport))
    # ssock.listen(5)
    print("Server waiting for connection")
    # csock, cip = ssock.accept()
    # print("Connection from : "+cip[0])
    while True:
        data,clientaddr = ssock.recvfrom(1024) #.recv(2048).decode('utf-8')
        if not data:
            print("No data received")
            break

        print("Message : "+ data)
        mmsg = data+data
        ssock.sendto(mmsg,clientaddr)
        #csock.send(mmsg.encode('utf-8'))
    #csock.close()

if __name__ == '__main__':
    if(len(sys.argv)==1):
        sys.exit("Enter all arguments\nExpected Format : asn1_8.py -p <server port number>")
    elif(len(sys.argv)>6):
        sys.exit("Unknown extra arguments added. Please check the arguments provided, properly")
    else:
        sys.exit(main())
