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


def thatsthemip(lookup): #People, phone, address(street, city, state or zip), email, ip
    url = 'http://ip-api.com/json/{}'.format(lookup)
    response = requests.get(url)
    geoip = response.json()
    region = geoip["region"]

    output = []
    names = []
    addresses = []
    phones = []
    emails = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"}
    url = f"https://thatsthem.com/ip/{lookup}"
    r = requests.get(url, headers=headers)
    html = r.text
    for line in html.split('\n'):
        if '<a href="/address' in line:
            address = line.lstrip()
            address = (address.strip("""<a href="/address/""")).replace('"', '').replace('>', '').replace('-', ' ').rstrip()
            address = str(address)
            addresses.append(address)

    for line in html.split('\n'):
        if '<span itemprop="name">' in line:
            name = line.lstrip().rstrip()
            name = name.strip('<span itemprop="name">').strip("</").split("<", 1)[0]
            name = str(name)
            names.append(name)
    
    for line in html.split('\n'):
        if '<span itemprop="email">' in line:
            email = line.rstrip().lstrip().strip('<span itemprop="email">').split("<", 1)[0]
            emails.append(email)

    for line in html.split('\n'):
        if 'telephone' in line:
            phone = line.lstrip().rstrip().strip('<span itemprop="telephone">"').split("<", 1)[0].split("-")
            phone = "({}) {}-{}".format(phone[0], phone[1], phone[2])
            phones.append(phone)
    
    names = names[3:]
    for name, address, phone, email in zip(names, addresses, phones, emails):
        if region in address:
            address = f"{bold}Name: {blue}{name}\n{reset}{bold}Address: {bold}{blue}{address}{reset}\nPhone: {bold}{blue}{phone}{reset}\nEmail: {bold}{blue}{email}{reset}\nAccuracy: {green}Most Accurate{reset}\n"
            output.append(address)
        else:
            address = bold + "Name: " + blue + name + "\n" + reset + bold + "Address: " + bold + blue + address + reset + "\nPhone: " + bold + blue + phone + reset + "\nEmail: "+ bold + blue + email + reset + "\nAccuracy: " + red + "Not Accurate" + reset + "\n"
            output.append(address)
    try:
        output[-1] = output[-1].rstrip()
    except: 
        pass

    if bool(output) == False:
        output.append("No Results Found :(")
    return output

