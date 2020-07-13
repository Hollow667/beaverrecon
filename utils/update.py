import platform
import requests
from os import system

def downloadfiles():
        system("curl -O https://raw.githubusercontent.com/cat-linux/beaverrecon/master/BeaverRecon.py")
        system("curl -O https://raw.githubusercontent.com/cat-linux/beaverrecon/master/requirements.txt")
        system("curl https://raw.githubusercontent.com/cat-linux/beaverrecon/master/utils/banners.py --output utils/banners.py")
        system("curl https://raw.githubusercontent.com/cat-linux/beaverrecon/master/utils/colors.py --output utils/colors.py")
        system("curl https://raw.githubusercontent.com/cat-linux/beaverrecon/master/utils/iputils.py --output utils/iputils.py")
        system("curl https://raw.githubusercontent.com/cat-linux/beaverrecon/master/utils/mainutils.py--output utils/mainutils.py")
        system("curl https://raw.githubusercontent.com/cat-linux/beaverrecon/master/utils/phoneutils.py --output utils/phoneutils.py")
        system("curl https://raw.githubusercontent.com/cat-linux/beaverrecon/master/utils/settings.py --output utils/settings.py")
        system("curl https://raw.githubusercontent.com/cat-linux/beaverrecon/master/utils/settings.txt --output utils/settings.txt")
        system("pip3 install -r requirements.txt")

def checkversion(VERSION):
    url = "https://pastebin.com/raw/D0TdL6w7"
    r = requests.get(url)
    check = r.text
    if VERSION != check:
        info = f"New Update Available!: {str(check)}"
        return info
    else:
        info = "You Are Up To Date."
        return info
        
def update():
    if platform.system() == "Windows":
        downloadfiles()
        system("python BeaverRecon.py")
    else:
        downloadfiles()
        system("python3 BeaverRecon.py")