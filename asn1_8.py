import os
import sys
import argparse

def main():
    aparser = argparse.ArgumentParser(description = 'Modify UDP message to show the same checksum')
    aparser.add_argument('-s' , type=str , dest = 'sip', nargs = 1, help = 'Server IP Address', required = True)
    aparser.add_argument('-p' , type = int, nargs = 1, dest = 'sport', help = 'Server Port Number', required = True)
    aparser.add_argument('-P' , type = int, nargs = 1, dest = 'cport', help = 'Client Port Number', required = True)
    aparser.add_argument('-d' , type=str , dest = 'data', nargs = 1, help = 'data', required = True)
    options = aparser.parse_args()
    sip = options.sip
    sport = options.sport
    cport = options.cport
    data = options.data

    print("Content yet to be added")

if __name__ == '__main__':
    if(len(sys.argv)==1):
        sys.exit("Enter all arguments\nExpected Format : asn1_8.py -s <server ip address> -p <server port number> -P <client port number> -d <data>")
    elif(len(sys.argv)>9):
        sys.exit("Unknown extra arguments added. Please check the arguments provided, properly")
    else:
        sys.exit(main())
