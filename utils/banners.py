from utils.colors import *
from utils.settings import *
from utils.update import *

def ipmenu(themec, target):
    print(f'''{reset}
 {bold}Current Target: {themec}{target}{reset}
╭───┬───────────────┬─────────────────────────╮
│ {themec}1{reset} │ {bold}GeoIP{reset}         │ {themec}Geo Locate A I.P.{reset}       │
│ {themec}2{reset} │ {bold}ThatsThem{reset}     │ {themec}Lookup On ThatsThem.com{reset} │
│ {themec}3{reset} │ {bold}Change Target{reset} │ {themec}Change Current Target{reset}   │
│ {themec}0{reset} │ {bold}Go Back{reset}       ├─────────────────────────╯
╰───┴───────────────╯
    ''')

def usernamemenu(themec, target):
    print(f'''{reset}
 {bold}Current Target: {themec}{target}{reset}
╭───┬───────────────┬────────────────────────────────────────────────────╮
│ {themec}1{reset} │ {bold}scylla{reset}        │ {themec}Data Breach Lookup(Shows Leaked Info){reset}              │
│ {themec}2{reset} │ {bold}instagram{reset}     │ {themec}Get The Partial Email or Phone On A Instagram User{reset} │
│ {themec}3{reset} │ {bold}change target{reset} │ {themec}Change Current Target{reset}                              │
│ {themec}0{reset} │ {bold}Go Back{reset}       ├────────────────────────────────────────────────────╯
╰───┴───────────────╯
    ''')

def phonemenu(themec, target):
    print(f'''{reset}
 {bold}Current Target: {themec}{target}{reset}
╭───┬───────────────┬────────────────────────────────────────────────────╮
│ {themec}1{reset} │ {bold}ThatsThem{reset}     │ {themec}Information Lookup{reset}                                 │
│ {themec}2{reset} │ {bold}Phone Scrape{reset}  │ {themec}Scrapes Multiple Sites For Information{reset}             │
│ {themec}3{reset} │ {bold}change target{reset} │ {themec}Change Current Target{reset}                              │
│ {themec}0{reset} │ {bold}Go Back{reset}       ├────────────────────────────────────────────────────╯
╰───┴───────────────╯
    ''')

def emailmenu(themec, target):
    print(f'''{reset}
 {bold}Current Target: {themec}{target}{reset}
╭───┬───────────────┬───────────────────────────────────────╮
│ {themec}1{reset} │ {bold}EmailRep{reset}      │ {themec}Email Reputation Lookup{reset}               │
│ {themec}2{reset} │ {bold}Scylla{reset}        │ {themec}Data Breach Lookup(shows leaked info){reset} │
│ {themec}3{reset} │ {bold}Pwndb2{reset}        │ {themec}Data Breach Lookup(shows leaked info){reset} │
│ {themec}4{reset} │ {bold}HIBP{reset}          │ {themec}Data Breach Lookup(only shows leaks){reset}  │
│ {themec}5{reset} │ {bold}ThatsThem{reset}     │ {themec}Information Lookup                  {reset}  │
│ {themec}6{reset} │ {bold}Change Target{reset} │ {themec}Change Current Target{reset}                 │
│ {themec}0{reset} │ {bold}Go Back{reset}       ├───────────────────────────────────────╯
╰───┴───────────────╯
    ''')


def settingsmenu(themec):
    print(f'''{reset}
╭───┬──────────────────╮
│ {themec}1{reset} │ {themec}Color Menu{reset}       │
│ {themec}2{reset} │ {themec}Update Api Keys{reset}  │
│ {themec}3{reset} │ {themec}Check For Update{reset} │
│ {themec}4{reset} │ {themec}Change Log{reset}       │
│ {themec}0{reset} │ {themec}Go Back{reset}          │
╰───┴──────────────────╯
    ''')

def banner(themec, version):
    return (f'''{themec}
 {reset}╭──────────┬───────┬────────╮ {themec}Version{reset}: {version}
 {reset}│  {themec}B E A V E R   R E C O N  {reset}│ {themec}{checkversion(version)}{reset}
 {reset}╰──────────╰───────╯────────╯ {themec}Coded By{reset}: catlinux{themec}{reset}
    ╭────────────────────╮
    │       {reset}Options      │ 
    ├───┬────────────────┤
    │ {themec}1{reset} │ {themec}Name{reset}           │
    │ {themec}2{reset} │ {themec}Address{reset}        │
    │ {themec}3{reset} │ {themec}IP{reset}             │
    │ {themec}4{reset} │ {themec}Username{reset}       │
    │ {themec}5{reset} │ {themec}Email{reset}          │
    │ {themec}6{reset} │ {themec}Phone{reset}          │
    │ {themec}7{reset} │ {themec}Hash Decrypt{reset}   │
    │ {themec}8{reset} │ {themec}Info{reset}           │
    │ {themec}9{reset} │ {themec}Settings{reset}       │
    │ {themec}0{reset} │ {themec}Exit{reset}           │
    ╰───┴────────────────╯''' + reset)

def colormenu():
    print(f'''
╭──────────────────────────╮
│    color selection       │
├────────────┬─────────────┤
│ {black}black{reset}      │ {darkgrey}darkgrey{reset}    │
│ {red}red{reset}        │ {lightred}lightred{reset}    │
│ {green}green{reset}      │ {lightgreen}lightgreen{reset}  │
│ {orange}orange{reset}     │ {yellow}yellow{reset}      │
│ {blue}blue{reset}       │ {lightblue}lightblue{reset}   │
│ {purple}purple{reset}     │ {pink}pink{reset}        │
│ {cyan}cyan{reset}       │  {lightcyan}lightcyan{reset}  │
│ {lightgrey}lightgrey{reset}  ├─────────────╯
╰────────────╯
''')
