import subprocess
import sys
from banner import ipb, banner, macb, suc, eb, banner2, banneros, mailb, keys, mail_sacn, port_scan, port_re, multipal_mail_scan, nick_name_to_mail, multiple_nick_name, phone_number_founds, find_account_by_name, ping, hashbanner, single_IP, s_a_ip_r, ip_lists# ---> Banner
from banner import single_port, range_of_port, all_ports, tcps, tcpsyns, uuddpp, igonrrr, osd1, osd2, osd3, wss, wss1, wss8, httppss, jom, rb, dns
from bs4 import BeautifulSoup
from collections import deque
import json
import os
import re
import requests
import requests.exceptions
import time
from time import gmtime, strftime
from urllib.error import URLError
from urllib.parse import urlsplit
import urllib3
import urllib.request
from urllib.request import urlopen

#########################
Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"
cyan = "\033[36m"
pink = "\033[95m"
purple = "\033[35m"
#########################
os.system("clear")
print(banner())

def mainMenu():
    print("" + Reset + "[" + Blue + "1" + Reset + "]-[" + Green + "CHANGING YOUR " + Reset + "[" + Red + "IP " + Green + "MAC " + Red + "Network Mask " + Green + "Broadcast" + Reset + "]" + Green + " ADDRESS" + Red + " WLAN0" + Green + " AND" + Red + " ETH0" + Reset + "]" + Reset)
    print('')
    print("" + Reset + "[" + Blue + "2" + Reset + "]-[" + Red + "Sniffing " + Green + "& " + Green + "Spoofing " + Red + "Tools" + Reset + "]" + Reset) # Sniffing & Spoofing Tools
    print('')
    print("" + Reset + "[" + Blue + "3" + Reset + "]-[" + Green + "Basic Cheatsheet " + Red + "Nmap" + Reset + "]" + Reset)
    print('')
    print("" + Reset + "[" + Blue + "4" + Reset + "]-[" + Red + "Open Sources" + Green + " Tools" + Reset + "]" + Reset)
    print('')
    print("" + Reset + "[" + Blue + "5" + Reset + "]-[" + Red + "Password " + Green + "Tools" + Reset + "]" + Reset)
    print('')
    print("" + Reset + "[" + Blue + "6" + Reset + "]-[" + Red + "WEB " + Green + "HACKING" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Blue + "7" + Reset + "]-[" + Red + "Exploitation " + Green + "Tools" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Blue + "99" + Reset + "]-[" + Red + "EXIT" + Reset + "]" + Reset)
    print('')
    choice = int(input("" + cyan + "[" + Red + "LBFH" + cyan + "]─[" + Blue + "~" + cyan + "]─[" + Green + "menu" + cyan + "]" + Red + ": " + Reset))
    if choice == 1:
        ip_network_mask_broadcast()
        mainMenu()
    elif choice == 2:
        spoofing_tools()
        mainMenu()
    elif choice == 3:
        nmap_cheatsheet()
        mainMenu()
    elif choice == 4:
        open_source()
        mainMenu()
    elif choice == 5:
        password_tools()
        mainMenu()
    elif choice == 6:
        website_information_gathrating()
        mainMenu()
    elif choice == 7:
        exploition_tools()
        mainMenu()
    elif choice == 99:
        exit()
        mainMenu()

def exploition_tools():
    print('')
    print("    " + Reset + "[" + Green + "1" + Reset + "]-[" + Blue + "ATSCAN" + Reset + "]" + Reset)
    print("    ")
    print("    " + Reset + "[" + Green + "2" + Reset + "]-[" + Blue + "sqlmap" + Reset + "]" + Reset)
    print("")
    print("    " + Reset + "[" + Green + "3" + Reset + "]-[" + Blue + "fsociety" + Reset + "]" + Reset)
    print("")
    print("    " + Reset + "[" + Green + "4" + Reset + "]-[" + Blue + "commix" + Reset + "]" + Reset)
    print("")
    print("    " + Reset + "[" + Green + "5" + Reset + "]-[" + Blue + "bettercap" + Reset + "]" + Reset)
    print("")
    print("    " + Reset + "[" + Red + "00" + Reset + "]-[" + Red + "BACK" + Reset + "]" + Reset)
    print("")
    choice = input("" + cyan + "[" + Red + "Exploitation" + cyan + "]─[" + Blue + "~" + cyan + "]─[" + Green + "menu" + cyan + "]" + Red + ": " + Reset)
    if choice == '1':
        try:
            os.system("reset")
            os.system("gnome-terminal -e 'bash -c \"perl ./tools/ATSCAN/atscan.pl; bash\"'")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
        except Exception:
            pass
    elif choice == '5':
        try:
            os.system("reset")
            os.system("gnome-terminal -e 'bash -c \"bettercap -h; bash\"'")
            print(banner())

        except Exception:
            pass
    elif choice == '4':
        try:
            os.system("reset")
            os.system("commix -h")
            print(banner())

        except Exception:
            pass
    elif choice == '3':
        try:
            os.system("reset")
            os.system("python2 ./tools/fsociety/fsociety.py")
            print(banner())

        except Exception:
            pass
    elif choice == '2':
        try:
            os.system("reset")
            os.system("gnome-terminal -e 'bash -c \"sqlmap -h; bash\"'")
            print(banner())

        except Exception:
            pass

#########################################################################################################################
def ip_network_mask_broadcast():
    print('')
    print("" + Reset + "[" + pink + "1" + Reset + "]-[" + Green + "CHANGING YOUR " + Red + "IP " + Green + "ADDRESS" + Red + " WLAN0" + Green + " AND" + Red + " ETH0" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + cyan + "2" + Reset + "]-[" + Green + "SPOOFING YOUR " + Red + "MAC  " + Green + "ADDRESS" + Red + " WLAN0" + Green + " AND" + Red + " ETH0" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Green + "3" + Reset + "]-[" + Green + "Changing Your" + Red + " Network Mask" + Green + " and" + Red + " Broadcast Address" + Green + " WLAN0" + Red + " and" + Green + " ETH0" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Blue + "00" + Reset + "]-[" + Red + "BACK" + Reset + "]" + Reset)
    print("")
    choice = int(input("$ : "))
    if choice == 1:
        ip_wlan0_and_eth0()
        mainMenu()
    elif choice == 2:
        mac_wla0_and_eth0()
        mainMenu()
    elif choice == 3:
        ip_netmask_and_brodcast()
        mainMenu()

def ip_wlan0_and_eth0():
    print('')
    print("" + Reset + "[" + Green + "1" + Reset + "]-[" + Green + "CHANGING YOUR " + Red + "IP " + Green + "ADDRESS" + Red + " WLAN0" + Reset + "]" + Reset)
    print('')
    print("" + Reset + "[" + Green + "2" + Reset + "]-[" + Green + "CHANGING YOUR " + Red + "IP " + Green + "ADDRESS" + Red + " ETH0" + Reset + "]" + Reset )
    print('')
    print("" + Reset + "[" + Green + "00" + Reset + "]-[" + Red + "BACK" + Reset + "]" + Reset)
    print("")
    choice = input("$ : ")
    if choice == '1':
        ip()
        mainMenu()
    elif choice == '2':
        ippc()
        mainMenu()
    elif choice == 00:
        exit()
        mainMenu()
