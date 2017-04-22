import socket   
import sys  
import struct
import time
import numpy as np

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
message = "a"

#collecting in database
data=np.zeros((5,5))
i=0
j=0
try :
    #Set the whole string
    while True:
        try:
            #Cant we go without reconnecting at each step. is there any way to stop closing connection betwen them.
            #print "Reconnecting"
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_ip = socket.gethostbyname( host )
            s.connect((host, port))
        except socket.gaierror:
            print 'Hostname could not be resolved. Exiting'
            sys.exit()
        s.send(message)
        time.sleep(.3)  #.3 seems optimal
        k=s.recv(15)
        print k
        ''' BEWARE: As there ight be delay in receiving i.e 1 ok 2 ok none none 3 received at posiotin of 5 will offset the whole data
         So, Keep a ending delimiter after every row so that we dont offset next row (maybe counter can be used) by mistake.'''
        '''if i<5:
            try:
                data[i,j]=float(k)
                
            except:
                data[i,j]=10
        j=j+1
        if j==5:
            j=0
            i=i+1'''
        
        #print "Got Data:",data #no much effect of using print function
        '''try:
            if float(k)>200:
                print "Got Data:",k
        except:
            temp=1'''
        #time.sleep(1)
        
except socket.error:
    #Send failed
    print 'Send failed'
    sys.exit()
s.close()