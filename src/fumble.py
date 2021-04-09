'''
Fumble Buddy

'''
import argparse
import random
import config

#############
# Argparser #
#############
parser = argparse.ArgumentParser(description='Fumble Buddy! Execute this script to randomly determine critical miss/hits automatically.')

subparsers = parser.add_subparsers(dest='command')
parser_hit = subparsers.add_parser('hit', help='generate a critical hit situation')
hit_group = parser_hit.add_mutually_exclusive_group(required=True)
hit_group.add_argument('-b', action='store_true', required=False, help='bludgeoning damage')
hit_group.add_argument('-s', action='store_true', required=False, help='slashing damage')
hit_group.add_argument('-p', action='store_true', required=False, help='piercing damage')
hit_group.add_argument('-poison', required=False, action='store_true', help='poison damage')
hit_group.add_argument('-a', action='store_true', required=False, help='acid damage')
hit_group.add_argument('-f', action='store_true', required=False, help='fire damage')
hit_group.add_argument('-c', action='store_true', required=False, help='cold damage')
hit_group.add_argument('-r', action='store_true', required=False, help='radiant damage')
hit_group.add_argument('-l', action='store_true', required=False, help='lightning damage')
hit_group.add_argument('-t', action='store_true', required=False, help='thunder damage')
hit_group.add_argument('-force', action='store_true', required=False, help='force damage')
hit_group.add_argument('-n', action='store_true', required=False, help='necrotic damage')
hit_group.add_argument('-psychic', action='store_true', required=False, help='psychic damage')

parser_miss = subparsers.add_parser('miss', help='generate a critical miss situation')
miss_group = parser_miss.add_mutually_exclusive_group(required=True)
miss_group.add_argument('-b', action='store_true', required=False, help='bludgeoning damage')
miss_group.add_argument('-s', action='store_true', required=False, help='slashing damage')
miss_group.add_argument('-p', action='store_true', required=False, help='piercing damage')
miss_group.add_argument('-poison', required=False, action='store_true', help='poison damage')
miss_group.add_argument('-a', action='store_true', required=False, help='acid damage')
miss_group.add_argument('-f', action='store_true', required=False, help='fire damage')
miss_group.add_argument('-c', action='store_true', required=False, help='cold damage')
miss_group.add_argument('-r', action='store_true', required=False, help='radiant damage')
miss_group.add_argument('-l', action='store_true', required=False, help='lightning damage')
miss_group.add_argument('-t', action='store_true', required=False, help='thunder damage')
miss_group.add_argument('-force', action='store_true', required=False, help='force damage')
miss_group.add_argument('-n', action='store_true', required=False, help='necrotic damage')
miss_group.add_argument('-psychic', action='store_true', required=False, help='psychic damage')

parser_injury = subparsers.add_parser('injury', help='generate a random injury')
injury_group = parser_injury.add_mutually_exclusive_group(required=True)
injury_group.add_argument('-m', action='store_true', required=False, help='minor injury')
injury_group.add_argument('-s', action='store_true', required=False, help='sever injury')

parser.add_argument('--repeat', type=int, default=None, help='number of situations to generate')

args = parser.parse_args()

#############
# Functions #
#############

def repeat(fun, args):
    [fun(args) for _ in range(args.repeat)]

def hit_picker(args):
    if (args.b):
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

    elif (args.s):
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

    elif (args.p):
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

    elif (args.poison):
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

    elif (args.a):
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

    elif (args.f):
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

    elif (args.c):
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

    elif (args.r):
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

    elif (args.l):
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

    elif (args.t):
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

    elif (args.force):
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

    elif (args.n):
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

    elif (args.psychic):
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

def miss_picker(args):
    if (args.p or args.s or args.b):
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

    elif (args.poison):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.COMPROMISED)
        else:
            print(config.SECOND_CHANCE)

    elif (args.a):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.ACID_BURN)
        else:
            print(config.SECOND_CHANCE)

    elif (args.f):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.SEVERE_BURNS)
        else:
            print(config.SECOND_CHANCE)

    elif (args.c):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.COLD_CHILL)
        else:
            print(config.SECOND_CHANCE)

    elif (args.r):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.BLESSED)
        else:
            print(config.SECOND_CHANCE)

    elif (args.l):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.SHORT_CIRCUIT)
        else:
            print(config.SECOND_CHANCE)

    elif (args.t):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.UNWANTED_SOUND)
        else:
            print(config.SECOND_CHANCE)

    elif (args.force):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.REDIRECTED)
        else:
            print(config.SECOND_CHANCE)

    elif (args.n):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.CONTAMINATED)
        else:
            print(config.SECOND_CHANCE)

    elif (args.psychic):
        roll = rollDie(10)
        if roll < 6:
            print(config.END_ACTION)
        elif roll < 10:
            print(config.IN_YOUR_HEAD)
        else:
            print(config.SECOND_CHANCE)

def injury(args):
    if (args.m):
        print(config.MINOR_INJURY[listPicker(12)])
    elif (args.s):
        print(config.MAJOR_INJURY[listPicker(11)])

def rollDie(die):
    return random.randint(1, die)

def listPicker(count):
    return random.randint(0, count)

def run(args):
    '''
    The main method containing fumble logic

    '''
    if args.command == 'miss':
        if args.repeat:
            repeat(miss_picker, args)
        elif rollDie(10) > 4:
            miss_picker(args)
        else:
            print(config.NORMAL_MISS)
    elif args.command == 'hit':
        if args.repeat:
            repeat(hit_picker, args)
        elif rollDie(10) > 4:
            hit_picker(args)
        else:
            print(config.NORMAL_HIT)
    elif args.command == 'injury':
        if args.repeat:
            repeat(injury, args)
        else:
            injury(args)

#############
#   Body    #
#############
run(args)
