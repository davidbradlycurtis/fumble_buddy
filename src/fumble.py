'''
Fumble Buddy

'''

import random
import config

#############
# Functions #
#############

def run():
    '''
    The main method containing fumble logic

    '''

    print('')
    print('Welcome to Fumble Buddy!            ')
    print('1) Get Critical Miss Situation      ')
    print('2) Get Critical Hit Situation       ')
    print('3) Get Random Injury                ')
    print('0) Quit                           ')
    print('')
    user_choice = input('What would you like to do? \n')
    print('')
    while not(user_choice.lower() == 'quit' or user_choice.lower() == 'q' or user_choice == '0'):
        if user_choice == '1':
            if rollDie(10) > 4:
                miss_picker()
            else:
                print(config.NORMAL_MISS)
        elif user_choice == '2':
            if rollDie(10) > 4:
                hit_picker()
            else:
                print(config.NORMAL_HIT)
        elif user_choice == '3':
            injury()
        else:
            print('')
            print('Invalid Input, try again!         ')
        print('')
        print('1) Get Critical Miss Situation      ')
        print('2) Get Critical Hit Situation       ')
        print('3) Get Random Injury                ')
        print('0) (Q)uit                           ')
        print('')
        user_choice = input('What would you like to do? ')
    print('Fubmle Buddy Terminated!        ')
    print('')