def ip():
    os.system("clear")
    print(ipb())
    ip = input("[\033[1;34mENTER \033[36mIP \033[0m\033[1;34mFOR \033[1;34mCHANGING\033[0m\033[31m WLAN0\033[0m]\033[93m\033[0m:\033[0m ")
    print('')
    subprocess.check_call(['ifconfig', 'wlan0',ip])
    print(suc())
    time.sleep(1)
    os.system("clear")
    print(banner())


def ippc():
    os.system("clear")
    print(ipb())
    ip = input("[\033[1;34mENTER \033[36mIP \033[0m\033[1;34mFOR \033[1;34mCHANGING\033[0m\033[31m ETH0\033[0m]\033[93m\033[0m:\033[0m ")
    subprocess.check_call(['ifconfig', 'eth0',ip])
    print(suc())
    time.sleep(0)
    os.system("clear")
    print(banner())
############################################################################################################################################################################################################
############################################################################################################################################################################################################
def mac_wla0_and_eth0():
    print('')
    print("" + Reset + "[" + Green + "1" + Reset + "]-[" + Green + "SPOOFING YOUR " + Red + "MAC " + Green + "ADDRESS" + Red + " WLAN0" + Reset + "]" + Reset )
    print('')
    print("" + Reset + "[" + Green + "2" + Reset + "]-[" + Green + "SPOOFING YOUR " + Red + "MAC " + Green + "ADDRESS" + Red + " ETH0" + Reset + "]" + Reset )
    print('')
    print("" + Reset + "[" + Green + "00" + Reset + "]-[" + Red + "BACK" + Reset + "]" + Reset)
    print("")
    choice = input("$ : ")
    if choice == '1':
        mac()
        mainMenu()
    elif choice == '2':
        macpc()
        mainMenu()
    elif choice == 00:
        exit()
        mainMenu()
def mac():
    os.system("clear")
    print(macb())
    mac = input("[\033[1;34mENTER \033[31mMAC \033[0m\033[1;34mFOR \033[1;34mCHANGING \033[31mWLAN0\033[0m]\033[93m\033[0m:\033[0m ")
    subprocess.check_call(['ifconfig', 'wlan0', 'down'])
    subprocess.check_call(['ifconfig', 'wlan0', 'hw', 'ether',mac])
    subprocess.check_call(['ifconfig', 'wlan0', 'up'])
    print(suc())
    time.sleep(1)
    os.system("clear")
    print(banner())


def macpc():
    os.system('clear')
    print(macb())
    mac = input("[\033[1;34mENTER \033[31mMAC \033[0m\033[1;34mFOR \033[1;34mCHANGING \033[31mETH0\033[0m]\033[93m\033[0m:\033[0m ")
    subprocess.check_call(['ifconfig', 'eth0', 'down'])
    subprocess.check_call(['ifconfig', 'eth0', 'hw', 'ether',mac])
    subprocess.check_call(['ifconfig', 'eth0', 'up'])
    print(suc())
    time.sleep(1)
    os.system("clear")
    print(banner())
############################################################################################################################################################################################################
############################################################################################################################################################################################################
def ip_netmask_and_brodcast():
    print('')
    print("" + Reset + "[" + Red + "1" + Reset + "]-[" + Green + "Changing Your" + Red + " Network Mask" + Green + " and" + Red + " Broadcast Address" + Green + " WLAN0"+ Reset + "]" + Reset)
    print('')
    print("" + Reset + "[" + Red + "2" + Reset + "]-[" + Green + "Changing Your" + Red + " Network Mask" + Green + " and" + Red + " Broadcast Address" + Green + " ETH0"+ Reset + "]" + Reset)
    print('')
    print("" + Reset + "[" + Red + "00" + Reset + "]-[" + Red + "BACK" + Reset + "]" + Reset)
    print("")
    choice = input("$ : ")
    if choice == '1':
        enb()
        mainMenu()
    elif choice == '2':
        enb2()
        mainMenu()
    elif choice == 00:
        exit()
        mainMenu()
def enb():
    os.system("clear")
    print(eb())
    ip = input("" + Reset + "[" + Blue + "ENTER YOUR SPOOFING" + Red + " IP" + Green + " WLAN0" + Reset + "]" + Green + ": " )
    nm = input("" + Reset + "[" + Blue + "ENTER YOUR SPOOFING" + Red + " NETMASK" + Green + " WLAN0" + Reset + "]" + Green + ": " )
    bdc = input("" + Reset + "[" + Blue + "ENTER YOUR SPOOFING" + Red + " BROADCAST" + Green + " WLAN0" + Reset + "]" + Green + ": " )
    subprocess.check_call(['ifconfig', 'wlan0', ip, 'netmask', nm, 'broadcast', bdc])
    print(suc())
    time.sleep(1)
    os.system("clear")
    print(banner())


def enb2():
    os.system("clear")
    print(eb())
    ip = input("" + Reset + "[" + Blue + "ENTER YOUR SPOOFING" + Red + " IP" + Green + " ETH0" + Reset + "]" + Green + ": " )
    nm = input("" + Reset + "[" + Blue + "ENTER YOUR SPOOFING" + Red + " NETMASK" + Green + " ETH0" + Reset + "]" + Green + ": " )
    bdc = input("" + Reset + "[" + Blue + "ENTER YOUR SPOOFING" + Red + " BROADCAST" + Green + " ETH0" + Reset + "]" + Green + ": " )
    subprocess.check_call(['ifconfig', 'eth0', ip, 'netmask', nm, 'broadcast', bdc])
    print(suc())
    time.sleep(1)
    os.system("clear")
    print(banner())
############################################################################################################################################################################################################
############################################################################################################################################################################################################
def spoofing_tools():
    print("")
    print("" + Reset + "[" + Red + "1" + Reset + "]-[" + Blue + "MAIL" + Green + " SPOOFING" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "00" + Reset + "]-[" + Red + "BACK" + Reset + "]" + Reset)
    print("")
    choice = input("" + cyan + "[" + Red + "Spoofing" + cyan + "]─[" + Blue + "~" + cyan + "]─[" + Green + "menu" + cyan + "]" + Red + ": " + Reset)
    if choice == '1':
        mail()
        mainMenu()

def mail():
    os.system("clear")
    print(mailb())
    f = input("" + Reset +"[" + Blue + "FAKE ADDRESS" + Reset + "]" + Green + " : " + Reset )
    t = input("" + Reset +"[" + Blue + "TARGET ADDRESS" + Reset + "]" + Green + " : " + Reset )
    u = input("" + Reset +"[" + Blue + "YOUR SUBJECT" + Reset + "]" + Green + " : " + Reset )
    m = input("" + Reset +"[" + Blue + "YOUR MESSAGE" + Reset + "]" + Green + " : " + Reset )
    s = input("" + Reset +"[" + Blue + "SERVER" + Green + ":" + Blue + "PORT" + Reset + "]" + Green + " : " + Reset )
    xu = input("" + Reset +"[" + Blue + "USERNAME" + Reset + "]" + Green + " : " + Reset )
    xp = input("" + Reset +"[" + Blue + "PASSWORD" + Reset + "]" + Green + " : " + Reset )
    subprocess.check_call(['sendemail', '-f', f, '-t', t, '-u', u, '-m', m, '-s', s, '-xu', xu, '-xp', xp])
    print(suc())
    time.sleep(1)
    os.system("clear")
    print(banner())
