import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mPyshell - Remote Access Trojan - RAT")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mWishfish - Powerful Tool For Grab Front Camera Snap Using A Link")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Ma1lHacK: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd Pyshell && ./Pyshell")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd wishfish && ./wishfish.sh")
elif(op==3):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==4):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