def hit_picker():
    print('')
    print('1) (B)ludgeoning                    ')
    print('2) (S)lashing                       ')
    print('3) (P)iercing                       ')
    print('4) Poison                           ')
    print('5) (A)cid                           ')
    print('6) (F)ire                           ')
    print('7) (C)old                           ')
    print('8) (R)adiant                        ')
    print('9) (L)ightning                      ')
    print('10) (T)hunder                       ')
    print('11) Force                           ')
    print('12) (N)ecrotic                      ')
    print('13) Psychic                         ')
    print('')
    damage_type = input('Select damage type:')
    print('')

    if (damage_type == '1' or damage_type.lower() == 'b' or damage_type.lower() == 'bludgeoning'):
        roll = rollDie(100)
        if roll < 45:
            print(config.DISARM_PRONE[listPicker(5)])
        elif roll < 75:
            print(config.ADDITIONAL_DIE)
        elif roll < 90:
            print(config.CRUSHING_BLOW)
        elif roll < 100:
            print(config.BLUDGEONING_FORCE_INJURY[listPicker(11)])
        else:
            print(config.SUPER_CRITICAL)
            print(config.MAJOR_INJURY[7])

    elif (damage_type == '2' or damage_type.lower() == 's' or damage_type.lower() == 'slashing'):
        roll = rollDie(100)
        if roll < 45:
            print(config.DISARM_PRONE[listPicker(5)])
        elif (roll > 44 and roll < 75):
            print(config.ADDITIONAL_DIE)
        elif (roll > 74 and roll < 90):
            print(config.BLEEDING_STRIKE)
        elif roll < 100:
            print(config.SLASHING_NECROTIC_INJURY[listPicker(8)])
        else:
            print(config.SUPER_CRITICAL)
            print(config.CRITICAL_WOUND)

    elif (damage_type == '3' or damage_type.lower() == 'p' or damage_type.lower() == 'piercing'):
        roll = rollDie(100)
        if roll < 45:
            print(config.DISARM_PRONE[listPicker(5)])
        elif (roll > 44 and roll < 75):
            print(config.ADDITIONAL_DIE)
        elif (roll > 74 and roll < 90):
            print(config.PINNING_SHOT)
        elif roll < 100:
            print(config.PIERCING_INJURY[listPicker(7)])
        else:
            print(config.SUPER_CRITICAL)
            print(config.PIERCING_INJURY[2])
            print(config.PIERCING_SHOT)

    elif (damage_type == '4' or damage_type.lower() == 'poison'):
        roll = rollDie(100)
        if roll < 45:
            print(config.NORMAL_HIT)
        elif (roll > 44 and roll < 75):
            print(config.ADDITIONAL_DIE)
        elif (roll > 74 and roll < 90):
            print(config.ALERGIC_REACTION)
        elif roll < 100:
            print(config.POISON_INJURY[listPicker(3)])
        else:
            print(config.SUPER_CRITICAL)
            print(config.SHOCK)

    elif (damage_type == '5' or damage_type.lower() == 'a' or damage_type.lower() == 'acid'):
        roll = rollDie(100)
        if roll < 45:
            print(config.NORMAL_HIT)
        elif roll > 44 and roll < 75:
            print(config.ADDITIONAL_DIE)
        elif (roll > 74 and roll < 90):
            print(config.CORROSION)
        elif roll < 100:
            print(config.ACID_INJURY[listPicker(7)])
        else:
            print(config.SUPER_CRITICAL)
            print(config.ACID_BATH)

    elif (damage_type == '6' or damage_type.lower() == 'f' or damage_type.lower() == 'fire'):
        roll = rollDie(100)
        if roll < 45:
            print(config.NORMAL_HIT)
        elif (roll > 44 and roll < 75):
            print(config.ADDITIONAL_DIE)
        elif (roll > 74 and roll < 90):
            print(config.HOT_FLASH)
        elif roll < 100:
            print(config.FIRE_RADIENT_INJURY[listPicker(6)])
        else:
            print(config.SUPER_CRITICAL)
            print(config.ADDITIONAL_FIRE)

    elif (damage_type == '7' or damage_type.lower() == 'c' or damage_type.lower() == 'cold'):
        roll = rollDie(100)
        if roll < 45:
            print(config.NORMAL_HIT)
        elif (roll > 44 and roll < 75):
            print(config.ADDITIONAL_DIE)
        elif (roll > 74 and roll < 90):
            print(config.REDUCED_MOVEMENT)
        elif roll < 100:
            print(config.COLD_INJURY[listPicker(3)])
        else:
            print(config.SUPER_CRITICAL)
            print(config.FROZEN_SOLID)

    elif (damage_type == '8' or damage_type.lower() == 'r' or damage_type.lower() == 'radiant'):
        roll = rollDie(100)
        if roll < 45:
            print(config.NORMAL_HIT)
        elif (roll > 44 and roll < 75):
            print(config.ADDITIONAL_DIE)
        elif (roll > 74 and roll < 90):
            print(config.BLINDED)
        elif roll < 100:
            print(config.FIRE_RADIENT_INJURY[listPicker(6)])
        else:
            print(config.SUPER_CRITICAL)
            print(config.RIGHTEOUS_MARK)

    elif (damage_type == '9' or damage_type.lower() == 'l' or damage_type.lower() == 'lightning'):
        roll = rollDie(100)
        if roll < 45:
            print(config.NORMAL_HIT)
        elif (roll > 44 and roll < 75):
            print(config.ADDITIONAL_DIE)
            print('')
        elif (roll > 74 and roll < 90):
            print(config.TAZED)
        elif roll < 100:
            print(config.LIGHTNING_INJURY[listPicker(6)])
        else:
            print(config.SUPER_CRITICAL)
            print(config.CHAIN_LIGHTNING)

    elif (damage_type == '10' or damage_type.lower() == 't' or damage_type.lower() == 'thunder'):
        roll = rollDie(100)
        if roll < 45:
            print(config.NORMAL_HIT)
        elif (roll > 44 and roll < 75):
            print(config.ADDITIONAL_DIE)
        elif (roll > 74 and roll < 90):
            print(config.RINGING_EARS)
        elif roll < 100:
            print(config.THUNDER_INJURY[listPicker(1)])
        else:
            print(config.SUPER_CRITICAL)

    elif (damage_type == '11' or damage_type.lower() == 'force'):
        roll = rollDie(100)
        if roll < 45:
            print(config.DISARM_PRONE[listPicker(5)])
        elif (roll > 44 and roll < 75):
            print(config.ADDITIONAL_DIE)
        elif (roll > 74 and roll < 90):
            print(config.CRUSHING_BLOW)
        elif roll < 100:
            print(config.BLUDGEONING_FORCE_INJURY[listPicker(11)])
        else:
            print(config.SUPER_CRITICAL)
            print(config.MAJOR_INJURY[9])

    elif (damage_type == '12' or damage_type.lower() == 'n' or damage_type.lower() == 'necrotic'):
        roll = rollDie(100)
        if roll < 45:
            print(config.NORMAL_HIT)
        elif (roll > 44 and roll < 75):
            print(config.ADDITIONAL_DIE)
        elif (roll > 74 and roll < 90):
            print(config.DECAY)
        elif roll < 100:
            print(config.SLASHING_NECROTIC_INJURY[listPicker(8)])
        else:
            print(config.SUPER_CRITICAL)
            print(config.PUTREFY)

    elif (damage_type == '13' or damage_type.lower() == 'psychic'):
        roll = rollDie(100)
        if roll < 45:
            print(config.NORMAL_HIT)
        elif (roll > 44 and roll < 75):
            print(config.ADDITIONAL_DIE)
        elif (roll > 74 and roll < 90):
            print(config.DOMINATED)
        elif (roll < 100):
            print(config.OVERWHELMED)
        else:
            print(config.SUPER_CRITICAL)
            print(config.SUICIDAL)
    else:
        print('')
        print('Invalid damage type, please try again.')
        print('')
        hit_picker()

