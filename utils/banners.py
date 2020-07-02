from utils.colors import *
from utils.settings import *

def ipmenu(themec, target):
    print(f'''{reset}
{bold}Current Target: {themec}{target}{reset}
 ___________________
| {themec}1{reset} | {themec}geoip{reset}         |
| {themec}2{reset} | {themec}thatsthem{reset}     |
| {themec}3{reset} | {themec}change target{reset} |
| {themec}0{reset} | {themec}Go Back{reset}       |
|___|_______________|
    ''')

def usernamemenu(themec, target):
    print(f'''{reset}
{bold}Current Target: {themec}{target}{reset}
 ___________________    
| {themec}1{reset} | {themec}scylla{reset}        |
| {themec}2{reset} | {themec}instagram{reset}     |
| {themec}3{reset} | {themec}change target{reset} |
| {themec}0{reset} | {themec}Go Back{reset}       |
|___|_______________|
    ''')

def emailmenu(themec, target):
    print(f'''{reset}
{bold}Current Target: {themec}{target}{reset}
 ___________________    
| {themec}1{reset} | {themec}emailrep{reset}      |
| {themec}2{reset} | {themec}scylla{reset}        |
| {themec}3{reset} | {themec}hibp{reset}          |
| {themec}4{reset} | {themec}change target{reset} |
| {themec}0{reset} | {themec}Go Back{reset}       |
|___|_______________|
    ''')


def settingsmenu(themec):
    print(f'''{reset}
 _____________________
| {themec}1{reset} | {themec}Color Menu{reset}      |
| {themec}2{reset} | {themec}Update Api Keys{reset} |
| {themec}0{reset} | {themec}Go Back{reset}         |
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
| {themec}Version{reset}: 0.6       |
|____________________|
| {themec}1{reset} | {themec}IP{reset}             |
| {themec}2{reset} | {themec}Username{reset}       |
| {themec}3{reset} | {themec}Email{reset}          |
| {themec}4{reset} | {themec}Hash Decrypt{reset}   |
| {themec}5{reset} | {themec}Info{reset}           |
| {themec}6{reset} | {themec}Settings{reset}       |
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


