import os
import subprocess
#########################
Green="\033[1;33m"
Blue="\033[1;34m"
Reset="\033[0m"
Red="\033[1;31m"
pink = "\033[95m"
#########################
os.system("clear")
print("" + Red + "This Tool Not Work 1st Time Try 2nd time work successfully")
print("")
url = input("" + Reset + "[" + Blue + "ENTER " + Red + "USERNAME " + Reset + "]" + Green + ": " + Reset)
print("")
options = input("" + Reset + "[" + Blue + "ENTER " + Red + "PASSWOARD " + Reset + "]" + Green + ": " + Reset)
subprocess.check_call(['python3', './tools/SocialFish/SocialFish.py', url, options])
