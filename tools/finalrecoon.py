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
print("")
print(
"""                      _____ _             _ ____                      \033[0m
                    \033[36m |  ___(_)_ __  \033[1;33m __ _| |  _ \ ___  ___ ___  _ __  \033[0m
                    \033[36m | |_  | | '_ \ \033[1;33m/ _` | | |_) / _ \/ __/ _ \| '_ \ \033[0m
                    \033[36m |  _| | | | | |\033[1;33m (_| | |  _ <  __/ (_| (_) | | | |\033[0m
                    \033[36m |_|   |_|_| |_|\033[1;33m\__,_|_|_| \_\___|\___\___/|_| |_|  \033[0m"""
)
print("")
print("""
\033[1;34m  --headers   Header Information\033[0m
\033[1;34m  --sslinfo   SSL Certificate Information\033[0m
\033[1;34m  --whois     Whois Lookup\033[0m
\033[1;34m  --crawl     Crawl Target\033[0m
\033[1;34m  --dns       DNS Enumeration\033[0m
\033[1;34m  --sub       Sub-Domain Enumeration\033[0m
\033[1;34m  --trace     Traceroute\033[0m
\033[1;34m  --dir       Directory Search\033[0m
\033[1;34m  --ps        Fast Port Scan\033[0m
\033[1;34m --full      Full Recon\033[0m"""
)
print("")
url = input("" + Reset + "[" + Blue + "ENTER " + Red + "The " + Green + "Domain " + pink + "To Test" + Reset + "]" + Green + ": " + Reset)
print("")
options = input("" + Reset + "[" + Blue + "ENTER " + Red + "The " + Green + "OPtions" + Reset + "]" + Green + ": " + Reset)
subprocess.check_call(['python3', './tools/FinalRecon/finalrecon.py', url, options])
