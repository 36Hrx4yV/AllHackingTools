import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  # \033[1;34m[ 1 ] >> \033[1;36;40mShark - Future Of Phishing With less delay")
print("  # \033[1;34m[ 2 ] >> \033[1;36;40mZphisher - An automated phishing tool with 30+ templates")
print("  # \033[1;34m[ 3 ] >> \033[1;36;40mShellphish - Modded version of shellphish")
print("  # \033[1;34m[ 4 ] >> \033[1;36;40mSayCheese - Grab target's webcam shots by link")
print("  # \033[1;34m[ 5 ] >> \033[1;36;40mBlackPhish - It's easy phishing tool")
print("  # \033[1;34m[ 6 ] >> \033[1;36;40mExit Utility")
print("  # \033[1;34m[ 7 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Phishing: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd shark && shark")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd zphisher && bash zphisher.sh")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd ShellPhish && bash shellphish.sh")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd saycheese && bash saycheese.sh")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd BlackPhish && sudo python3 blackphish.py")
elif(op==6):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==7):
 os.system("cd")
 os.system("cd AllHackingTool")
 os.system("python2 MainMenu.py")
 