############################################################################################################################################################################################################
############################################################################################################################################################################################################
def nmap_cheatsheet():
    print('')
    print("" + Reset + "[" + Red + "1" + Reset + "]-[" + Blue + "Nmap" + Red + " Target " + Green + "Selection" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "2" + Reset + "]-[" + Blue + "Nmap " + Red + "Port " + Green + "Selection" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "3" + Reset + "]-[" + Blue + "Nmap " + Red + "Port " + Green + "Scan " + Blue + "types" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "4" + Reset + "]-[" + Blue + "Service " + Green + "And " + Red + "OS Detection" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "5" + Reset + "]-[" + Blue + "MOST " + Green + "USEFull " + Red + "Nmap " + Green + "CMD" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "00" + Reset + "]-[" + Red + "BACK" + Reset + "]" + Reset)
    print("")
    choice = input("" + cyan + "[" + Red + "Nmap" + cyan + "]─[" + Blue + "~" + cyan + "]─[" + Green + "menu" + cyan + "]" + Red + ": " + Reset)
    if choice == '1':
        nmap_target_select()
        mainMenu()
    elif choice == '2':
        namp_port_selection()
        mainMenu()
    elif choice == '3':
        nmap_port_scan_types()
        mainMenu()
    elif choice == '4':
        serive_and_os_decation()
        mainMenu()
    elif choice == '5':
        most_usefull_nmap_cmd()
        mainMenu()
    elif choice == 00:
        exit()
        mainMenu()


def most_usefull_nmap_cmd():
    print("")
    print("" + Reset + "[" + cyan + "1" + Reset + "]-[" + Green + "WEBSITE" + Red + " HOST DISCOVERY" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + cyan + "2" + Reset + "]-[" + Green + "WEBSITE" + Red + " OS DISCOVERY" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + cyan + "3" + Reset + "]-[" + Green + "WEBSITE" + Red + " PORT DISCOVERY" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + cyan + "4" + Reset + "]-[" + Green + "WEBSITE" + Red + " PORT RANGE DISCOVERY" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + cyan + "5" + Reset + "]-[" + Red + "PING" + Green + " SCAN THE " + Red + "NETWORK" + Reset + "]-[" + Green + "LISTING " + Red + "MACHINES" + Reset + "]" + Reset)
    print("")
    choice = input("" + cyan + "[" + Red + "nmap-useful" + cyan + "]─[" + Blue + "~" + cyan + "]─[" + Green + "menu" + cyan + "]" + Red + ": " + Reset)
    if choice == '1':
        Host_Discovery()
        mainMenu()
    elif choice == '2':
        Os_Discovery()
        mainMenu()
    elif choice == '3':
        Port_Discovery()
        mainMenu()
    elif choice == '4':
        Port_Discovery_In_Range()
        mainMenu()
    elif choice == '5':
        ping_scan()
        mainMenu()



