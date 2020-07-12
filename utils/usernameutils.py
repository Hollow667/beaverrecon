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

def scyllalookup(query, lookup): # Password, User, PassHash, PassSalt, Email, IP, UserId, Name, Domain 
    if query == "Password" or "PassHash" or "PassSalt":
        pass
    else:
        lookup = lookup.lower()
    try:
        info = []

        emails = []
        passwords = []
        users = []
        pwdhshs = []
        pwdslts = []
        ips = []
        userids = []
        names = []
        breaches = []

        headers = {'Accept': 'application/json', 'Authorization': 'Basic c2FtbXk6QmFzaWNQYXNzd29yZCE='}
        url = f"https://scylla.sh/search?q={query}:{lookup}"
        r = requests.get(url, headers=headers, verify=False, )
        json = r.json()
        readablejson = json.dumps(json.loads(str(r.text)),sort_keys=True, indent=4, separators=('', ':'))

        num = 0
        while True:
            try:
                out = json[num]["_source"]
                if str(lookup) in json.dumps(out).lower():
                    try: email = out["Email"]; emails.append(f'{themecolor}Email{reset}: {email}{reset}\n')
                    except KeyError: emails.append(""); pass
                    try: password = out["Password"]; passwords.append(f'{themecolor}Password{reset}: {password}{reset}\n')
                    except KeyError: passwords.append(""); pass
                    try: user = out["User"]; users.append(f'{themecolor}User{reset}: {user}{reset}\n')
                    except KeyError: users.append(""); pass
                    try: passhash = out["PassHash"]; pwdhshs.append(f'{themecolor}Password Hash{reset}: {passhash}{reset}\n')
                    except KeyError: pwdhshs.append(""); pass
                    try: passalt = out["PassSalt"]; pwdslts.append(f'{themecolor}Password{reset}: {passalt}{reset}\n')
                    except KeyError: pwdslts.append(""); pass
                    try: ip = out["IP"]; ips.append(f'{themecolor}IP{reset}: {ip}{reset}\n')
                    except KeyError: ips.append(""); pass
                    try: userid = out["UserId"]; userids.append(f'{themecolor}User ID{reset}: {userid}{reset}\n')
                    except KeyError: userids.append(""); pass
                    try: name = out["Name"]; names.append(f'{themecolor}Name{reset}: {name}{reset}\n')
                    except KeyError: names.append(""); pass
                    try: breach = out["Domain"]; breaches.append(f'{themecolor}Breach{reset}: {breach}{reset}\n')
                    except KeyError: breaches.append(""); pass
                num += 1 
            except:
                pass
                break 
    except: 
        pass
    for email, password, user, passhash, passalt, ip, userid, name, breach in zip(emails, passwords, users, pwdhshs, pwdslts, ips, userids, names, breaches):
        info.append(email + password + user + passhash + passalt + ip + userid + name + breach)
    if bool(info) == False:
        info.append("No Results Found :(")
    
    return info

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