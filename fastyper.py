from typing import Text
from pynput.keyboard import Key, Controller, Listener
import time
import random_words
import names
import math
import sys
import argparse
import _thread


parser = argparse.ArgumentParser(description='Fastyper', usage=""" %(prog)s [options]

optional arguments:

  -h, --help            show this help message and exit
  --word                Word or phrase to type and send
  --repeat              Times to repeat
  --randomwords 
                        Number of random words to generate
  --randomnames 
                        Number of random names to generate
  --splitword
                        Word or phrase to split, type and send letter by letter""" )

parser.add_argument("--word", help="Word or phrase to type and send", default="None")

parser.add_argument("--repeat", help="Times to repeat", default="10")

parser.add_argument("--randomwords", help="Number of random words to generate", default="None")

parser.add_argument("--randomnames", help="Number of random names to generate", default="None")

parser.add_argument("--splitword", help="Word or phrase to split, type and send letter by letter", default="None")

args = parser.parse_args()


begin = "not yet"
act = "no"
emergency_exit = "not yet"


keyboard = Controller()

def char(wr): 
    return [char for char in wr]

def on_press(key):
    global begin
    global act
    global emergency_exit
    if str(key) == "'\\x18'":
        time.sleep(0.8145412)
        begin = "now"
    if str(key) == 'Key.esc':
        emergency_exit = "now"
        sys.exit(1)

def listenerthread():
    global Listener
    with Listener(on_press=on_press) as Listener:
        Listener.join()

_thread.start_new_thread(listenerthread, ())

def send_keys(wrn, wr):
    for f in range(wrn):
        for i in range(0, len(wr)):
            wrd = char(wr[i])
            for nm in range(0, len(wrd)):
                keyboard.press(wrd[nm])
                keyboard.release(wrd[nm])
                if emergency_exit == "now":
                    sys.exit(0)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

def grname(nm):
    rname = []
    for i in range(nm):
        rname.append(names.get_first_name())
    return rname


def grwor(nm):
    rwor = []
    for i in range(nm):
        rwor.append(random_words.RandomWords().random_word())
    return rwor

def wrsplit(wr):
    wr = wr.split(" ")
    return wr

def wrsplit_argparse(wr):
    wr = wr.split("_")
    return wr

