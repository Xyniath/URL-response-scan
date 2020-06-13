import os
import sys
import re
import requests

def urlScan(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
        response = requests.get(url, headers=headers)
        print(response)
    except requests.ConnectionError:
        print("failed to connect: " + url)

def formatUrl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'http://{}'.format(url)
    return url

def openFile(urlFile):
    if os.path.exists(urlFile):
        with open(urlFile) as urlList: #opens the file
            for line in urlList:
                url = formatUrl(line)
                urlScan(url)
                #print(line)
    else:
        print("File does not exist")
        os._exit(0)
        
if __name__== "__main__":
    openFile(sys.argv[1])


