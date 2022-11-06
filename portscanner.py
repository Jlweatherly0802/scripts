import socket
import threading
import queue

q = queue.Queue()
#target = '10.0.0.230'
#ports = 65000
target = input('Target: ')
ports = input('Max number of ports: ')

for x in range(1,int(ports)):
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

        #else:
         #   print('Port {} closed' .format(port))

for x in range(30):
    t = threading.Thread(target=worker)
    t.start()