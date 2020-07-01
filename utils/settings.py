from utils.colors import *

def getapikey(setting):
    readst = open("utils//settings.txt", 'r').readlines()
    for line in readst:
        line = line.rstrip().split(": ")
        if line[0] == setting:
            apikey = line[1]
    return apikey

def chaneapikey(setting, key):
    readst = open("utils//settings.txt", 'r').readlines()
    current = getapikey(setting)
    writest = open("utils//settings.txt", 'w')
    for line in readst:
        if setting in line:
            repapi = line.replace(current, key)
            writest.write(f"{repapi}")
        else:
            writest.write(f"{line}")

def getcolor():
    readst = open("utils//settings.txt", 'r').readlines()
    for line in readst:
        line = line.rstrip().split(": ")
        if line[0] == 'color':
            currentcolor = line[1]
    return currentcolor

def changecolor(color):
    readst = open("utils//settings.txt", 'r').readlines()
    cc = getcolor()
    writest = open("utils//settings.txt", 'w')
    for line in readst:
        repcolor = line.replace(cc, color)
        writest.write(f"{repcolor}")


def colortocode(color):
    if color == "black":
        bannercolor = bold + black
    elif color == "red":
        bannercolor = bold + red
    elif color == "green":
        bannercolor = bold + green
    elif color == "orange":
        bannercolor = bold + orange
    elif color == "blue":
        bannercolor = bold + blue
    elif color == "purple":
        bannercolor = bold + purple
    elif color == "cyan":
        bannercolor = bold + cyan
    elif color == "lightgrey":
        bannercolor = bold + lightgrey
    elif color == "darkgrey":
        bannercolor = bold + darkgrey
    elif color == "lightred":
        bannercolor = bold + lightred
    elif color == "lightgreen":
        bannercolor = bold + lightgreen
    elif color == "yellow":
        bannercolor = bold + yellow
    elif color == "lightblue":
        bannercolor = bold + lightblue
    elif color == "pink":
        bannercolor = bold + pink
    elif color == "lightcyan":
        bannercolor = bold + lightcyan
    elif color == "bgblack":
        bannercolor = bold + bgblack
    elif color == "bgred":
        bannercolor = bold + bgred
    elif color == "bggreen":
        bannercolor = bold + bggreen
    elif color == "bgorange":
        bannercolor = bold + bgorange
    elif color == "bgblue":
        bannercolor = bold + bgblue
    elif color == "bgpurple":
        bannercolor = bold + bgpurple
    elif color == "bgcyan":
        bannercolor = bold + bgcyan
    elif color == "bglightgrey":
        bannercolor = bold + bglightgrey
    else:
        bannercolor = bold + blue
    return bannercolor


def colormenu():
    print(f'''
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

