import queue
import socket
import threading

q = queue.Queue()

list = []
user = ''
mode = input('Range or list(r or l): ')
target = input('Target: ')

if mode == 'r':
    ports = input('Max number of ports: ')
    for x in range(1,int(ports)):
        q.put(x)
    
elif mode == 'l':
    while user != 'q':
        user = input('Enter port: ') 
        list.append(user)
    list.pop()     
    
    for x in list:
        q.put(x) 
    

def Pscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect((target, port))
        return True 

    except:
        return False 

def worker():
    while True:
        port = q.get()
        if Pscan(port):
            print('Port {} open' .format(port))
        elif q.empty():
            break

        else:
            print('Port {} closed' .format(port))

for x in range(30):
    t = threading.Thread(target=worker)
    t.start()