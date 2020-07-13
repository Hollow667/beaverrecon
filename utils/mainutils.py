import requests
from utils.colors import *
from utils.settings import *
import json
import urllib3
from bs4 import BeautifulSoup
from emailrep import EmailRep
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

themecolor = colortocode(getcolor())

def igpartialemail(username):

    url = "https://instagram.com/accounts/account_recovery_send_ajax/"
    headers = {
    'Host' : 'www.instagram.com',
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'X-CSRFToken': 'yNDkIGI5RNIm80rGlwMdYs7THx8OEdJy',
    'X-Instagram-AJAX': '8f02a43ad311',
    'X-IG-App-ID': '936619743392459',
    'X-IG-WWW-Claim': '0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '58',
    'Origin': 'https://www.instagram.com',
    'Connection': 'close',
    'Referer': 'https://www.instagram.com/accounts/password/reset/',
    'Cookie': 'ig_did=5C63FD9D-DC35-4A74-9211-CA81AA197467; csrftoken=yNDkIGI5RNIm80rGlwMdYs7THx8OEdJy; mid=Xedu2wAEAAGU7rLTjcGhohUrbx_F; rur=VLL'
    }

    rawdata = "email_or_username=" + username + "&recaptcha_challenge_field="

    r = requests.post(url, headers=headers, data=rawdata)
    yee = r.json()
    yee = str(yee["message"]).strip("Thanks! Please").strip(" for a link to reset your password.").strip("check").lstrip().rstrip().replace('"', "").replace('[', "").replace(']', "")
    
    if yee == "N":
        yee = "User Not Found"
    elif yee == "We couldn't reach your email address. Please try resetting your password using a different option, or contact support":
        yee = "No Results Found :("
    elif yee == "query should not be em":
        yee = "No Results Found :("

    return yee

def scylla(typelookup, query):
    finalinfo = []
    try:
        headers = {'Accept': 'application/json'}
        url = f"https://scylla.sh/search?q={typelookup}:{query}"
        r = requests.get(url, verify=False, headers=headers)
        if r.status_code != 200:
            finalinfo.append("scylla.sh is down :(\n")
            return finalinfo
        jsn = r.json()
        for key in jsn:
            for x in key:
                if x == "_source":
                    info = key[x]
                    for i in list(info)[-1].split("\n"):
                        info[i] = f"{info[i]}\n"

                    if info[typelookup] != query:
                        pass
                    else:
                        for z in info:
                            finalinfo.append(f"{themecolor}{z}{reset}: {info[z]}")

        if bool(finalinfo) == False:
            finalinfo.append("No Results Found :(\n")
        return finalinfo

    except Exception as e:
        finalinfo.append("Lookup Failed!")
        finalinfo.append(f"Error: {str(e)}\n")
        return finalinfo

def hashcheck(hash):
    checked = []
    try:
        apikey = getapikey("hasheskey")
        if apikey == "None":
            checked.append("No Hashes Api Key Found...")
            checked.append("This Can Be Updated Via Settings")
        elif len(apikey) != 30:
            checked.append("Invalid Api Key Detected...")
        url = f"https://hashes.org/api.php?key={apikey}&query={hash}"
        r = requests.get(url)
        resp = r.text
        ye = json.loads(resp)
        for x in ye:
            if 'result' in x:
                um = ye[x]
                for x in um:
                    if hash in x:
                        info = um[x]
                        for key in info:
                            if 'hexplain' in key:
                                pass
                            else:
                                checked.append(f"{themecolor}{key}{reset}: {info[key]}")
        return checked

    except TypeError:
        checked.append("No Results Found :(")
        return checked
    except json.decoder.JSONDecodeError:
        checked.append("Api is down :(")
        return checked

def emailrep(email):
    emailinfo = []
    apikey = getapikey("emailrepkey")
    if apikey == "None" or len(apikey) != 48:
        emailrep = EmailRep()
    else:
        emailrep = EmailRep(apikey)
    info = emailrep.query(email)
    for key in info:
        if 'details' in key:
            stuff = info[key]
            for x in stuff:
                if 'profiles' in x:
                    profiles = str(stuff[x]).replace("'", "").strip("[").strip("]")
                    emailrep = f"{themecolor}{x}{reset}: {profiles}"
                    emailinfo.append(emailrep)
                else:
                    emailrep = f"{themecolor}{x}{reset}: {stuff[x]}"
                    emailinfo.append(emailrep)
        else:
            emailrep = f"{themecolor}{key}{reset}: {info[key]}"
            emailinfo.append(emailrep)
    return emailinfo