if (args.word == "None") and (args.randomwords == "None") and (args.randomnames == "None"):

    def gout():
        try:
            exit()
        except:
            gout()

    def optionss1():
        try:
            global optio
            global wr
            global wr_nmr
            global wr_nmr
            global nm_nmr
            global nmr
            try:
                print("""
    Type '1' for typing random generated words
    Type '2' for typing random generated names
    Type '3' for typing a custom word or phrase
    Type '4' for typing a custom word or phrase and spit into individual characters
    """)
                optio = int(input("ƒ(x)= "))
                print("\n")
                if optio > 4:
                    print("That option is currently unavailable\n")
                    optionss1()
                if optio == 0:
                    print("That option is currently unavailable\n")
                    optionss1()
            except KeyboardInterrupt:
                sys.exit(1)
            try:
                if math.ldexp(14512, optio*optio) == 232192.0:
                    nm_nmr = int(input("""Number of random names to generate:\n 
ƒ(x)= """))
                    print("\n")
                if math.ldexp(14512, optio) == 29024.0:
                    wr_nmr = input("""Number of random words to generate:\n 
ƒ(x)= """)
                    wr_nmr = int(wr_nmr)
                    print("\n")
            except KeyboardInterrupt:
                sys.exit(1)
        except SystemExit:
            endf()
            sys.exit()
        except:
            print("\n\n\n\n\n\n\n\n")
            print("     unknown input, must be a number")
            print("\n")
            optionss1()




    def endf(): 

        print("""\n\n\n\n\n\n\n\n\n
 /$$$$$$$$/$$                        /$$                       /$$$$$$                       
|__  $$__| $$                       | $$                      /$$__  $$                      
   | $$  | $$$$$$$  /$$$$$$ /$$$$$$$| $$   /$$ /$$$$$$$      | $$  \__/$$$$$$  /$$$$$$       
   | $$  | $$__  $$|____  $| $$__  $| $$  /$$//$$_____/      | $$$$  /$$__  $$/$$__  $$      
   | $$  | $$  \ $$ /$$$$$$| $$  \ $| $$$$$$/|  $$$$$$       | $$_/ | $$  \ $| $$  \__/      
   | $$  | $$  | $$/$$__  $| $$  | $| $$_  $$ \____  $$      | $$   | $$  | $| $$            
   | $$  | $$  | $|  $$$$$$| $$  | $| $$ \  $$/$$$$$$$/      | $$   |  $$$$$$| $$            
   |__/  |__/  |__/\_______|__/  |__|__/  \__|_______/       |__/    \______/|__/            
                                                                                             
                                                                                             
                                                                                             
          /$$                                 /$$                                            
         | $$                                |__/                                            
  /$$$$$$| $$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$$/$$/$$$$$$$  /$$$$$$                           
 /$$_____| $$__  $$/$$__  $$/$$__  $$/$$_____| $| $$__  $$/$$__  $$                          
| $$     | $$  \ $| $$  \ $| $$  \ $|  $$$$$$| $| $$  \ $| $$  \ $$                          
| $$     | $$  | $| $$  | $| $$  | $$\____  $| $| $$  | $| $$  | $$                          
|  $$$$$$| $$  | $|  $$$$$$|  $$$$$$//$$$$$$$| $| $$  | $|  $$$$$$$                          
 \_______|__/  |__/\______/ \______/|_______/|__|__/  |__/\____  $$                          
                                                          /$$  \ $$                          
                                                         |  $$$$$$/                          
                                                          \______/                                           
        \n\n\n         """)                           
        time.sleep(1.14512)
        print("""                                                                                                                           
                                                                                                                            
 /$$   /$$                    /$$                                       /$$       
| $$  | $$                   | $$                                      | $/       
| $$  | $$ /$$$$$$  /$$$$$$$/$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$  /$$$$$|_//$$$$$$$
| $$$$$$$$/$$__  $$/$$_____|_  $$_/  |____  $$/$$__  $$/$$__  $$|____  $$/$$_____/
| $$__  $| $$$$$$$| $$       | $$     /$$$$$$| $$  \__| $$$$$$$$ /$$$$$$|  $$$$$$ 
| $$  | $| $$_____| $$       | $$ /$$/$$__  $| $$     | $$_____//$$__  $$\____  $$
| $$  | $|  $$$$$$|  $$$$$$$ |  $$$$|  $$$$$$| $$     |  $$$$$$|  $$$$$$$/$$$$$$$/
|__/  |__/\_______/\_______/  \___/  \_______|__/      \_______/\_______|_______/ 
                                                                                  
                                                                                  
                                                                                  
                                  /$$                    /$$            
                                 | $$                   | $$            
  /$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$$/$$   /$$ /$$$$$$$/$$$$$$  /$$$$$$$
 /$$__  $$/$$__  $$/$$__  $$/$$__  $| $$  | $$/$$_____|_  $$_/ /$$_____/
| $$  \ $| $$  \__| $$  \ $| $$  | $| $$  | $| $$       | $$  |  $$$$$$ 
| $$  | $| $$     | $$  | $| $$  | $| $$  | $| $$       | $$ /$\____  $$
| $$$$$$$| $$     |  $$$$$$|  $$$$$$|  $$$$$$|  $$$$$$$ |  $$$$/$$$$$$$/
| $$____/|__/      \______/ \_______/\______/ \_______/  \___/|_______/ 
| $$                                                                    
| $$                                                                    
|__/                                                                   \n\n\n\n """)                         
                                    
        time.sleep(1.14512)
        print("""   \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n                                https://github.com/Hectarea?tab=repositories                                                                
                                                                                                                                
        \n\n\n\n\n\n\n\n\n\n """)



    print("\n\n\n\n\n\n\n\n\n\n\n\n\nPress enter to start or CTRL+C to quit at any time")
    print("""  
 /$$$$$$$$                   /$$                                                                          
| $$_____/                  | $$                                                                          
| $$    /$$$$$$   /$$$$$$$ /$$$$$$   /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$                               
| $$$$$|____  $$ /$$_____/|_  $$_/  | $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$                              
| $$__/ /$$$$$$$|  $$$$$$   | $$    | $$  | $$| $$  \ $$| $$$$$$$$| $$  \__/                              
| $$   /$$__  $$ \____  $$  | $$ /$$| $$  | $$| $$  | $$| $$_____/| $$                                    
| $$  |  $$$$$$$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$$$$$$/|  $$$$$$$| $$                                    
|__/   \_______/|_______/    \___/   \____  $$| $$____/  \_______/|__/                                    
                                     /$$  | $$| $$                                                        
                                    |  $$$$$$/| $$                                                        
                                     \______/ |__/                                                        
 /$$                       /$$                             /$$                                            
| $$                      | $$                            | $$                                            
| $$$$$$$  /$$   /$$      | $$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
| $$__  $$| $$  | $$      | $$__  $$ /$$__  $$ /$$_____/|_  $$_/   |____  $$ /$$__  $$ /$$__  $$ |____  $$
| $$  \ $$| $$  | $$      | $$  \ $$| $$$$$$$$| $$        | $$      /$$$$$$$| $$  \__/| $$$$$$$$  /$$$$$$$
| $$  | $$| $$  | $$      | $$  | $$| $$_____/| $$        | $$ /$$ /$$__  $$| $$      | $$_____/ /$$__  $$
| $$$$$$$/|  $$$$$$$      | $$  | $$|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$      |  $$$$$$$|  $$$$$$$
|_______/  \____  $$      |__/  |__/ \_______/ \_______/   \___/   \_______/|__/       \_______/ \_______/
           /$$  | $$                                                                                      
          |  $$$$$$/                                                                                      
           \______/  """)
    input()
    print("""\n\n\n
                                            https://github.com/Hectarea?tab=repositories
                        
                        """)

    print("""Welcome to fastyper by Hectarea
    \n""")

    time.sleep(0.4)


    optionss1()
    try:
        wrn = int(input("""Number of times to repeat:\n 
ƒ(x)= """)) 
        print("\n")
    except KeyboardInterrupt:
        endf()
        sys.exit()
    except:
        print("Input must be a number\n")
        print("\n")
        wrn = int(input("""Number of times to type and send(must be a whole number):\n
ƒ(x)= """))
        print("\n")
        print("\n")
    try:
        if math.ldexp(14512, optio*optio*optio) == 1947767668736.0:
            wr = input("""Phrase or word to type:\n 
ƒ(x)= """)
            print("\n")
        if math.ldexp(14512, optio*optio*optio*optio) == 1.6803747990119326e+81:
            wr = input("""Phrase or word to split and type:\n 
ƒ(x)= """)
            wr = char(wr)
            print("\n")
        
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nClick on the desired chat and press  CTRL+X  to start typing and sending the Keys or press Esc to stop\n\n\n\n\n\n\n\n\n\n")
        act = "yes"
        print("\n")


        if math.ldexp(14512, optio*optio*optio) == 1947767668736.0:
            wr = wrsplit(wr)

        if math.ldexp(14512, optio*optio) == 232192.0:
            wr = grname(nm_nmr)

        if math.ldexp(14512, optio) == 29024.0:
            wr = grwor(wr_nmr)

    except KeyboardInterrupt:


        print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n
 /$$$$$$$$ /$$   /$$ /$$$$$$$ 