def Host_Discovery():
    os.system("clear")
    print("")
    print(banner2())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    host = input("" + Reset + "[" + Blue + "ENTER WEBSITE" + Red + " HOST ADDERSS" + Blue + " TO SCAN" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', '-n', '-v', '-Pn', '-sn', '-sL', '-PE', '-PP', '-oN', "Result/" + outname + ".txt", host])
    print(suc())
    time.sleep(1)
    print(banner())

def Os_Discovery():
    os.system("clear")
    print("")
    print(banneros())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    ois = input("" + Reset + "[" + Blue + "ENTER" + Red + " HOST ADDERSS" + Blue + " FOR"+ Red + " OS" + Blue + " SCAN" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap','-n','-F','-A','-Pn','-sS','-O','-oN', "Result/" + outname + ".txt",ois])
    print(suc())
    time.sleep(1)
    print(banner())

def Port_Discovery():
    os.system("clear")
    print("")
    print(port_scan())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    port = input("" + Reset + "[" + Blue + "ENTER " + Red + "HOST " + Blue + "FOR " + Red + "PORT " + Blue + "SCAN" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap','-n','-v','-Pn','-sV','-oN', "Result/" + outname + ".txt",port])
    print(suc())
    time.sleep(1)
    print(banner())

def Port_Discovery_In_Range():
    os.system("clear")
    print("")
    print(port_re())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    port_range = input("" + Reset + "[" + Blue + "ENTER " + Red + "HOST " + Blue + "FOR " + Red + "PORT RANGE SCAN" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap','-P','1-100','-oN', "Result/" + outname + ".txt", port_range])
    print(suc())
    time.sleep(1)
    print(banner())

def ping_scan():
    os.system("clear")
    print(ping())
    ip = input("" + Reset + "[" + Blue + "ENTER IP FOR " + Red + "PING SCAN " + Green + "AND CHACK " + Blue + "ACTIVE" + Red + " HOST" + Reset + "]" + Green + ": " + Reset)
    range = input("" + Reset + "[" + Blue + "ENTER " + Red + "PING SCAN " + Green + "IP " + Blue + "RANGE" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', '-sP', ip + '/' + range])
    print(suc())
    time.sleep(1)
    print(banner())


###############################################################
def serive_and_os_decation():
    print("")
    print("" + Reset + "[" + pink + "1" + Reset + "]-[" + cyan + "Detect" + Red + " OS " + Green + "And" + cyan + " Services" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + pink + "2" + Reset + "]-[" + cyan + "Standard" + Red + " service " + Green + "detection"+ Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + pink + "3" + Reset + "]-[" + Green + "Website And IP" + Red + " OS Discovery" + Reset + "]" + Reset)
    print("")
    choice = input("" + cyan + "[" + Red + "OS" + Green + "-" + Red + "Detection" + cyan + "]─[" + Blue + "~" + cyan + "]─[" + Green + "menu" + cyan + "]" + Red + ": " + Reset)
    if choice == '1':
        os_andservice()
        mainMenu()
    elif choice == '2':
        stander_service_detection()
        mainMenu()
    elif choice == '3':
        osnmap()
        mainMenu()

def os_andservice():
    os.system("clear")
    print("")
    print(osd1())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    osss = input("" + Reset + "[" + Blue + "ENTER " + Red + "IP " + Green + "TO SCAN " + Red + "OS " + Green + "And " + Red + "Services Detect " + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', '-A', osss, '-oN', "Result/" + outname + ".txt"])
    print(suc())
    time.sleep(1)
    print(banner())

def stander_service_detection():
    os.system("clear")
    print("")
    print(osd2())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    ssd = input("" + Reset + "[" + Blue + "ENTER " + Red + "IP " + Green + "TO SCAN " + Red + "OS " + Green + "And " + Red + "Services Detect " + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', '-sV', ssd, '-oN', "Result/" + outname + ".txt"])
    print(suc())
    time.sleep(1)
    print(banner())


def osnmap():
    os.system("clear")
    print("")
    print(banneros())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    ois = input("" + Reset + "[" + Blue + "ENTER" + Red + " HOST ADDERSS" + Blue + " FOR"+ Red + " OS" + Blue + " SCAN" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap','-n','-F','-A','-Pn','-sS','-O','-oN', "Result/" + outname + ".txt",ois])
    print(suc())
    time.sleep(1)
    print(banner())


######################################################################################################
######################################################################################################
def nmap_port_scan_types():
    print("")
    print("" + Reset + "[" + Red + "1" + Reset + "]-[" + Green + "Scan" + Blue + " Using " + Red + "TCP" + cyan + " Connect" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "2" + Reset + "]-[" + Green + "Scan " + Blue + "using  " + Red + "TCP SYN " + cyan + "scan " + Green + "(default)" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "3" + Reset + "]-[" + Green + "Scan " + Blue + "UDP " + Red + "PORTs " + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "4" + Reset + "]-[" + Green + "Scan " + Blue + "Selected " + Red + "- " + cyan + "Ignore Discovery " + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "00" + Reset + "]-[" + Red + "BACK" + Reset + "]" + Reset)
    print("")
    choice = input("" + cyan + "[" + Red + "PORT" + Green + "-" + Red + "SCAN" + cyan + "]─[" + Blue + "~" + cyan + "]─[" + Green + "menu" + cyan + "]" + Red + ": " + Reset)
    if choice == '1':
        scan_using_tcp_connection()
        mainMenu()
    elif choice == '2':
        scan_using_tcp_syn_defualt()
        mainMenu()
    elif choice == '3':
        scan_using_udp()
        mainMenu()
    elif choice == '4':
        scan_ignor_discover()
        mainMenu()
    elif choice == 00:
        exit()
        mainMenu()



def scan_using_tcp_connection():
    os.system("clear")
    print("")
    print(tcps())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    tcp = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "IP " + Green + "TO SCAN " + Red + "TCP CONNECT" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', '-sT', tcp, '-oN', "Result/" + outname + ".txt"])
    print(suc())
    time.sleep(1)
    print(banner())


def scan_using_tcp_syn_defualt():
    os.system("clear")
    print("")
    print(tcpsyns())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    tcpsyn = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "IP " + Green + "TO SCAN " + Red + "TCP SYN" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', '-sS', tcpsyn, '-oN', "Result/" + outname + ".txt"])
    print(suc())
    print(banner())

def scan_using_udp():
    os.system("clear")
    print("")
    print(uuddpp())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    udpss = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "IP " + Green + "TO SCAN " + Red + "UDP PORTs" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', '-sU', '-p', '123,161,162', udpss, '-oN', "Result/" + outname + ".txt"])
    print(suc())
    time.sleep(1)
    print(banner())

def scan_ignor_discover():
    os.system("clear")
    print("")
    print(igonrrr())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    idis = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "IP " + Green + "TO SCAN " + Red + "Ignore Discovery" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', '-Pn', '-F', idis, '-oN', "Result/" + outname + ".txt"])
    print(suc())
    time.sleep(1)
    print(banner())



##########################################################################################################
##########################################################################################################
def namp_port_selection():
    print("")
    print("" + Reset + "[" + pink + "1" + Reset + "]-[" + Green + "Scan" + Blue + " single " + Red + "PORT" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + pink + "2" + Reset + "]-[" + Green + "Scan" + Blue + " 100 " + Green + "Most Common " + Red + "PORT " + Blue + "(Fast)" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + pink + "3" + Reset + "]-[" + Green + "Scan" + Blue + " All " + Green + "(" + Red + "65535" + Green + ") " + Red + "PORTs" + Reset + "]" + Reset)
    print("")
    choice = input("" + cyan + "[" + Red + "PORT" + Green + "-" + Red + "SELECTION" + cyan + "]─[" + Blue + "~" + cyan + "]─[" + Green + "menu" + cyan + "]" + Red + ": " + Reset) # ___menu___choice
    if choice == '1':
        single_scan_a_port()
        mainMenu()
    elif choice == '2':
        scan_a_range_of_ports()
        mainMenu()
    elif choice == '3':
        scan_alll_portss()
        mainMenu()


def single_scan_a_port():
    os.system("clear")
    print("")
    print(single_port())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    ports = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "IP " + Green + "TO SCAN " + Red + "PORT" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', '-P', '22', ports, '-oN', "Result/" + outname + ".txt"])
    print(suc())
    time.sleep(1)
    print(banner())

def scan_a_range_of_ports():
    os.system("clear")
    print("")
    print(range_of_port())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    iprn = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "IP " + Green + "TO SCAN " + Red + "PORT" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', '-F', iprn, '-oN', "Result/" + outname + ".txt"])
    print(suc())
    print(banner())


def scan_alll_portss():
    os.system("clear")
    print("")
    print(all_ports())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    ipp = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "IP " + Green + "TO SCAN " + Red + "PORT" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', '-p-', ipp, '-oN', "Result/" + outname + ".txt"])
    print(suc())
    time.sleep(1)
    print(banner())


##########################################################
##########################################################

def nmap_target_select():
    print("")
    print("" + Reset + "[" + cyan + "1" + Reset + "]-[" + Green + "Scan" + Blue + " a single " + Red + "IP" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + cyan + "2" + Reset + "]-[" + Green + "Scan" + Blue + " a " + Red + "host" + Green + " Or" + Red + " Website" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + cyan + "3" + Reset + "]-[" + Green + "Scan" + Blue + " a " + Red + "Range" + Green + " Of" + Red + " IPs" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + cyan + "4" + Reset + "]-[" + Green + "Scan" + Blue + " a " + Red + "subnet" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + cyan + "5" + Reset + "]-[" + Green + "Scan" + Red + " IP " + Blue + "List" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + cyan + "00" + Reset + "]-[" + Red + "BACK" + Reset + "]" + Reset)
    print("")
    choice = input("" + cyan + "[" + Red + "nmap " + Green + "TARGET " + Red + "SELECTION" + cyan + "]─[" + Blue + "~" + cyan + "]─[" + Green + "menu" + cyan + "]" + Red + ": " + Reset) # ___menu___choice
    if choice == '1':
        scan_a_single_ip()
        mainMenu()
    elif choice == '2':
        scan_a_host()
        mainMenu()
    elif choice == '3':
        sacn_a_range_ips()
        mainMenu()
    elif choice == '4':
        Scan_a_subnet()
        mainMenu()
    elif choice == '5':
        scan_id_terget_list()
        mainMenu()
    elif choice == 00:
        exit()
        mainMenu()

def scan_a_single_ip():
    os.system("clear")
    print("")
    print(single_IP())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    scanip = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "IP " + Green + "TO SCAN" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', scanip, '-oN', "Result/" + outname + ".txt"])
    print(suc())
    time.sleep(1)
    print(banner())

def scan_a_host():
    os.system("clear")
    print("")
    print(banner2())
    print("" + Green + "Example " + Blue + ":" + Reset + " [" + Blue + "( " + Red + "WWW.Example.com" + Blue + " )" + Red + " Like This Not https or http" + Reset + "]" + Reset)
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    website = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "Website " + Green + "Or " + Red + "IP" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', website, '-oN', "Result/" + outname + ".txt"])
    print(suc())
    time.sleep(1)
    print(banner())

def sacn_a_range_ips():
    os.system("clear")
    print("")
    print(s_a_ip_r())
    print("" + Green + "Example " + Blue + ":" + Reset + " [" + Blue + "( " + Red + "Thst Is IP :" + cyan + " 192.168.1.1 " + Green + "And " + Red +"Range : " + cyan + "20 or 40 or 80 or 1000" + Red + " Your Choice" + Blue + " )" + Reset + "]" + Reset)
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    ips = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "IP" + Reset + "]" + Green + ": " + Reset)
    range = input("" + Reset + "[" + Blue + "ENTER " + Red + "RANGE" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', ips + '-' + range, "-oN", "Result/" + outname + ".txt"])
    print(suc())
    time.sleep(1)
    print(banner())

def Scan_a_subnet():
    os.system("clear")
    print("")
    print(s_a_ip_r())
    print("" + Green + "Example " + Blue + ":" + Reset + " [" + Blue + "( " + Red + "Thst Is IP :" + cyan + " 192.168.10.238 " + Green + "And " + Red + "Range : " + cyan + "24" + Blue + " )" + Reset + "]" + Reset)
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    ip = input("" + Reset + "[" + Blue + "ENTER " + Green + "TARGET " + Red + "IP " + Reset + "]" + Green + ": " + Reset)
    range = input("" + Reset + "[" + Blue + "ENTER " + Red + "RANGE" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "FILE " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', ip + '/' + range,'-oN', "Result/" + outname + ".txt"])
    print(suc())
    time.sleep(1)
    print(banner())

def scan_id_terget_list():
    os.system("clear")
    print("")
    print(ip_lists())
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
    print("")
    ippath = input("" + Reset + "[" + Blue + "ENTER " + Green + "Your " + Red + "IP LIST " + Blue + "PATH" + Reset + "]" + Green + ": " + Reset)
    outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['nmap', '-iL', ippath, '-oN', "Result/" + outname + ".txt"])
    print(suc())
    time.sleep(1)
    print(banner())

############################################################################################################################################################################################################
############################################################################################################################################################################################################
def open_source():
    print("")
    print("" + Reset + "[" + Green + "1" + Reset + "]-[" + Red + "WEBSITE FIND WITH" + Blue + " KEYWORD" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Green + "2" + Reset + "]-[" + Green + "SINGLE " + Red + "MAIL" + Blue + " SCAN " + Green + "SOCIAL MEDIA" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Green + "3" + Reset + "]-[" + Green + "MULTIPLE " + Red + "MAIL" + Blue + " SCAN " + Green + "SOCIAL MEDIA" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Green + "4" + Reset + "]-[" + Red + "NICK NAME " + Green + "TO " + Red + "MAIL" + Blue + " FOUND" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Green + "5" + Reset + "]-[" + Green + "MULTIPLE " + Red + "NICK NAME" + Blue + " TO " + Green + "MAIL FOUND" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Green + "6" + Reset + "]-[" + Green + "SINGLE " + Red + "PHONE NUMBER" + Blue + " FOUND"+ Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Green + "7" + Reset + "]-[" + Green + "FIND " + Red + "ACCOUNT BY" + Blue + " TARGET " + Green + "NAME" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Green + "00" + Reset + "]-[" + Red + "BACK" + Reset + "]" + Reset)
    print("")
    choice = input("" + cyan + "[" + Red + "OPEN" + Green + "-" + Red + "SOURCE" + cyan + "]─[" + Blue + "~" + cyan + "]─[" + Green + "menu" + cyan + "]" + Red + ": " + Reset) # ___menu___choice
    if choice == '1':
        website_keyword()
        mainMenu()
    elif choice == '2':
        mail_scan_socialmedia()
        mainMenu()
    elif choice == '3':
        multiple_scan_socialmedia()
        mainMenu()
    elif choice == '4':
        nick_name_mail_found()
        mainMenu()
    elif choice == '5':
        multiple_nick_name_mail()
        mainMenu()
    elif choice == '6':
        phone_number_found()
        mainMenu()
    elif choice == '7':
        find_account_name()
        mainMenu()
    elif choice == 00:
        exit()
        mainMenu()


def website_keyword():
    print("")
    print(keys())
    keyword = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "KEYWORD " + Green + "FIND WEBSITE" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['domainfy','--whois','-n',keyword])
    print(suc())
    print(banner())

def mail_scan_socialmedia():
    print("")
    print(mail_sacn())
    targetmail = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "SINGLE TARGET " + Green + "MAIL" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['mailfy','-m',targetmail,'-p','all'])
    print(suc())
    time.sleep(1)
    print(banner())

def multiple_scan_socialmedia():
    print("")
    print(multipal_mail_scan())
    pathmail = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "MULTIPLE " + Green + "MAIL PATH" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['mailfy','--emails-file',pathmail])
    print(suc())
    time.sleep(1)
    print(banner())


def nick_name_mail_found():
    print("")
    print(nick_name_to_mail())
    nick = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "SINGLE " + Green + "NICK NAME" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['mailfy','--nicks',nick,'-p','all'])
    print(suc())
    print(banner())


def multiple_nick_name_mail():
    print("")
    print(multiple_nick_name())
    mnick = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "NICK NAME " + Green + "PATH" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['mailfy','-N',mnick])
    print(suc())
    time.sleep(1)
    print(banner())


def phone_number_found():
    print("")
    print(phone_number_founds())
    nm = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "PHONE " + Green + "NUMBER" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['phonefy','--numbers',nm])
    print(suc())
    print(banner())

def find_account_name():
    print("")
    print(find_account_by_name())
    name = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "NAME " + Green + "FIND " + Red + "ACCOUNT" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['searchfy','-q',name])
    print(suc())
    time.sleep(1)
    print(banner())
############################################################################################################################################################################################################
############################################################################################################################################################################################################
def password_tools():
    print("")
    print("" + Reset + "[" + Blue + "1" + Reset + "]-[" + pink + "HASH " + Green + "IDENTIFIER" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Blue + "2" + Reset + "]-[" + pink + "Download " + Green + "Rockyou.txt" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Blue + "00" + Reset + "]-[" + Red + "BACK" + Reset + "]" + Reset)
    print("")
    choice = input("" + cyan + "[" + Red + "PASSWOARD" + Green + "-" + Red + "TOOLS" + cyan + "]─[" + Blue + "~" + cyan + "]─[" + Green + "menu" + cyan + "]" + Red + ": " + Reset) # ___menu___choice
    if choice == '1':
        hash_tools()
        mainMenu()
    elif choice == '2':
        rockyou_txt()
        mainMenu()
    elif choice == 00:
        exit()
        mainMenu()

def rockyou_txt():
    print("")
    print("\033[91m     Downloading ...    \033[0m")
    print("")
    path = input("" + Reset + "[" + Blue + "Enter Path " + Red + "Save " + Green + "This File" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['wget', '-O', path + 'rockyou.txt.gz', 'https://gitlab.com/kalilinux/packages/wordlists/raw/kali/master/rockyou.txt.gz'])
def hash_tools():
    print(hashbanner())
    hash = input("" + Reset + "[" + Blue + "ENTER YOUR " + Red + "HASH" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['hash-identifier',hash])
    print(suc())
    time.sleep(1)
    print(banner())
############################################################################################################################################################################################################
def website_information_gathrating():
    print("")
    print("" + pink + "-[" + Red + "!" + pink + "]" + Green + "-----" + Blue + " Auto " + Green + "------"+ pink + "-[" + Red + "!" + pink + "]-" + Reset)
    print("")
    print("" + Reset + "[" + Red + "1" + Reset + "]-[" + Green + "Scan " + Blue + "Website" + Red + " TraceRoute" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "2" + Reset + "]-[" + Red + "WhatWeb " + pink + "Lookup" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "3" + Reset + "]-[" + Red + "Whois " + pink + "Lookup" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "4" + Reset + "]-[" + Green + "Website " + Blue + "Copier On" + Red + " Offline Browser" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "5" + Reset + "]-[" + Green + "Scan " + Blue + "Website With" + Red + " J00MScan" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "6" + Reset + "]-[" + Red + "Robots.txt " + Blue + "Scanner" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "7" + Reset + "]-[" + Red + "DNS " + pink + "Lookup" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "8" + Reset + "]-[" + Green + "EtherApe = " + Blue + "Graphical Network Monitor" + Red + " (root)" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "9" + Reset + "]-[" + Green + "Clickjacking Test " + Blue + "X-Frame-Options " + Red + "Header" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "10" + Reset + "]-[" + Red + "Link " + Blue + "Grabber" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "11" + Reset + "]-[" + Green + "IP " + Blue + "Location " + Red + "Finder" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "12" + Reset + "]-[" + Green + "Website " + Blue + "Scan On" + Red + " Blue Eye" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "13" + Reset + "]-[" + Green + "Shodan " + pink + "Lookup" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "14" + Reset + "]-[" + Green + "Website " + Blue + "Scan On" + Red + " CMSeeK" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "15" + Reset + "]-[" + Green + "Website " + Blue + "XSS " + purple + "ToolKit" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "16" + Reset + "]-[" + Green + "Website " + Blue + "Deep Information Gathering Using" + Red + " netcraft" + Green + " & " + Red + "Dmitry" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "17" + Reset + "]-[" + Green + "Website " + Blue + "Scan On " + purple + "RED_HAWK" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "18" + Reset + "]-[" + Green + "Website " + Blue + "Test " + Red + "FinalRecon" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "19" + Reset + "]-[" + Red + "Admin " + Blue + "Scan " + Green + "website" + Reset + "]" + Reset)
    print("")
    print("" + pink + "-[" + Red + "!" + pink + "]" + Green + "-----" + Blue + " Manual " + Green + "------"+ pink + "-[" + Red + "!" + pink + "]-" + Reset)
    print("")
    print("" + Reset + "[" + Red + "20" + Reset + "]-[" + Green + "droopescan" + Reset + "]" + Reset)
    print("")
    print("" + Reset + "[" + Red + "00" + Reset + "]-[" + Red + "BACK" + Reset + "]" + Reset)
    print("")
    choice = input("" + cyan + "[" + Red + "WEB" + Green + "-" + Red + "HACKING" + cyan + "]─[" + Blue + "~" + cyan + "]─[" + Green + "menu" + cyan + "]" + Red + ": " + Reset) # ___menu___choice
    if choice == '1':
        TraceRoute()
        mainMenu()
    elif choice == '2':
        what_website()
        mainMenu()
    elif choice == '3':
        whois()
        mainMenu()
    elif choice == '4':
        httpoffline()
        mainMenu()
    elif choice == '5':
        joomscans()
        mainMenu()
    elif choice == '15':
        xss_tool_Kit()
        mainMenu()
    elif choice == '19':
        try:
            os.system("reset")
            os.system("python3 ./tools/admin-san/admin-san.py")
            print(banner())

        except Exception:
            pass
####################################################################################################################
    elif choice == '20':
        try:
            os.system("reset")
            os.system("gnome-terminal -e 'bash -c \"droopescan scan --help; bash\"'")

        except Exception:
            pass
#####################################################################################################################
    elif choice == '18':
        try:
            os.system("reset")
            os.system("python3 ./tools/finalrecoon.py")
            print(banner())

        except Exception:
            pass
#######################################################################################################################
    elif choice == '17':
        try:
            os.system("reset")
            os.system("php ./tools/RED_HAWK/rhawk.php")

        except Exception:
            pass
############################################################################################################################################################
    elif choice == '16':
        try:
            os.system('clear')
            print(
"""\033[36m                                   __                  ______ 
\033[36m                       ____  ___  / /_______________ _/ __/ /_\033[0m
\033[36m                      / __ \/ _ \/ __/ ___/ ___/ __ `/ /_/ __/\033[0m
\033[36m                     / / / /  __/ /_/ /__/ /  / /_/ / __/ /_  \033[0m
\033[36m                    /_/ /_/\___/\__/\___/_/   \__,_/_/  \__/  \033[0m
    """ )
            print("")
            print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + Blue + " This Directory" + Red + " Result " + Blue + "Folder" + Reset + " ]" + Reset)
            print("")
            ntfc = input("" + Reset + "[" + Blue + "ENTER " + Red + "Domain " + Green + "or " + Red + "IP Address" + Reset + "]" + Green + ": " + Reset).lower()
            outname = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "NAME" + Reset + "]" + Green + ": " + Reset)
            subprocess.check_call(['dmitry', 'wish', '-i', '-w', '-n', '-s', '-e', '-o', "Result/" + outname + ".txt", ntfc])
        except Exception:
            pass
