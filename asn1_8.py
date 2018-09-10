import os
import sys
import argparse
import struct
import socket
import threading

class Server(threading.Thread):
  def __init__(self, threadID, name, counter,server_ip,server_port):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.server_ip = server_ip
        self.server_port = server_port
  def run(self):
      print ("Starting " + self.name)
      # Get lock to synchronize threads
      # threadLock.acquire()
      serverSide(self.server_ip,self.server_port)
      # Free lock to release next thread
      # threadLock.release()

class Client(threading.Thread):
  def __init__(self, threadID, name, counter,server_ip,server_port,data_to_be_sent):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.server_ip = server_ip
        self.server_port = server_port
        self.data_to_be_sent = data_to_be_sent
  def run(self):
      print ("Starting " + self.name)
      # Get lock to synchronize threads
      # threadLock.acquire()
      clientSide(self.server_ip,self.server_port,self.data_to_be_sent)
      # Free lock to release next thread
      # threadLock.release()

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
    threads = []
    # Create new threads
    serverThread = Server(1,'server',1,sip,sport)
    clientThread = Client(2,'client',2,sip,sport,data)
    # Start new Threads
    serverThread.start()
    clientThread.start()
    # Adding threads to thread list
    threads.append(serverThread)
    threads.append(clientThread)

    for t in threads:
      t.join()
    print("Exiting main thread")

def serverSide(server_ip,server_port):
  ssock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  ssock.bind((server_ip,server_port))
  # ssock.listen(5)
  print("Server waiting for connection")
  # while True:
  data,clientaddr = ssock.recvfrom(1024) #.recv(2048).decode('utf-8')
  #   if not data:
  #       print("No data received")
  #       break
  print("Message : "+ data)
  mmsg = data+data
  ssock.sendto(mmsg,clientaddr)
  ssock.close()

def clientSide(server_ip,server_port,data_to_be_sent):
  csock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
  csock.connect((server_ip,server_port))
  print("Connected to server : "+str(server_ip))
  msg = data_to_be_sent
  print("Sending to Server: "+data_to_be_sent)
  csock.sendto(msg,(server_ip,server_port))
  mmsg,sip = csock.recvfrom(1024)
  mmsg = mmsg.decode('utf-8')
  print("Received Modified Message : "+str(mmsg))


if __name__ == '__main__':
  if(len(sys.argv)==1):
      sys.exit("Enter all arguments\nExpected Format : asn1_8.py -s <server ip address> -p <server port number> -P <client port number> -d <data>")
  elif(len(sys.argv)>9):
      sys.exit("Unknown extra arguments added. Please check the arguments provided, properly")
  else:
      sys.exit(main())