| $$_____/| $$$ | $$| $$__  $$
| $$      | $$$$| $$| $$  \ $$
| $$$$$   | $$ $$ $$| $$  | $$
| $$__/   | $$  $$$$| $$  | $$
| $$      | $$\  $$$| $$  | $$
| $$$$$$$$| $$ \  $$| $$$$$$$/
|________/|__/  \__/|_______/ 
                              
                              
                              """)                         
                                    
        time.sleep(1.14512)
        exit()

if args.word != "None":
    wr = str(args.word)
    wr = wrsplit_argparse(wr)
    wrn = int(args.repeat)
    act = "yes"
    print( "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nClick on the desired chat and press  CTRL+X  to start typing and sending the Keys or press Esc to stop\n\n\n\n\n\n\n\n\n\n\n\n\n")

if args.randomwords != "None":
    wr = grwor(int(args.randomwords))
    wrn = int(args.repeat)
    act = "yes"
    print( "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nClick on the desired chat and press  CTRL+X  to start typing and sending the Keys or press Esc to stop\n\n\n\n\n\n\n\n\n\n\n\n\n")

if args.randomnames != "None":
    wr = grname(int(args.randomnames))
    wrn = int(args.repeat)
    act = "yes"
    print( "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nClick on the desired chat and press  CTRL+X  to start typing and sending the Keys or press Esc to stop\n\n\n\n\n\n\n\n\n\n\n\n\n")

while begin == "not yet":
    if emergency_exit == "now":
        sys.exit(0)

if act == "yes":
    if begin == "now":
        send_keys(wrn=wrn, wr=wr)

key = "keys were" 
if len(wr) == 1:
    if wrn == 1:
        key = "key was"


sentk = len(wr)
if wrn != 1:
    sentk = int(len(wr))*wrn
print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n
 /$$$$$$$$ /$$   /$$ /$$$$$$$ 
| $$_____/| $$$ | $$| $$__  $$
| $$      | $$$$| $$| $$  \ $$
| $$$$$   | $$ $$ $$| $$  | $$
| $$__/   | $$  $$$$| $$  | $$
| $$      | $$\  $$$| $$  | $$
| $$$$$$$$| $$ \  $$| $$$$$$$/
|________/|__/  \__/|_______/ 
                        
                        
                        """)    

print(str(sentk) + " " + key + " "+ "succesfully typed and sent \n\n\n")