def checkbreaches(email): # this function is here just in case the one below doesnt work anymore
    datalist = []
    try:
        driver.get(f'https://haveibeenpwned.com/unifiedsearch/{email}')
        lol = driver.find_elements_by_xpath("//html")
        for t in lol:
            info = json.loads(t.text)
            for x in info:
                if "Breaches" in x:
                    breaches = info[x]
                    for breach in breaches:
                        for idk in breach:
                            if idk == "Title":
                                title = breach[idk]
                            elif idk == "DataClasses":
                                breachdata = str(breach[idk]).replace("'", "").strip("[").strip("]")
                                datalist.append(f"{title}: {breachdata}")
                            else:
                                pass
                else:
                    pass
        driver.quit()
        return datalist
    except json.decoder.JSONDecodeError:
        datalist.append("No Info Found")
        return datalist

def haveibeenpwned(email):
    finalinfo = []
    try:
        headers = {"hibp-api-key": "da0f1fc9a24a4a5c81dcf09bb7f195f3"} # stole this key off some random site
        leakedreq = requests.get(f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=true", headers=headers)
        pastesreq = requests.get(f"https://haveibeenpwned.com/api/v3/pasteaccount/{email}", headers=headers)



        if leakedreq.status_code == 404:
            finalinfo.append("No Leaks Found")
            return finalinfo
        elif leakedreq.status_code == 401:
            finalinfo.append("Api is down :(")
            return finalinfo
        else:
            finalinfo.append(f"[{themecolor}+{reset}] {bold}Leaks{reset} [{themecolor}+{reset}]")
            leakedjson = json.loads(leakedreq.text)

            for leakdic in leakedjson:
                for leak in leakdic:
                    finalinfo.append(f"{bold}{leakdic[leak]}{reset}")
                    pass

        if pastesreq.status_code == 404:
            finalinfo.append("\nNo Pastes Found")
        else:
            finalinfo.append(f"\n[{themecolor}+{reset}] {bold}Pastes{reset} [{themecolor}+{reset}]")
            pastesjson = json.loads(pastesreq.text)

            for pastedic in pastesjson:
                for x in pastedic:
                    if x == "Id":
                        if "http" in pastedic[x]:
                            finalinfo.append(f"{bold}{pastedic[x]}{reset}")
                            pass
                        else:
                            finalinfo.append(f"{bold}http://pastebin.com/{pastedic[x]}{reset}")
        return finalinfo
    except:
        finalinfo.append("No Results Found :(")

def pwndb2(email):
    finalinfo = []
    try:
        email = email.split("@")
        url = "https://pwndb2am4tzkvold.onion.ws/"
        data = f"luser={email[0]}&domain={email[1]}&luseropr=0&domainopr=0&submitform=em"
        headers = {'Host': 'pwndb2am4tzkvold.onion.ws','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
        r = requests.post(url, data=data, allow_redirects=True, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        if "1\nArray" not in str(soup):
            finalinfo.append("No Results Found :(\n")
            return finalinfo
        else:
            info = str(soup.find("pre")).split("1\nArray", 1)[-1]
            for line in info.split("\n"):
                line = line.rstrip().lstrip()
                if "=&gt" not in line: pass
                else:
                    line = line.replace("=&gt;", ':').split(":")
                    line[0] = line[0].strip("[").strip("] ")
                    line[1] = line[1].strip(" ")
                    if line[0] == "id":
                        pass
                    if line[0] == "password":
                        line[1] = f'{line[1]}\n'
                    finalinfo.append(f"{line[0]}: {line[1]}")
        return finalinfo

    except Exception as e:
        finalinfo.append("Lookup Failed!")
        finalinfo.append(f"Error: {str(e)}\n")
        return finalinfo
