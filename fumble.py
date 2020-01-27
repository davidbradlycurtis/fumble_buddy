###########
# Imports #
###########
import random

##########################
# Scenarios and Outcomes #
##########################

#############
# Functions #
#############
def start_fn():
    print("")
    print("        Welcome to Fumble Buddy!            ")
    print("        1) Get Critical Miss Situation      ")
    print("        2) Get Critical Hit Situation       ")
    print("        0) (Q)uit                           ")
    print("")

    userChoice = input("What would you like to do?")
    if (userChoice == "1"):
        criticalMiss()
    elif (userChoice == "2"):
        criticalHit
    elif (userChoice.lower() == "q" or userChoice.lower == "quit" or userChoice == "0"):
        terminate
    else :
        print("")
        print("        Invalid Input        ")
        print("")

def criticalMiss():
    return 0

def criticalHit():
    return 0

def terminate():
    return 0


#############
#   Body    #
#############
start_fn()