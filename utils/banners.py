from utils.colors import *
from utils.settings import *

def ipmenu(themec, target):
    print(f'''{reset}
{bold}Current Target: {themec}{target}{reset}
 _____________________________________________
| {themec}1{reset} | {bold}GeoIP{reset}         | {themec}Geo Locate A I.P.{reset}       |
| {themec}2{reset} | {bold}ThatsThem{reset}     | {themec}Lookup On ThatsThem.com{reset} |
| {themec}3{reset} | {bold}Change Target{reset} | {themec}Change Current Target{reset}   |
| {themec}0{reset} | {bold}Go Back{reset}       |_________________________|
|___|_______________|
    ''')

def usernamemenu(themec, target):
    print(f'''{reset}
{bold}Current Target: {themec}{target}{reset}
 ________________________________________________________________________
| {themec}1{reset} | {bold}scylla{reset}        | {themec}Data Breach Lookup(Shows Leaked Info){reset}              |
| {themec}2{reset} | {bold}instagram{reset}     | {themec}Get The Partial Email or Phone On A Instagram User{reset} |
| {themec}3{reset} | {bold}change target{reset} | {themec}Change Current Target{reset}                              |
| {themec}0{reset} | {bold}Go Back{reset}       |____________________________________________________|
|___|_______________|
    ''')

def emailmenu(themec, target):
    print(f'''{reset}
{bold}Current Target: {themec}{target}{reset}
 ___________________________________________________________
| {themec}1{reset} | {bold}EmailRep{reset}      | {themec}Email Reputation Lookup{reset}               |
| {themec}2{reset} | {bold}Scylla{reset}        | {themec}Data Breach Lookup(shows leaked info){reset} |
| {themec}3{reset} | {bold}Pwndb2{reset}        | {themec}Data Breach Lookup(shows leaked info){reset} |
| {themec}4{reset} | {bold}HIBP{reset}          | {themec}Data Breach Lookup(only shows leaks){reset}  |
| {themec}5{reset} | {bold}Change Target{reset} | {themec}Change Current Target{reset}                 |
| {themec}0{reset} | {bold}Go Back{reset}       |_______________________________________|
|___|_______________|
    ''')


def settingsmenu(themec):
    print(f'''{reset}
 _____________________
| {themec}1{reset} | {themec}Color Menu{reset}       |
| {themec}2{reset} | {themec}Update Api Keys{reset}  |
| {themec}3{reset} | {themec}Check For Update{reset} |
| {themec}0{reset} | {themec}Go Back{reset}          |
|___|_________________|
    ''')

def banner(themec):
    return (f'''{themec}
 ______
|   __ \.-----.---.-.--.--.-----.----.
|   __ <|  -__|  _  |  |  |  -__|   _|
|______/|_____|___._|\___/|_____|__|
 ______
|   __ \.-----.----.-----.-----.
|      <|  -__|  __|  _  |     |
|___|__||_____|____|_____|__|__|

 Made By {reset}catlinux{themec} with love <3
{reset}
 ____________________
| {themec}Version{reset}: 0.7       |
|____________________|
| {themec}1{reset} | {themec}IP{reset}             |
| {themec}2{reset} | {themec}Username{reset}       |
| {themec}3{reset} | {themec}Email{reset}          |
| {themec}4{reset} | {themec}Phone{reset}          |
| {themec}5{reset} | {themec}Hash Decrypt{reset}   |
| {themec}6{reset} | {themec}Info{reset}           |
| {themec}7{reset} | {themec}Settings{reset}       |
| {themec}0{reset} | {themec}Exit{reset}           |
|___|________________|
''' + reset)

def colormenu():
    print(f'''{reset}
 __________________________
|    color selection       |
|__________________________|
| {black}black{reset}      | {bgblack}bgblack{reset}     |
| {red}red{reset}        | {bgred}bgred{reset}       |
| {green}green{reset}      | {bggreen}bggreen{reset}     |
| {orange}orange{reset}     | {bgorange}bgorange{reset}    |
| {blue}blue{reset}       | {bgblue}bgblue{reset}      |
| {purple}purple{reset}     | {bgpurple}bgpurple{reset}    |
| {cyan}cyan{reset}       | {bgcyan}bgcyan{reset}      |
| {lightgrey}lightgrey{reset}  | {bglightgrey}bglightgrey{reset} |
| {darkgrey}darkgrey{reset}   |_____________| 
| {lightred}lightred{reset}   |
| {lightgreen}lightgreen{reset} |
| {yellow}yellow{reset}     |
| {lightblue}lightblue{reset}  |
| {pink}pink{reset}       |
| {lightcyan}lightcyan{reset}  |
|____________|
''')

