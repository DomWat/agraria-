# name: Dominic Waters
# date: 09/09/2020
# description: Text based fantasy game in python3 

# so you can use random functions and time functions 
import random
import time 

# how users might respond 
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
answer_yes = ["Yes", "yes", "y", "Y"]
answer_no = ["No", "no", "n", "N"]

# inventory
items = ["weapon", "health potion", "mana potion", "monney"]
item_count = [0, 0, 0, 0]
inventory = zip(items, item_count)
print(list(inventory))

# character
user = [150, 80, 12, 15, 13] 
def attack_a(): 
    for agi in range(2):
        if agi >= 10:
            chance = random.randint(0,20)
            if chance > 15:
                print("CRITICAL")
            elif chance > 8:
                print("success! Nice strike.")
            else:
                print("You missed.")
        else:
            print("The enemey is too strong!")

def attack_b(): 
    for agi in range(2):
        if agi > 11:
            chance = random.randint(0,20)
            if chance > 17:
                print("CRITICAL")
            elif chance > 10:
                print("success! Nice strike.")
            else:
                print("You missed.")
        else:
            print("The enemey is too strong!")


def intro():
    print("Welcome to Agraria, a land of magic and dragons.")
    print("It's also a land of war and destruction where the many races fight and kill for supremecy")
    print("and survival.")
    print()
    time.sleep(3)
    print("Five races live on the two continents of Agraria.")
    time.sleep(4)
    print("Elves, the long lived race with great access to magic but with a fear and hatred of the other races.")
    time.sleep(4)
    print("The Dwarves a hearty race with strength that rivals many larger than them, but with no access to magic.")
    time.sleep(4)
    print("The Demons, a similar race to the Elves who naturally take to magic, and the Dwarves with a strength that is greater than their size.")
    time.sleep(5)
    print("The Humans, the most populas of races with a gift for weapons but also a gift for cruelty and hatred.")
    time.sleep(5.5)
    print("The last of the races are called The Hated, monsters that have been corrupted by magic and have a gift of intellect above other monsters and a gift for the dark magic that allows them to feed and attack the other races.")
    print()
    time.sleep(4.5)
    print("After five hundred years of war, peace has fallen on the races of Agraria.")
    time.sleep(3)
    print("However, peace never lasts.")
time.sleep(2)

def choose_race():
    race = ""
    while race != "human": # and race != "dwarf" and race != "elf" and race != "demon":
        race = input("Which race will you choose? (human ): ") #, dwarf, elf, or demon): ")
    return race    
time.sleep(2)

def choose_gender():
    gender = ""
    while gender != "male" and gender != "female":
        gender = input("Choose your gender. (male, female): ")
    return gender
time.sleep(2)

def choose_job():
    job = ""
    while job != "warrior" and job != "archer" and job != "mage" and job != "cleric":
        job = input("Choose your initial job. (warrior: high strength and defense, archer: high agility and dexterity, mage: high dark magic and magic defense, cleric: high light magic and magic defense: ")
    return job
time.sleep(2)

def ch1_1():
    time.sleep(2)
    print("Chapter 1: The fall of the Elves!")
    time.sleep(2)
    if user_gender == "male":
        print("You awaken in the barracks as a royal guardsman")
    else:
        print("You awaken in the barracks as a royal guardswoman")
    print("The sound of bells and screaming awaken you.")
    time.sleep(2)
    print()
    print(""" 
    A. Grab your weapon and run into the hallway. 
    B. Lie down and go back to sleep. Can't be that important.
    C. Wait in the room and see what happens. """)
    option = input(">>> ")
    if option in answer_A:

        option_fight()
    elif option in answer_B:
        print("\nEnemy soldiers burst into your room and attack you while you lay in bed. \n\nYou died!")
        ch1_1()
    elif option in answer_C:
        print("You hear screaming and realize city is being attacked. You grab your weapon")
        print("\nAfter waiting multiple soldiers barge into the room and quickly overwhelm you. \n\n You Died!")
        ch1_1()
    else:
        print("Required: A, B, or C")
        ch1_1()

time.sleep(2)   
def option_fight():
    print()
    print("You enter the hallway and see people runninng and being chased by The Hated")
    print("You see two large monsters standing on two feet coming towards you with wands in their hannds.")
    print("One of the enemy mages begins chanting and you can see magic glyphs shining in the air")
    print("""
    A. Charge towards the mage and attack him with your sword.
    B. Run down the hallway and try to escape.
    C. Retreat to safety inside of your room. """)
    option = input(">>> ")
    if option in answer_A:
        option_attack_mage()
    elif option in answer_B:
        option_run()
    elif option in answer_C:
        print("As you escape into your room the door blows inside with a ball of fire.")
        print("\n The two mages enter your room their wands glowing with magic as fire shoots at you. \n\n You die.")
        option_fight()
    else:
        print("required: A, B, or C")
        option_fight()

time.sleep(2)
print()
def option_attack_mage():
    print("You charge towards the mage with your sword in hand.")
    print("""
    A. Run him through with your sword.
    B. Cut off his arm holding the wand. """)
    option = input(">>> ")
    if option in answer_A:
        attack_a()
    elif option in answer_B:
        attack_b()
    else:
        print("required: A or B")
        option_attack_mage()

time.sleep(2)
def option_run():
    print("You run as fast as you can down the hall.")
    print("Just as you are about to reach the corner you feel the impact of scorching heat on your back")
    print("No matter how fast you ran the mage's fire could not be escaped. \n\n You Died!")
    option_fight()

   

intro()
user_race = choose_race()
user_gender = choose_gender()
user_initial_job = choose_job()
ch1_1()
#option_fight()
#option_wait()
user_bio = [user_race, user_gender, user_initial_job]
