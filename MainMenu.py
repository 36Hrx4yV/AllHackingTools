import requests
from bs4 import BeautifulSoup
import os
import time
import random
import sys

os.system("clear")
os.system("bash Logo.sh")

Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
Purple="\033[0;35m"

print("  # \033[1;34m[ 01 ] >> \033[1;36;40mPhishing-Tool")
print("  # \033[1;34m[ 02 ] >> \033[1;36;40mRouter-Hacking")
print("  # \033[1;34m[ 03 ] >> \033[1;36;40mWifi-Jumming")
print("  # \033[1;34m[ 04 ] >> \033[1;36;40mWeb-DDOS")
print("  # \033[1;34m[ 05 ] >> \033[1;36;40mWeb-AdminHack")
print("  # \033[1;34m[ 06 ] >> \033[1;36;40mAndroid-Hack")
print("  # \033[1;34m[ 07 ] >> \033[1;36;40mSQL injection-Tool")
print("  # \033[1;34m[ 08 ] >> \033[1;36;40mSocialMedia-Hacking")
print("  # \033[1;34m[ 09 ] >> \033[1;36;40mAnon-SMS_Tool")
print("  # \033[1;34m[ 10 ] >> \033[1;36;40mDarkSearch-Tool")
print("  # \033[1;34m[ 11 ] >> \033[1;36;40mMail-Hack")
print("  # \033[1;34m[ 12 ] >> \033[1;36;40mUpdate Utility")
print("  # \033[1;34m[ 13 ] >> \033[1;36;40mAbout Utility")
print("  # \033[1;34m[ 14 ] >> \033[1;36;40mExit Utility")

op=int(raw_input("Options: "))

if(op==1):
 os.system("bash Files/PhishingFiles.sh")
elif(op==2):
 os.system("Python2 SMSbomberMenu.py")
elif(op==3):
 os.system("python2 WifiJummingMenu.py")
elif(op==4):
 os.system("python2 WebDDOSMenu.py")
elif(op==5):
 os.system("python2 WebAdminHackMenu.py")
elif(op==6):
 os.system("python2 AndroidHackMenu.py")
elif(op==7):
 os.system("python2 SQLinjectionMenu.py")
elif(op==8):
 os.system("python2 SocialMenu.py")
elif(op==9):
 os.system("bash files/AnonSMSMenu.sh")
elif(op==10):
 os.system("python2 DarkSearchMenu.py")
elif(op==11):
 os.system("python2 MailHackMenu.py")
elif(op==12):
 os.system("cd && rm -rf AutoUpdateMyTools && git clone https://github.com/mishakorzik/AutoUpdateMyTools")
 os.system("cd AutoUpdateMyTools")
 os.system("bash AllHackingToolupdate.sh")
elif(op==13):
 os.system("bash src/About.sh")

elif(op==14):
 print("\033[1;31;40mQuiting utility...")
 time.sleep(1)
 sys.exit()
else:
 print("\033[1;31;40mInvalid input. Quiting...")
 time.sleep(1)
 sys.exit()
