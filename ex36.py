# --coding:utf-8--
from sys import exit

def start():
    print """
    help~ help ~ princess  is takend by the monster
    what would you do?
    1.recure her
    2.ignore her
    """
    choice = raw_input('>')

    if choice == '1':
        monster_room()
    elif choice == '2':
        print "coward!go home and fuck your self"
        exit(0)
    else :
        print "I don't know what's your mean"

def monster_room():
    print """
    the moster is sleeping,it is perfect time to attack!
    DO you want hit him?
    """
    choice = raw_input('>')

    if choice == "yes":
        print "the monster is dead and left a mustory box ,do you want open it?"
        mystory_box()
    elif choice == "no":
        print "you are a good man, but you alredy dead"
        exit(0)
    else:
        print "I don't know what's your mean"


def mystory_box():
    choice = raw_input('>')

    if choice == "yes":
        for part in ["weapon","armor","shose"]:
            print "you get a new %s"%part
        print "now,you have the power to defeat the drogon and save the princess"
        drogon_room ()
    elif choice == "no"or"No":
        print "stupid,you are dead man already!"
        exit(0)
    else :
        print "I don't know what's your mean"

def drogon_room():
    print """
    the drogon is show up,you need hit his point! or you will be die
    face?cock? where would you want to hit?
    hit him with your new weapon as soon as possible!
    """
    while True:
        choice = raw_input('>')

        if choice == "face":
            print "the drogon is throw up a fire ball ,and you are burned"
        elif choice == "cock":
            print "Good job!the drogon is dead and you save the princess!"
            exit(0)
        else :
            print "I don't know what's your mean"
start()