################################################################################################################
    elif choice == '14':
        try:
            os.system("reset")
            os.system("python3 ./tools/CMSeeK/cmseek.py")

        except Exception:
            pass
##################################################################################################################
    elif choice == '13':
        try:
            os.system("reset")
            os.system("python3 ./tools/shodan_eye.py")

        except Exception:
            pass
###################################################################################################################
    elif choice == '12':
        try:
            os.system("reset")
            os.system("python3 ./tools/blue_eye.py")

        except Exception:
            pass
#####################################################################################################################
    elif choice == '11':
        try:
            os.system("clear")
            print(
                """
\033[36m             _______    \033[1;33m__                 __  _             \033[36m_____         __       \033[0m
\033[36m            /  _/ _ \  \033[1;33m/ /  ___  _______ _/ /_(_)__  ___    \033[36m/ __(_)__  ___/ /__ ____\033[0m
\033[36m           _/ // ___/ \033[1;33m/ /__/ _ \/ __/ _ `/ __/ / _ \/ _ \  \033[36m/ _// / _ \/ _  / -_) __/\033[0m
\033[36m          /___/_/    \033[1;33m/____/\___/\__/\_,_/\__/_/\___/_//_/ \033[36m/_/ /_/_//_/\_,_/\__/_/   \033[0m
""")
            print("")
            target = input("" + Reset + "[" + Blue + "ENTER " + Red + "Domain " + Green + "or " + Red + "IP Address" + Reset + "]" + Green + ": " + Reset).lower()
            url = ("http://ip-api.com/json/")
            response = urllib.request.urlopen(url + target)
            data = response.read()
            jso = json.loads(data)
            os.system("reset")
            print("\033[34mSearching.... IP Location Finder: \033[0m".format(url) + target)
            time.sleep(1.5)

            print("\n [+] \033[34mUrl: " + target + "\033[0m")
            print(" [+] " + "\033[34m" + "IP: " + jso["query"] + "\033[0m")
            print(" [+] " + "\033[34m" + "Status: " + jso["status"] + "\033[0m")
            print(" [+] " + "\033[34m" + "Region: " + jso["regionName"] + "\033[0m")
            print(" [+] " + "\033[34m" + "Country: " + jso["country"] + "\033[0m")
            print(" [+] " + "\033[34m" + "City: " + jso["city"] + "\033[0m")
            print(" [+] " + "\033[34m" + "ISP: " + jso["isp"] + "\033[0m")
            print(" [+] " + "\033[34m" + "Lat & Lon: " + str(jso['lat']) + " & " + str(jso['lon']) + "\033[0m")
            print(" [+] " + "\033[34m" + "Zipcode: " + jso["zip"] + "\033[0m")
            print(" [+] " + "\033[34m" + "TimeZone: " + jso["timezone"] + "\033[0m")
            print(" [+] " + "\033[34m" + "AS: " + jso["as"] + "\033[0m" + "\n")

        except URLError:
            print("\033[1;31m[-] Please provide a valid IP address!\033[1;m")
            print(suc())
            time.sleep(1)
            print(banner())
