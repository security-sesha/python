import os
import sys
import socket


#ip = sys.argv[1]


for port in range(1,1024):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.214.131',port))
        s.send('Sesha\n')
        banner = s.recv(1024)
        if banner:
            print "[+]Scanning for Port:", port
            print banner
        s.close()           
    except:
        pass
