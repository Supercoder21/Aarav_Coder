import time
import os
os.system("")
inventory = {}
n=0
y=0
invent = ''
BLACK  = '\33[30m'
RED    = '\33[31m'
GREEN  = '\33[32m'
YELLOW = '\33[33m'
BLUE   = '\33[34m'
VIOLET = '\33[35m'
BEIGE  = '\33[36m'
WHITE  = '\33[37m'
BLACK2  = '\33[4;20m'
RED2    = '\33[4;21m'
GREEN2  = '\33[4;22m'
YELLOW2 = '\33[4;23m'
BLUE2   = '\33[4;24m'
VIOLET2 = '\33[4;25m'
BEIGE2  = '\33[4;26m'
WHITE2  = '\33[4;27m'
END = '\33[0m'
def color(COLOR):
    print(COLOR)
def maketext(color,string,tim=0.25):
    string = str(string)
    chars = list(string)
    for i in chars:
        print(color+i+END,end='',flush=True)
        time.sleep(tim)
def colortext(color,string):
    string = str(string)
    pri
    return color+string+END
def enter(string,color):
    string = str(string)
    choice = input(color+string)
    end = print(END,end = '')
    return choice
def endtext():
    print('',end = '\n')
def begin(welcome,color):
    print(color,welcome,os.getlogin(),END)
def itemadd(key,value):
    inventory[key] = value
def show():
    for k, v in inventory.items():
        print(k)
        print(v)
        print('')
def change(oldkey,newkey):
    inventory[newkey] = inventory[oldkey]
    del inventory[oldkey]
def textpic(file):
    import climage
    output = climage.convert(file)
    print(output)
def end():
    print(END)