#######################################################################################################################
    elif choice == '10':
        try:
            os.system("clear")
            print(
"""\033[36m                       __    _       __      ______           __    __             
\033[36m                      / /   (_)___  / /__   \033[1;33m/ ____/________ _/ /_  / /_  ___  _____\033[0m
\033[36m                     / /   / / __ \/ //_/  \033[1;33m/ / __/ ___/ __ `/ __ \/ __ \/ _ \/ ___/\033[0m
\033[36m                    / /___/ / / / / ,<    \033[1;33m/ /_/ / /  / /_/ / /_/ / /_/ /  __/ /    \033[0m
 \033[36m                  /_____/_/_/ /_/_/|_|   \033[1;33m\____/_/   \__,_/_.___/_.___/\___/_/     \033[0m
 """
)
            print("")
            target = input("" + Reset + "[" + Blue + "ENTER " + Red + "Domain " + Reset + "]" + Green + ": " + Reset).lower()
            os.system("reset")
            print("\033[34mScanning.... Link Grabber: \033[0m\n" + target)
            time.sleep(2)
            if not (target.startswith("http://") or target.startswith("https://")):
                target = "http://" + target
            deq = deque([target])
            pro = set()

            try:
                while len(deq):
                    url = deq.popleft()
                    pro.add(url)
                    parts = urlsplit(url)
                    base = "{0.scheme}://{0.netloc}".format(parts)

                    print("[+] Crawling URL " + "\033[34m" + url + "\033[0m")
                    try:
                        response = requests.get(url)
                    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                        continue

                    soup = BeautifulSoup(response.text, "lxml")
                    for anchor in soup.find_all("a"):
                        link = anchor.attrs["href"] if "href" in anchor.attrs else ''
                        if link.startswith("/"):
                            link = base + link
                        if not link in deq and not link in pro:
                            deq.append(link)
                        continue

            except KeyboardInterrupt:
                print("\n")
                print("[-] User Interruption Detected..!")
                time.sleep(1)
                print("\n \t\033[34m[!] I like to See Ya, Hacking Anywhere ..!\033[0m\n")
                print(suc())
                time.sleep(1)
                print(banner())

        except Exception:
            pass
