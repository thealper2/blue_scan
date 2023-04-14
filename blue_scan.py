import colorama
from bluetooth import *
from colorama import Fore, Back, Style
import argparse

colorama.init(autoreset=True)

def bt_scan(scan=True, target=None):
	found = []
	devices = discover_devices(lookup_names=True)
	for addr, name in devices:
		if addr not in found:
			if scan == True:
				print(f"[+] Found: {str(name)}:{str(addr)}")
			found.append()

		if target != None:
			if name == target:
				print(f"[+] Target: {str(target)}:{str(addr)}")

parser = argparse.ArgumentParser(description='BT Scan')
parser.add_argument('--scan', required=False, action='store_true', help='Scan devices.')
parser.add_argument('--target', required=False, type=str, help='Find Target device.')
args = parser.parse_args()

if args.scan:
	bt_scan(scan=True, target=args.target)

else:
	bt_scan(scan=False, target=args.target)
