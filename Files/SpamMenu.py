import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mSMS-Bomber-300")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mXLR8_BOMBER")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mAnon-SMS")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mAres-Bomb")
print("  # \033[1;34m[ 5 ] >> \033[1;36;40mExit")
print("  # \033[1;34m[ 6 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Phishing: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd SMS-Bomber-300-Free && python SMS-Bomber.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd XLR8_BOMBER && bash xlr8.sh")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Anon-SMS && bash Run.sh")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd AresBomb && python boom.py")
elif(op==5):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==6):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
 