#######################################################################################################################
    elif choice == '9':
        os.system("clear")
        print("""
              \033[36m                         /$$       /$$     \033[0m               
              \033[36m                        | $$      |__/         \033[0m           
               \033[36m/$$  /$$$$$$   /$$$$$$$| $$   /$$ /$$ /$$$$$$$   /$$$$$$ \033[0m
              \033[36m|__/ |____  $$ /$$_____/| $$  /$$/| $$| $$__  $$ /$$__  $$\033[0m
               \033[36m/$$  /$$$$$$$| $$      | $$$$$$/ | $$| $$  \ $$| $$  \ $$\033[0m
              \033[36m| $$ /$$__  $$| $$      | $$_  $$ | $$| $$  | $$| $$  | $$\033[0m
              \033[36m| $$|  $$$$$$$|  $$$$$$$| $$ \  $$| $$| $$  | $$|  $$$$$$$\033[0m
              \033[36m| $$ \_______/ \_______/|__/  \__/|__/|__/  |__/ \____  $$\033[0m
         \033[36m/$$  | $$                                             /$$  \ $$\033[0m
        \033[36m|  $$$$$$/                                            |  $$$$$$/\033[0m
         \033[36m\______/                                              \______/ \033[0m
        """)
        print("")
        target = input("" + Reset + "[" + Blue + "ENTER " + Red + "The " + Green + "Domain " + Red + "To Test" + Reset + "]" + Green + ": " + Reset).lower()
        os.system("reset")

        if not (target.startswith("http://") or target.startswith("https://")):
            target = "http://" + target
        print("\033[1;34mTesting...  Clickjacking Test: \033[1;m" + target)
        time.sleep(2)
        try:
            resp = requests.get(target)
            headers = resp.headers
            print("\nHeader set are: \n")
            for item, xfr in headers.items():
                print("\033[1;34m" + item + ":" + xfr + "\033[1;m")

            if "X-Frame-Options" in headers.keys():
                print("\n[+] \033[1;34mClick Jacking Header is present\033[1;m")
                print("[+] \033[1;34mYou can't clickjack this site !\033[1;m\n")
            else:
                print("\n[*] \033[1;34mX-Frame-Options-Header is missing ! \033[1;m")
                print("[!] \033[1;34mClickjacking is possible,this site is vulnerable to Clickjacking\033[1;m\n")

        except Exception as ex:
            print("\033[1;34mException caught: " + str(ex))
            print(suc())
            time.sleep(1)
            print(banner())
##########################################################################################################################
    elif choice == '8':
        try:
            os.system("reset")
            os.system("sudo etherape")

        except Exception:
            pass
