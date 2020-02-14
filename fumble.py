###########
# Imports #
###########
import random

##########################
# Scenarios and Outcomes #
##########################

injuries = [
    "Lose an Eye.\n>>>You have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>Magic such as the regenerate spell can restore the lost eye.\n>>>If you have no eyes left after sustaining this injury, you are blinded.",
    "Lose an Arm or a Hand.\n>>>You can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>Magic such as the regenerate spell can restore the lost appendage",
    "Lose a Foot or Leg.\n>>>Your walking speed is halved and you must use a cane or crutch to move unless you have a peg leg or other prosthesis.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>Magic such as the regenerate spell can restore the lost appendage",
    "Lose an Ear.\n>>>You have disadvantage on Charisma (Persuasion) checks and Wisdom (Perception) checks that rely on hearing.\n>>>You have advantage on Charisma (Intimidation) checks.\n>>>Magic such as the regenerate spell can restore the lost ear.",
    "Lose Nose.\n>>>You have disadvantage on Charisma (Persuasion) checks and Wisdom (Perception) checks that rely on smell.\nYou have advantage on Charisma (Intimidation) checks.\nMagic such as the regenerate spell can restore the lost nose.",
    "Blurred Vision.\n>>>You have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting.",
    "Broken Arm or Hand.\n>>>You can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the bone with a DC 15 Wisdom (Medicine) check and you spend thirty days doing nothing but resting.",
    "Broken Foot or Leg.\n>>>Your walking speed is halved and you must use a cane or crutch to move.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the bone with a DC 15 Wisdom (Medicine) check and you spend thirty days doing nothing but resting.",
    "Ringing Ears.\n>>>You have disadvantage on Wisdom (Perception) checks that rely on hearing.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting.",
    "Limp.\n>>>Your walking speed is reduced by 5 feet.\n>>>You must make a DC 10 Dexterity saving throw after using the Dash action.\n>>>If you fail the save, you fall prone.\n>>>Magical healing removes the limp.",
    "Lose a Finger.\n>>>You have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves' tools) using the hand with which you lost the finger.\n>>>Magic such as the regenerate spell can restore the lost finger.\n>>>If you lose all the fingers from one hand, then it functions as if you had lost a hand.",
    "Break a Finger.\n>>>You have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves tools) using the hand with the broken finger.\nThe injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the finger with a DC 10 Wisdom (Medicine) check and you spend ten days doing nothing but resting.",
    "Break an Item.\n>>>A randomly determined nonmagical item you hold, wear, or carry on your person is broken or ruined.\n>>>Roll a d10. On a roll of 1, the item broken is a weapon, on a roll of 2 the item is armor or a shield, and on a roll of 3-10 it is an item that's not a shield or weapon.",
    "Teeth Knocked Out.\n>>>You have disadvantage on Charisma (Persuasion) checks.\n>>>When you cast a spell with a verbal component there is a 25% chance the spell will not work.\n>>>If the spell fails, you still used your action to try to cast it, but the spell did not use any slots or material components.\n>>>The injury heals if you receive magical healing.",
    "Festering Wound.\n>>>Your hit point maximum is reduced by 1 every 24 hours the wound persists.\n>>>If your hit point maximum drops to 0, you die.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every 24 hours.\n>>>After ten success, the injury heals.",
    "Open Wound.\n>>>You lose 1 hit point every hour the wound persists.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every hour.\n>>>After ten success, the injury heals.",
    "Skull Fracture.\n>>>Whenever you attempt an action in combat, you must make a DC 20 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing or if you spend thirty days doing nothing but resting.",
    "Punctured Lung.\n>>>You can take either an action or a bonus action or your turn, but not both.\n>>>The injury heals if you receive magical healing.\n>>>If you puncture both lungs your hit points drop to 0 and you immediately begin dying.",
    "Internal Injury.\n>>>Whenever you attempt an action in combat, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing or if you spend ten days doing nothing but resting.",
    "Broken Ribs.\n>>>Whenever you attempt an action in combat, you must make a DC 10 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing or if you spend ten days doing nothing but resting.",
    "Horrible Scar.\n>>>You have disadvantage on Charisma (Persuasion) checks and advantage on Charisma (Intimidation) checks.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the injury.",
    "Painful Scar.\n>>>You have a scar which gets painful whenever it rains, sleets, hails, or snows.\n>>>Whenever you attempt an action in combat and your scar is giving you pain, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing.",
    "Minor Scar.\n>>>The scar doesn't have any adverse effect, but chicks dig it.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the scar.",
]

minor_miss = [
    "Disarmed!\n>>>Enemy is able to work the players weapon free, dropping it 5ft away.",
    "Disarmed!\n>>>Enemy is able to work the players weapon free, dropping it 10ft away.",
    "Disarmed!\n>>>Enemy is able to work the players weapon free, dropping it 15ft away.",
    "Knocked Prone!\n>>>Player gets off balance, enemy knocks them prone.",
    "Knocked Prone!\n>>>Player gets off balance, enemy knocks them prone.",
    "Knocked Prone!\n>>>Player gets off balance, enemy knocks them prone.",
]

major_miss = [
    "Riposte!\n>>>Enemy can use reaction to counter attack.",
    "Advantage!\n>>>Enemy gets advantage on next attack on that player."
]

#############
# Functions #
#############
def start_fn():
    print("")
    print("Welcome to Fumble Buddy!            ")
    print("1) Get Critical Miss Situation      ")
    print("2) Get Critical Hit Situation       ")
    print("3) Get Random Injury                ")
    print("0) (Q)uit                           ")
    print("")

    userChoice = input("What would you like to do? ")
    print("")
    if (userChoice == "1"):
        criticalMiss()
        start_fn()
    elif (userChoice == "2"):
        criticalHit()
        start_fn()
    elif (userChoice == "3"):
        injury()
        start_fn()
    elif (userChoice.lower() == "q" or userChoice.lower == "quit" or userChoice == "0"):
        print("Fubmle Buddy Terminated!        ")
        print("")
    else :
        print("")
        print("Invalid Input, try again!         ")
        print("")
        start_fn()
    

def criticalMiss():
    roll = random.randint(1, 100)
    if (roll >= 65):
        print("Nothing happens....") 
    elif (roll <= 65 and roll > 50):
        print("Player ends their action.")
    elif (roll < 65 and roll > 1):
        missPicker() 
    else :
        print("Player falls on their own weapon, their hp is reduced to 0.")

def criticalHit():
    return 0  

def missPicker():
    roll = rollDie(100) 
    if (roll >= 50): #They either fall down or are disarmed
        print(minor_miss[random.randint(0, 5)])
    elif (roll < 50 and roll > 25): #Opponent gets advantage/reaction
        print(major_miss[random.randint(0,1)])
    elif (roll <= 25) : 
        injury()        

def injury():
    roll = rollDie(100)
    if (roll <= 10):
        print(injuries[random.randint(0, 4)])
    else :
        print(injuries[random.randint(5, 22)])

def rollDie(die):
    return random.randint(1, die)



#############
#   Body    #
#############
start_fn()