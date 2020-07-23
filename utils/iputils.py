import requests
from utils.colors import *
from utils.settings import *

themecolor = colortocode(getcolor())

def isgoodipv4(ipv4):
    pieces = ipv4.split('.')
    if len(pieces) != 4: return False
    try: return all(0<=int(p)<256 for p in pieces)
    except ValueError: return False

def iplookup(ip):
    finalinfo = []
    url = f'http://ip-api.com/json/{ip}'
    r = requests.get(url)
    jsonresp = r.json()
    for x in jsonresp:
        finalinfo.append(f"{themecolor}{x}{reset}: {bold}{jsonresp[x]}{reset}")
    return finalinfo