############################################################################################################################
    elif choice == '7':
        try:
            os.system("clear")
            print(dns())
            print("")
            target = input("" + Reset + "[" + Blue + "ENTER " + Red + "Domain " + Green + "or " + Red + "IP Address" + Reset + "]" + Green + ": " + Reset).lower()
            os.system("reset")
            print("\033[34mSearching for... DNS Lookup: \033[0m".format(target) + target)
            time.sleep(1.5)
            command = ("dig " + target + " +trace ANY")
            proces = os.popen(command)
            results = str(proces.read())
            print("\033[1;34m" + results + command + "\033[1;m")
            print(suc())
            time.sleep(1)
            print(banner())

        except Exception:
            pass
    ##########################################################################################################################
    elif choice == '6':
            try:
                os.system("clear")
                print(rb())
                print("")
                target = input("" + Reset + "[" + Blue + "ENTER " + Red + "Domain " + Reset + "]" + Green + ": " + Reset)
                os.system("reset")
                print("\033[34mScanning.... Robots.txt Scanner: \033[0m\n" + target)
                time.sleep(1.5)

                if not (target.startswith("http://") or target.startswith("https://")):
                    target = "http://" + target
                robot = target + "/robots.txt"

                try:
                    bots = urlopen(robot).read().decode("utf-8")
                    print("\033[34m" + (bots) + "\033[1;m")
                except URLError:
                    print("\033[1;31m[-] Can\'t access to {page}!\033[1;m".format(page=robot))

            except Exception as ex:
                print("\033[1;34mException caught: " + str(ex))
    print(suc())
    time.sleep(1)
    print(banner())
###################################################################################################################
def xss_tool_Kit():
    print("")
    print("      " + Reset + "[" + Green + "1" + Reset + "]-[" + pink + "XSS " + Green + "Test With " + Blue + "XSStrike" + Reset + "]" + Reset)
    print("")
    print("      " + Reset + "[" + Green + "2" + Reset + "]-[" + pink + "XSS " + Green + "Attack With " + Red + "XSpear" + Reset + "]" + Reset)
    print("")
    print("      " + Reset + "[" + Green + "3" + Reset + "]-[" + pink + "BruteXSS" + Reset + "]" + Reset)
    print("")
    print("      " + Reset + "[" + Red + "00" + Reset + "]-[" + Red + "BACK" + Reset + "]" + Reset)
    print("")
    choice = input("" + cyan + "[" + Red + "XSS" + Green + "-" + Red + "TESTING" + cyan + "]─[" + Blue + "~" + cyan + "]─[" + Green + "menu" + cyan + "]" + Red + ": " + Reset) # ___menu___choice
    if choice == '1':
        try:
            os.system("reset")
            os.system("python3 ./tools/XSStrike/xsstrike2.py")
            print(suc())
            time.sleep(1)
            print(banner())

        except Exception:
            pass
####################################################################################################################
    elif choice == '3':
        try:
            os.system("reset")
            os.system("gnome-terminal -e 'bash -c \"python2 ./tools/BruteXSS/brutexss.py; bash\"'")
            print(banner())
        except Exception:
            pass
#####################################################################################################################
    elif choice == '2':
        try:
            os.system("clear")
            print(
"""                     \033[36m/$$   /$$  \033[1;33m/$$$$$$                                         \033[0m
                    \033[36m| $$  / $$ \033[1;33m/$$__  $$                                        \033[0m
                    \033[36m|  $$/ $$/\033[1;33m| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ \033[0m
                     \033[36m\  $$$$/ \033[1;33m|  $$$$$$  /$$__  $$ /$$__  $$ |____  $$ /$$__  $$\033[0m
                      \033[36m>$$  $$  \033[1;33m\____  $$| $$  \ $$| $$$$$$$$  /$$$$$$$| $$  \__/\033[0m
                     \033[36m/$$/\  $$ \033[1;33m/$$  \ $$| $$  | $$| $$_____/ /$$__  $$| $$      \033[0m
                    \033[36m| $$  \ $$\033[1;33m|  $$$$$$/| $$$$$$$/|  $$$$$$$|  $$$$$$$| $$      \033[0m
                    \033[36m|__/  |__/ \033[1;33m\______/ | $$____/  \_______/ \_______/|__/      \033[0m
                                        \033[1;33m| $$                                    \033[0m
                                        \033[1;33m| $$                                    \033[0m
                                        \033[1;33m|__/\033[0m"""
)
            print("" + Red + "Example : " + Green + "[" + Blue + "'https://www.hahwul.com/?q=123' --cookie='role=admin' -v 1 -a" + Green + "]" + Reset)
            print("")
            print("" + Red + "Example : " + Green + "[" + Blue + "'http://testphp.vulnweb.com/listproducts.php?cat=123' -v 2" + Green + "]" + Reset)
            print("")
            print("" + Red + "Example : " + Green + "[" + Blue + "'http://testphp.vulnweb.com/listproducts.php?cat=123' -v 0 -o json" + Green + "]" + Reset)
            print("")
            xssweboi = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "WEBSITE " + Reset + "]" + Green + ": " + Reset)
            print("")
            subprocess.check_call(['XSpear', '-u', xssweboi])
            print(suc())
            time.sleep(1)
            print(banner())

        except Exception:
            pass
##################################################################################################################
def TraceRoute():
    os.system("clear")
    print("")
    print(wss())
    webb = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "WEBSITE " + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['traceroute',webb])
    print(suc())
    time.sleep(1)
    print(banner())

def what_website():
    os.system("clear")
    print("")
    print(wss1())
    print("")
    wsfs = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "WEBSITE " + Reset + "]" + Green + ": " + Reset)
    wsfs1 = input("" + Reset + "[" + Blue + "ENTER TARGET " + Red + "WEBSITE " + Green + "Again" + cyan + " Please" + Reset + "]" + Green + ": " + Reset)
    path = input("" + Reset + "[" + Blue + "ENTER " + Green + "RESULT " + Red + "SAVE " + Blue + "PATH" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['whatweb',wsfs])
    subprocess.check_call(['whatweb','-v', wsfs1, "--log-xml=" + path + wsfs1])
    print(suc())
    time.sleep(1)
    print(banner())

def whois():
    os.system("clear")
    print("")
    print(wss8())
    print("")
    whoisss = input("" + Reset + "[" + Blue + "ENTER " + Green + "TARGET " + Red + "WEBSITE " + Green + "To " + Red + "Whois" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['whois',whoisss])
    print(suc())
    time.sleep(1)
    print(banner())

def httpoffline():
    os.system("clear")
    print("")
    print(httppss())
    print("")
    htpoff = input("" + Reset + "[" + Blue + "ENTER " + Green + "TARGET " + Red + "WEBSITE To Copier" + Green + " Offline" + Reset + "]" + Green + ": " + Reset)
    svpath = input("" + Reset + "[" + Blue + "ENTER " + Green + "File " + Red + "Saveing " + Blue + "PATH" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['httrack', htpoff, '-O', svpath])
    print(suc())
    time.sleep(1)
    print(banner())

def joomscans():
    os.system("clear")
    print("")
    print(jom())
    print("")
    print("" + Green + "NOTE " + cyan + ':' + Reset + " [" + Blue + " This Scan Result Save" + Green + " in" + pink + " /usr/share/joomscan/reports/" + Red + " This Directory" + Reset + " ]" + Reset)
    print("")
    weh = input("" + Reset + "[" + Blue + "ENTER " + Green + "TARGET " + Red + "WEBSITE " + Green + " URL" + pink + " TO SCAN" + Reset + "]" + Green + ": " + Reset)
    subprocess.check_call(['joomscan', '-u', weh])
    print(suc())
    time.sleep(1)
    print(banner())
############################################################################################################################################################################################################
############################################################################################################################################################################################################
def exit():

    sys.exit()


if __name__== "__main__":
    mainMenu()
############################################################################################################################################################################################################

# /usr/share/joomscan/reports/
