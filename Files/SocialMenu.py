import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHackingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mInstaHack - Best Tool For instagram bruteforce hacking Tool")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mExit System")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Soc1alF1sh: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHackingTools && cd instahack && bash instahack.sh")
elif(op==2):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting utility...")
 sys.exit()
elif(op==3):
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHackingTools")
 os.system("python2 Files/SocialMenu.py")