def miss_picker():
    print('')
    print('1) (B)ludgeoning, (S)lashing, or (P)iercing')
    print('2) Poison                           ')
    print('3) (A)cid                           ')
    print('4) (F)ire                           ')
    print('5) (C)old                           ')
    print('6) (R)adiant                        ')
    print('7) (L)ightning                      ')
    print('8) (T)hunder                       ')
    print('9) Force                           ')
    print('10) (N)ecrotic                      ')
    print('11) Psychic                         ')
    print('')
    damage_type = input('Select damage type:')
    print('')

    if (damage_type == '1' or damage_type.lower() == 'b' or damage_type.lower() =='bludgeoning' or damage_type == '2' or damage_type.lower() == 's' or damage_type.lower() =='slashing' or damage_type == '3' or damage_type.lower() == 'p' or damage_type.lower() =='piercing'):
        roll = rollDie(100)
        if roll < 45:
            print(config.DISARM_PRONE_MISS[listPicker(5)])
        elif (roll > 44 and roll < 75):
            print(config.RIPOSTE)
        elif (roll > 74 and roll < 90):
            print(config.END_ACTION)
        elif roll < 100:
            print(config.WRONG_TARGET)
        else:
            print(config.SECOND_CHANCE)

    elif (damage_type == '2' or damage_type.lower() == 'poison'):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.COMPROMISED)
        else:
            print(config.SECOND_CHANCE)

    elif (damage_type == '3' or damage_type.lower() == 'a' or damage_type.lower() == 'acid'):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.ACID_BURN)
        else:
            print(config.SECOND_CHANCE)

    elif (damage_type == '4' or damage_type.lower() == 'f' or damage_type.lower() == 'fire'):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.SEVERE_BURNS)
        else:
            print(config.SECOND_CHANCE)

    elif (damage_type == '5' or damage_type.lower() == 'c' or damage_type.lower() == 'cold'):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.COLD_CHILL)
        else:
            print(config.SECOND_CHANCE)

    elif (damage_type == '6' or damage_type.lower() == 'r' or damage_type.lower() == 'radiant'):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.BLESSED)
        else:
            print(config.SECOND_CHANCE)

    elif (damage_type == '7' or damage_type.lower() == 'l' or damage_type.lower() == 'lightning'):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.SHORT_CIRCUIT)
        else:
            print(config.SECOND_CHANCE)

    elif (damage_type == '8' or damage_type.lower() == 't' or damage_type.lower() == 'thunder'):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.UNWANTED_SOUND)
        else:
            print(config.SECOND_CHANCE)

    elif (damage_type == '9' or damage_type.lower() == 'force'):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.REDIRECTED)
        else:
            print(config.SECOND_CHANCE)

    elif (damage_type == '10' or damage_type.lower() == 'n' or damage_type.lower() == 'necrotic'):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.CONTAMINATED)
        else:
            print(config.SECOND_CHANCE)

    elif (damage_type == '11' or damage_type.lower() == 'psychic'):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.IN_YOUR_HEAD)
        else:
            print(config.SECOND_CHANCE)
    else:
        print('')
        print('Invalid damage type, please try again.')
        print('')
        miss_picker()

def injury():
    print('')
    print('Injury Severity                     ')
    print('1) (M)inor injury                   ')
    print('2) (S)evere injury                  ')
    print('')
    injuryType = input('Select a minor or severe injury: ')
    print('')

    if (injuryType.lower() == 'minor' or injuryType.lower() == 'm' or injuryType == '1'):
        print(config.MINOR_INJURY[listPicker(12)])
    elif (injuryType.lower() == 'severe' or injuryType.lower() == 's' or injuryType == '2'):
        print(config.MAJOR_INJURY[listPicker(11)])
    else:
        print('')
        print('Invalid input, please try again')
        injury()

def rollDie(die):
    return random.randint(1, die)

def listPicker(count):
    return random.randint(0, count)

#############
#   Body    #
#############
run()
