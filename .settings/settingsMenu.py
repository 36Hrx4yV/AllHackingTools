import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mLogo Setting")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mMenu Setting")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mVibration Setting")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mSpecial Opportunities")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mExit System")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Sett1Ngs: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd pyshell && ./Pyshell && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd wishfish && ./wishfish.sh && cd && cd AllHackingTools && python2 MainMenu.py")
elif(op==5):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==6):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 Files/AndroidMenu.py")

