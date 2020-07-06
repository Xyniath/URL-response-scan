import os
import sys
import re
import requests

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

load = "[>$<] ".replace(">", green).replace("<", clear)
err = "[>-<] ".replace(">", red).replace("<", clear)
intro = introart.replace(">", green).replace("<", clear)


def helpScreen():
    print("ERROR:")
    print("USAGE - python urlscan.py [domain list]")


def urlScan(url):
    try:
        r = requests.get(url)
        print('[' + str(r.status_code) + '] ' + url)
    except requests.ConnectionError:
        print("failed to connect: " + url)


def formatUrl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'http://{}'.format(url)
    return url


def openFile(urlFile):
    if os.path.exists(urlFile):
        with open(urlFile) as urlList:  # opens the file
            for line in urlList:
                url = formatUrl(line)
                urlScan(url)
                # print(line)
    else:
        print("File does not exist")
        os._exit(0)


if __name__ == "__main__":
    print(intro)
    try:
        openFile(sys.argv[1])
    except:
        helpScreen()
