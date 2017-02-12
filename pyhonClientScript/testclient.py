import socket   
import sys  
import struct
import time

#main function
if __name__ == "__main__":

    if(len(sys.argv) < 2) :
        print 'Usage : python client.py hostname'
        sys.exit()

    host = sys.argv[1]
    port = 8080

#create an INET, STREAMing socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

print 'Socket Created'

try:
    remote_ip = socket.gethostbyname( host )
    s.connect((host, port))

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

print 'Socket Connected to ' + host + ' on ip ' + remote_ip

#Send some data to remote server
message = "Test"

try :
    #Set the whole string
    while True:
        try:
            print "Reconnecting"
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_ip = socket.gethostbyname( host )
            s.connect((host, port))
        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        s.send(message)
        time.sleep(1.0005)
        k=s.recv(15)
        print "Got Data:",k
        #time.sleep(1)
        
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()
s.close()