import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mERROR404 - NOT FOUND")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Soc1alF1sh: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==2):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==3):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
