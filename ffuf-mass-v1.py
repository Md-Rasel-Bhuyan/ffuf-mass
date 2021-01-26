import os
import sys, time

version = 'v1.0'
contact = "Contact with me in FB> https://www.facebook.com/InF3R10R"
site = 'list urls should be contain urls like this format https://site.com/'

def loading():
    print("Coded By Md Rasel..Please Wait it is Loading...")
    for i in range(0, 100):
        time.sleep(0.0015)
        width = (i + 1) / 4
        bar = "[" + "-+-" * width + " " * (25 - width) + "]"
        sys.stdout.write(u"\u001b[1000D" +  bar)
        sys.stdout.flush()
    
loading()

print('\n'
r'''                       

  ______ ______ _    _ ______   __  __           _____ _____     
 |  ____|  ____| |  | |  ____| |  \/  |   /\    / ____/ ____| --------------- 
 | |__  | |__  | |  | | |__    | \  / |  /  \  | (___| (___                -
 |  __| |  __| | |  | |  __|   | |\/| | / /\ \  \___ \\___ \    ^_^       -
 | |    | |    | |__| | |      | |  | |/ ____ \ ____) |___) |            -
 |_|    |_|     \____/|_|      |_|  |_/_/    \_\_____/_____/            -
                                                                V1.0   -                                                         
-----------------------------------------------------------------------

  ____          _____                _        __   ___  
 |  _ \        |  __ \              | |      /_ | / _ \ 
 | |_) |_   _  | |__) |__ _ ___  ___| | __   _| || | | |
 |  _ <| | | | |  _  // _` / __|/ _ \ | \ \ / / || | | |
 | |_) | |_| | | | \ \ (_| \__ \  __/ |  \ V /| || |_| |
 |____/ \__, | |_|  \_\__,_|___/\___|_|   \_/ |_(_)___/ 
         __/ |                                          
        |___/                                           
    +++++++++++++++++ Welome Boss..Give Me File I Will Run Mass FFUF For You+++++++++++++++
        ================Modifying The Code Won't Make You Coder=======================
            ++++++++++++++++ Thanks For Using This Script+++++++++++++++++++++++++
                 ---------------- ./Md Rasel ------------------
                     ######## We Are ~ErrOr SquaD~ #########

        ''')
print(version)
print(contact)
print(site)

if os.path.isfile('command.txt') == True:
  a = raw_input("Please Enter The Site List> ")
  b = open(a, "r")
  read = b.readlines()
  out = 0
  auto = open('command.txt').readline()
  for line in read:
    out += 1
    if 'http://' not in line and 'https://' not in line:
        line = 'http://'+line
    line = line+'FUZZ'    
    test = line
    j = "".join(test.splitlines())
    mix = auto%(j,out)
    fire = "".join(mix.splitlines())
    print(fire)
    os.system(fire)
else:
  k = raw_input("Please Enter The Site List>")
  print("FFUF Will Run Default Mood")
  word = raw_input("Give Me The Wordlist Full Path>")
  print(word)  
  l = open(k, "r")
  rid = l.readlines()
  o = 0
  for line in rid:
    o += 1
    if 'http://' not in line and 'https://' not in line:
      line = 'http://'+line
    line = line+'FUZZ'    
    test = line
    j = "".join(test.splitlines())
    #print(j)
    com = "ffuf -u %s -w %s -of html -o %s.html"%(j,word,o)
    go = "".join(com.splitlines())
    os.system(go)
print('\n'
r'''  
  _____                     ____                
 |  __ \                   |  _ \               
 | |  | | ___  _ __   ___  | |_) | ___  ___ ___ 
 | |  | |/ _ \| '_ \ / _ \ |  _ < / _ \/ __/ __|
 | |__| | (_) | | | |  __/ | |_) | (_) \__ \__ \
 |_____/ \___/|_| |_|\___| |____/ \___/|___/___/
                                                ''')   
