#!/usr/bin/python3

import os
import sys
from colorama import *
import platform
import nmap

##################################################################
##################################################################

nm = nmap.PortScanner()
puertos_abiertos="-p "
count=0
red = Fore.RED
cyan = Fore.CYAN
azul = Fore.BLUE
yellow = Fore.YELLOW
verde = Fore.GREEN
white = Fore.WHITE
magenta = Fore.MAGENTA
host = ""
dev = "Frxst"
github = "https://github.com/DevFrxst"
banner = f'''
{cyan}
88  dP .dP"Y8  dP""b8    db    88b 88 88b 88 888888 88""Yb 
88odP  `Ybo." dP   `"   dPYb   88Yb88 88Yb88 88__   88__dP 
88"Yb  o.`Y8b Yb       dP__Yb  88 Y88 88 Y88 88""   88"Yb  
88  Yb 8bodP'  YboodP dP""""Yb 88  Y8 88  Y8 888888 88  Yb 
'''
info = f'''
{white}[+] {cyan}Informacion:
 {white}[-] {cyan}Developer: {magenta}{dev}
 {white}[-] {cyan}Github: {azul}{github}
'''

##################################################################
##################################################################

def escanear():
    global host
    global puertos_abiertos
    global count
    global nm
    
    print(f"{white}[+] {cyan}Host:{verde}"+" %s" % host)
    for proto in nm[host].all_protocols():
	    print(f"{white}[+] {cyan}Protocol:{verde}"+" %s\n" % proto)
	    lport = nm[host][proto].keys()
	    sorted(lport)
	    for port in lport:
		    print(f"{white}[+] {cyan}port: {verde}"+"%s" % port +f"\t{cyan}state:{verde}"+" %s" % nm[host][proto][port]["state"])
		    if count==0:
			    puertos_abiertos=puertos_abiertos+str(port)
			    count=1
		    else:
			    puertos_abiertos=puertos_abiertos+","+str(port)

if __name__ == "__main__":
    print(banner+info)
    host = input(f'{white}[+] {cyan}Objetivo:{verde} ')
    results = nm.scan(hosts=host,arguments="-sT -n -Pn -T4")
    escanear()

else:
    sys.exit(0)
