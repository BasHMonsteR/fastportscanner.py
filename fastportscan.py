import threading
from queue import Queue
import time
import socket

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("-"*70)
print(bcolors.WARNING + "**Don't use in on unauthorized network. purely educational purpose**"+ bcolors.ENDC)
print("-"*70)

target = raw_input("target ip = ")
print_lock = threading.Lock()

print("-"*40)

print (bcolors.HEADER + 'scanning................................'+ bcolors.FAIL)
print("-"*40)

open_ports = []

def portscan(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		con = s.connect((target, port))
		with print_lock:
			print"open_port detected ! = ", port
			open_ports.append(port)
		con.close()
	except:
		return False


def threader():
	while True:

		worker = q.get()


		portscan(worker)


		q.task_done()



q = Queue()

for x in range(500):
	t = threading.Thread(target=threader)


	t.daemon = True


	t.start()


start = time.time()

for worker in range(1, 10000):
	q.put(worker)


q.join()
print"open ports are : ",open_ports
