clear
g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"
echo "╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╭╮╱╱╱╱╱╱╭━━━━╮╱╱╭━━━╮╭╮╱╱╱╱╱╭╮"
echo "┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱┃╭━━╯╱╭╯╰╮╱╱╱╱╱┃╭╮╭╮┃╱╱┃╭━╮┣╯╰╮╱╱╱╭╯╰╮"
echo "┃╰━╯┣━┳━━┳━━┳━━╮┃╰━━┳━╋╮╭╋━━┳━╮╰╯┃┃┣┻━╮┃╰━━╋╮╭╋━━┳┻╮╭╯"
echo "┃╭━━┫╭┫┃━┫━━┫━━┫┃╭━━┫╭╮┫┃┃┃━┫╭╯╱╱┃┃┃╭╮┃╰━━╮┃┃┃┃╭╮┃╭┫┃"
echo "┃┃╱╱┃┃┃┃━╋━━┣━━┃┃╰━━┫┃┃┃╰┫┃━┫┃╱╱╱┃┃┃╰╯┃┃╰━╯┃┃╰┫╭╮┃┃┃╰╮"
echo "╰╯╱╱╰╯╰━━┻━━┻━━╯╰━━━┻╯╰┻━┻━━┻╯╱╱╱╰╯╰━━╯╰━━━╯╰━┻╯╰┻╯╰━╯"
echo "Please press enter to launch..."
read a1
echo -e $b">"$w" verify modules: "$g"python2"$w
apt-get install python
echo -e $b">"$w" verify modules: "$g"pip3"$w
apt-get install pip3
echo -e $b">"$w" verify modules: "$g"requests"$w
pip3 install requests
echo -e $b">"$w" verify modules: "$g"php"$w
apt-get install php
echo -e $b">"$w" verify modules: "$g"bs4"$w
apt-get install bs4
echo -e $b">"$w" verify modules: "$g"wget"$w
apt-get install wget
echo -e $b">"$w" verify modules: "$g"openssh"$w
apt-get install openssh
echo "Succesfull verifined!"
clear
bash Logo.sh
sleep 1
python2 MainMenu.py
