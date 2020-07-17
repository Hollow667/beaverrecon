from os import system
from utils.colors import *
from utils.iputils import *
from utils.mainutils import *
from utils.banners import *
from utils.settings import *
from utils.phoneutils import *
from utils.update import *
from time import sleep
from random import choice
import sys

## Version
VERSION = "0.7.3"

def cls():
    if sys.platform == 'win32':
        system("cls")
    else:
        system("clear")


def mainloop(themec):
    try:
        reload = False
        while True:
            if reload == True:
                break

            icons = ['ツ', '卐', '✦', '☣']
            icon = choice(icons)
            cls()
            print(banner(themec, VERSION))
            option = input(f"{reset}{bold}Option:{reset}{themec} ")
            if option.isnumeric():
                pass
            else:
                cls()
                continue

            if option == "1":
                target = []
                try:
                    cls()
                    ip = input(f"{reset}{bold}IP:{reset}{themec} ")
                    if bool(isgoodipv4(ip)) == True:
                        target.append(ip)
                        pass

                    else:
                        cls()
                        print (f"{orange}please enter a valid ipv4 address...")
                        sleep(2)
                        continue

                    while True:
                        cls()
                        for x in target:
                            currenttarget = x.lstrip().rstrip()
                        ipmenu(themec, currenttarget)
                        option = input(f"{reset}{bold}Option:{reset}{themec} ")

                        if option == "1":
                            cls()
                            print (f"{reset}{green}{icon}{reset} {blue} Geo Lookup {green}{icon}{reset}")
                            for line in iplookup(currenttarget):
                                print (line)
                            input(f"{reset}{bold}\npress enter to go back:{reset}{themec} ")
                            continue

                        elif option == "2":
                            cls()
                            print (f"{reset}{green}{icon}{reset} {blue} ThatsThem Lookup {green}{icon}{reset}")
                            for line in thatsthemip(currenttarget):
                                if line == "":
                                    print ("None")
                                else:
                                    print (line)
                            input(f"{reset}{bold}\npress enter to go back:{reset}{themec} ")
                            continue

                        elif option == "3":
                            cls()
                            changetarget = input(f"{reset}{bold}Target:{reset}{themec} ")
                            if bool(isgoodipv4(changetarget)) == True:
                                target.clear()
                                target.append(changetarget)
                                continue

                            else: 
                                print("Invalid IP...")
                                sleep(1)
                                continue

                        elif option == "0":
                            break

                        else:
                            continue
                except Exception as e:
                    cls()
                    print (f"Error Has Occurred: {str(e)}")
                    sleep(2)
                    continue
            
            elif option == "2":
                target = []
                cls()
                username = input(f"{reset}{bold}Username:{reset}{themec} ")
                if username == "":
                    cls()
                    print("Please Enter A Username...")
                    sleep(2)
                    continue
                target.append(username)
                while True:
                    cls()
                    for x in target:
                        currenttarget = x.lstrip().rstrip()
                    usernamemenu(themec, currenttarget)
                    option = input(f"{reset}{bold}Option:{reset}{themec} ")

                    if option == "1":
                        cls()
                        print (f"{reset}{green}{icon}{reset} {blue} Scylla Lookup {green}{icon}{reset}")
                        for x in scylla("User", currenttarget):
                            print (x)
                        input(f"{reset}{bold}press enter to go back:{reset}{themec} ")
                        continue

                    elif option == "2":
                        cls()
                        print (f"{reset}{green}{icon}{reset} {blue} Instagram Lookup {green}{icon}{reset}")
                        print(igpartialemail(currenttarget))
                        input(f"\n{reset}{bold}press enter to go back:{reset}{themec} ")
                        continue

                    elif option == "3":
                        cls()
                        changetarget = input(f"{reset}{bold}Target:{reset}{themec} ")
                        target.clear()
                        target.append(changetarget)
                        continue
                    elif option == "0":
                        break    
                    else:
                        continue

            elif option == "3":
                target = []
                cls()
                email = input(f"{reset}{bold}Email:{reset}{themec} ")
                if email == "":
                    cls()
                    print("Please Enter A Email...")
                    sleep(2)
                    continue
                if "@" in email:
                    pass
                else:
                    cls()
                    print("Please Enter A Email...")
                    sleep(2)
                    continue
                target.append(email)
                while True:
                    cls()
                    for x in target:
                        currenttarget = x.lstrip().rstrip()
                    emailmenu(themec, currenttarget)
                    option = input(f"{reset}{bold}Option:{reset}{themec} ")

                    if option == "1":
                        cls()
                        print (f"{reset}{green}{icon}{reset} {blue} Emailrep Lookup {green}{icon}{reset}")
                        for x in emailrep(currenttarget):
                            print(x)
                        input(f"\n{reset}{bold}press enter to go back: {themec}")
                        continue

                    elif option == "2":
                        cls()
                        print (f"{reset}{green}{icon}{reset} {blue} Scylla Lookup {green}{icon}{reset}")
                        for x in scylla("Email", currenttarget):
                            print (x)
                        input(f"{reset}{bold}press enter to go back: {themec}")
                        continue

                    elif option == "3":
                        cls()
                        print (f"{reset}{green}{icon}{reset} {blue} Pwndb2 Lookup {green}{icon}{reset}")
                        for x in pwndb2(currenttarget):
                            print (x)
                        input(f"{reset}{bold}press enter to go back: {themec}")
                        continue
                    elif option == "4":
                        cls()
                        print (f"{reset}{green}{icon}{reset} {blue} HIBP Lookup {green}{icon}{reset}")
                        for x in haveibeenpwned(currenttarget):
                            print(x)
                        input(f"{reset}{bold}\npress enter to go back:{reset}{themec} ")
                        continue

                    elif option == "5":
                        cls()
                        changetarget = input(f"{reset}{bold}Target:{reset}{themec} ")
                        target.clear()
                        target.append(changetarget)
                        continue

                    elif option == "0":
                        break

                    else: 
                        continue
            
            elif option == "4":
                cls()
                print("Format: 1231231234\nFYI: This Only Works on US Numbers")
                phone = input(f"{reset}{bold}Phone:{reset}{themec} ").lstrip()
                if phone.isnumeric():
                    pass
                else:
                    cls()
                    print("Please Enter A Valid Phone Number...")
                    sleep(2)
                    continue
                cls()
                print (f"{reset}{green}{icon}{reset} {blue} Phone Scrape {green}{icon}{reset}")

                for x in reversephone(phone):
                    print(x)
                input(f"{reset}{bold}\npress enter to go back:{themec} ")
                continue

            elif option == "5":
                cls()
                hash = input(f"{reset}{bold}Hash:{reset}{themec} ")
                if hash == "":
                    cls()
                    print("Please Enter A Hash...")
                    sleep(2)
                    continue
                cls()
                print (f"{reset}{green}{icon}{reset} {blue} Hash Decrypt(hashes.org) {green}{icon}{reset}")
                for x in hashcheck(hash):
                    print (x)
                input(f"{reset}{bold}\npress enter to go back:{themec} ")
                continue

            elif option == "6":
                cls()
                print (f"{reset}{green}{icon}{reset} {blue} Tool Info {green}{icon}{reset}\n")
                print(f'{themec}Coded By:{reset} CatLinux\n{themec}Info:{reset} Tool Made For Reversing Info Quicker For OSINT Uses \n{themec}Sites Used:{reset} Instagram.com, syclla.sh, ip-api.com, thatsthem.com, emailrep.io, hashes.org, haveibeenpwned.com\n{themec}Version:{reset} {VERSION}')
                input(f"{bold}\npress enter to go back:{reset}{themec} ")
                continue
            
            elif option == "7":
                while True:
                    cls()
                    settingsmenu(themec)
                    option = input(f"{reset}{bold}Option:{reset}{themec} ")
                    if option == '1':
                        while True:
                            cls()
                            print(reset)
                            colormenu()
                            print("type 'back' to go back")
                            col = input("Color: ")
                            if col == "":
                                cls()
                                print("Please Pick A Color...")
                                sleep(2)
                                continue
                            elif col.lower() == "back":
                                break
                            else:
                                cls()
                                changecolor(col)
                                print(f"color changed to: {colortocode(col)}{col}")
                                reload = True
                                sleep(1)
                                break

                    elif option == "2":
                        while True:
                            cls()
                            print(f'{themec}1{reset} | {themec}Hashes.org : {themec}{getapikey("hasheskey")}{reset}')
                            print(f'{themec}2{reset} | {themec}Emailrep.io : {themec}{getapikey("emailrepkey")}{reset}')
                            print(f'{themec}0{reset} | {themec}Go Back{reset}')
                            option = input(f"{reset}{bold}Option:{reset}{themec} ")
                            if option == '1':
                                option = input(f"{reset}{bold}apikey:{reset}{themec} ")
                                chaneapikey("hasheskey", option)
                                cls()
                                print("Hashes.org Api Key Updated")
                                sleep(1.5)
                                reload = True
                                break
                            if option == '2':
                                option = input(f"{reset}{bold}apikey:{reset}{themec} ")
                                chaneapikey("emailrepkey", option)
                                cls()
                                print("Emailrep.io Api Key Updated")
                                sleep(1.5)
                                reload = True
                                break
                            elif option == '0':
                                break
                            else:
                                continue

                    elif option == "3":
                        print("Checking For Update...")
                        sleep(2)
                        check = checkversion(VERSION)
                        print(check)
                        if "Update" in check:
                            option = input("Would You Like To Update?(y/n): ")
                            if option.lower() == 'y':
                                print("Updating...")
                                sleep(2)
                                update()
                            else:
                                continue
                        sleep(2)

                    elif option == "0":
                        break
                    else:
                        continue
            
            elif option == "0":
                print (f"{red}Exiting...{reset}")
                sys.exit()
    except KeyboardInterrupt:
        print (f"{red}\nCtrl-C Pressed Exiting...{reset}")
        sys.exit()

while True:
    themec = colortocode(getcolor())
    mainloop(themec)
    continue
