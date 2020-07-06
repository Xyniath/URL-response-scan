# Add argparse support
# Add timeout option
# Add output file
# Choose to verbose
# Choose what responses to output
# Add basic responses to help (maybe using another python sc)
# Fix exception

import os
import sys
import re
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("domainlist", help = "file path of domain list")
parser.add_argument("-t", "--timeout", help = "timeout in seconds (default 20)")
args = parser.parse_args()

introart = """
> _    _ _____  _         _____  _____          _   _  <
>| |  | |  __ \| |       / ____|/ ____|   /\   | \ | | <
>| |  | | |__) | |      | (___ | |       /  \  |  \| | <
>| |  | |  _  /| |       \___ \| |      / /\ \ | . ` | <
>| |__| | | \ \| |____   ____) | |____ / ____ \| |\  | <
> \____/|_|  \_\______| |_____/ \_____/_/    \_\_| \_| <
                                                       <
                ={>   BY XYNIATH   <}=                
                                                        
                  Twitter : >@Xyniath<                  
               Site : >xyniath.github.io<               """

green = "\033[1;32m"
red = "\033[1;31m"
clear = "\033[0m"

load = "[>$<] ".replace(">", red).replace("<", clear)
err = "[>-<] ".replace(">", red).replace("<", clear)
intro = introart.replace(">", red).replace("<", clear)

print(intro)

def urlScan(url):
    try:
        r = requests.get(url, timeout=20)
        print('[' + str(r.status_code) + '] ' + url)
    except requests.ConnectionError:
        print("[ERR] " + url)


def formatUrl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'http://{}'.format(url)
    return url

if os.path.exists(args.domainlist):
    with open(str(args.domainlist)) as urlList:  # opens the file
        for line in urlList:
            url = formatUrl(line)
            urlScan(url)
else:
    print("File does not exist")
    os._exit(0)
