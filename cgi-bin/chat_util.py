#!/usr/bin/python
print "Content-type:text/plain"
print ""

import socket
import sys
import os
import cgi, cgitb
import math
import json

def idToIP(id):
   ip = "172.20."
   msb = int(math.floor(int(id)/256))
   lsb = int(int(id) - msb * 256)
   ip = ip + str(msb) + '.' + str(lsb)
   return ip

def IPToid(ip):
   ip2 = ip.split('.')[2]
   ip3 = ip.split('.')[3]
   id = int(ip2) * 256 + int(ip3)
   return str(id)


HISTORY_PATH='/tmp/mnt/im_history'
f = open('/dev/shm/radio/nodeid','r')
NODEID = f.read().splitlines()[0]
f.close()
NODEIP = idToIP(NODEID)

NICK_FILE = "/usr/local/cgi-bin/web_im/nickname"
if os.path.isfile(NICK_FILE):
    nick_f = open(NICK_FILE, 'r')
    NICKNAME = nick_f.read().splitlines()[0]
    nick_f.close()
else:
    NICKNAME = NODEID


form = cgi.FieldStorage()

cmd = form.getvalue('cmd')

def send_message(message, remote_ip):
    global NODEID
    global NODEIP
    global NICKNAME
    #create an AF_INET, STREAM socket(TCP)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print 'Failed to create socket. Error code:' + str(msg[0]) + ', Error message : ' + msg[1]
        sys.exit()
    
    print "Socket Created"
    
    host = remote_ip
    port = 3721
    
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print "Hostname could not be resolved. Exiting"
        sys.exit()
    
    print "Ip address of " + host + " is " + remote_ip
    #connect to remote server
    try:
        s.connect((remote_ip, port))
    except socket.error, msg:
        print "Error code:" + str(msg[0]) + ', Error message :' + msg[1]
        sys.exit()

    print "Socket Connected to " + host + " on ip " + remote_ip
    #if NICKNAME == "": 
    s_message = '{ "Nodeid": %s, "NodeIP": %s, "Nickname": %s,"Message": %s}' % (NODEID, NODEIP, NICKNAME, message)
    #else:
    #    s_message = NICKNAME + "(" + NODEIP + "): " + message

    remote_id = IPToid(remote_ip)
    history_file = HISTORY_PATH + "/" + remote_id
    f = open(history_file, 'a')
    his_msg = "<p> me: " + message + "</p>"
    f.write(his_msg)
    f.close()
   
    #send some data to remote server
    try:
        #send the whole string
        s.sendall(s_message)
    except socket.error:
        print "send failed"
        sys.exit()
    
    print "Message sent successfully"
    
    #now receive data
    reply = s.recv(4096)
    
    print reply
    
    #close 
    s.close()

def close_chat():
   os.system('killall -KILL chat_server.py') 

def connect_remote(remote_ip):
    #create an AF_INET, STREAM socket(TCP)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print 'Failed to create socket. Error code:' + str(msg[0]) + ', Error message : ' + msg[1]
        sys.exit()
    
    print "Socket Created"
    
    host = remote_ip
    port = 3721
    
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print "Hostname could not be resolved. Exiting"
        sys.exit()
    
    print "Ip address of " + host + " is " + remote_ip
    #connect to remote server
    try:
        s.connect((remote_ip, port))
    except socket.error, msg:
        print "Error code:" + str(msg[0]) + ', Error message :' + msg[1]
        sys.exit()

    print "Socket Connected to " + host + " on ip " + remote_ip

    s.close()

def clear_history(remote_node_id):
    global HISTORY_PATH
    history_file = HISTORY_PATH + "/" + remote_node_id
    os.remove(history_file)    

def clear_all_history():
    global HISTORY_PATH
    remove_all_cmd = "rm -rf %s" % HISTORY_PATH
    os.system(remove_all_cmd)

def change_nickname(nickname):
    f = open('/usr/local/cgi-bin/web_im/nickname', 'w')  
    f.write(nickname)
    f.close()

'''
def update_msg(remote_node_id):
    global HISTORY_PATH
    history_file = HISTORY_PATH + "/" + remote_node_id
    f = open(history_file, 'r') 
    print f.read()
    f.close()
    sys.exit()
'''

if __name__ == "__main__":
    if cmd == "send_msg":
        message = form.getvalue('msg')
        remote_ip = form.getvalue('remote_ip')
        send_message(message, remote_ip)
    elif cmd == "close_chat":
        close_chat()
    elif cmd == "connect_remote":
        remote_ip = form.getvalue('remote_ip')
        connect_remote(remote_ip)
    elif cmd == "clear_history":
        remote_node_id = form.getvalue('remote_node_id')
        clear_history(remote_node_id)
    elif cmd == "clear_all_history":
        clear_all_history()
    elif cmd == "change_nickname":
        nickname = form.getvalue('nickname')
        change_nickname(nickname)
        

