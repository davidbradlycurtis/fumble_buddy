###########
# Imports #
###########
import random

##########################
# Scenarios and Outcomes #
##########################

major_injury = [ 
    "Lose an Eye.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>Magic such as the regenerate spell can restore the lost eye.\n>>>If you have no eyes left after sustaining this injury, you are blinded.",
    "Lose an Arm or a Hand.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>Magic such as the regenerate spell can restore the lost appendage",
    "Lose a Foot or Leg.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move unless you have a peg leg or other prosthesis.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>Magic such as the regenerate spell can restore the lost appendage",
    "Lose an Ear.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and Wisdom (Perception) checks that rely on hearing.\n>>>You have advantage on Charisma (Intimidation) checks.\n>>>Magic such as the regenerate spell can restore the lost ear.",
    "Lose Nose.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and Wisdom (Perception) checks that rely on smell.\nYou have advantage on Charisma (Intimidation) checks.\nMagic such as the regenerate spell can restore the lost nose.",
    "Lose a Finger.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves' tools) using the hand with which you lost the finger.\n>>>Magic such as the regenerate spell can restore the lost finger.\n>>>If you lose all the fingers from one hand, then it functions as if you had lost a hand.",
    "Open Wound.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you lose 1 hit point every hour the wound persists.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every hour.\n>>>After ten success, the injury heals.",
    "Skull Fracture.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 13 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing or if you spend thirty days doing nothing but resting.",
    "Punctured Lung.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you can take either an action or a bonus action or your turn, but not both.\n>>>The injury heals if you receive magical healing.\n>>>If you puncture both lungs your hit points drop to 0 and you immediately begin dying.",
    "Broken Ribs.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 10 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing or if you spend ten days doing nothing but resting.",
    "Painful Scar.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have a scar which gets painful whenever it rains, sleets, hails, or snows.\n>>>Whenever you attempt an action in combat and your scar is giving you pain, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing."
]

minor_injury = [
    "Blurred Vision.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting.",
    "Broken Arm or Hand.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the bone with a DC 15 Wisdom (Medicine) check and you spend thirty days doing nothing but resting.",
    "Broken Foot or Leg.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the bone with a DC 15 Wisdom (Medicine) check and you spend thirty days doing nothing but resting.",
    "Ringing Ears.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on hearing.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting.",
    "Limp.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is reduced by 5 feet.\n>>>You must make a DC 10 Dexterity saving throw after using the Dash action.\n>>>If you fail the save, you fall prone.\n>>>Magical healing removes the limp.",
    "Break a Finger.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves tools) using the hand with the broken finger.\nThe injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the finger with a DC 10 Wisdom (Medicine) check and you spend ten days doing nothing but resting.",
    "Break an Item.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, a randomly determined nonmagical item you hold, wear, or carry on your person is broken or ruined.\n>>>Roll a d10. On a roll of 1, the item broken is a weapon, on a roll of 2 the item is armor or a shield, and on a roll of 3-10 it is an item that's not a shield or weapon.",
    "Teeth Knocked Out.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks.\n>>>When you cast a spell with a verbal component there is a 25% chance the spell will not work.\n>>>If the spell fails, you still used your action to try to cast it, but the spell did not use any slots or material components.\n>>>The injury heals if you receive magical healing.",
    "Festering Wound.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your hit point maximum is reduced by 1 every 24 hours the wound persists.\n>>>If your hit point maximum drops to 0, you die.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every 24 hours.\n>>>After ten success, the injury heals.",
    "Internal Injury.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 10 Constitution saving throw.\n>>>On a failed save, you lose your action until the start of your next turn.\n>>>The injury heals if you receive magical healing or if you spend ten days doing nothing but resting.",
    "Horrible Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and advantage on Charisma (Intimidation) checks.\n>>>Magical healing of 3rd level or higher removes the injury.",
    "Minor Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, the scar doesn't have any adverse effect, but chicks dig it.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the scar."
]

#Injuries for critical hit Bludgeoning/Force attacks
binjury = [
    "Broken Ribs.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 10 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing or if you spend ten days doing nothing but resting.",
    "Skull Fracture.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 13 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing or if you spend thirty days doing nothing but resting.",
    "Lose Nose.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and Wisdom (Perception) checks that rely on smell.\nYou have advantage on Charisma (Intimidation) checks.\nMagic such as the regenerate spell can restore the lost nose.",
    "Teeth Knocked Out.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks.\n>>>When you cast a spell with a verbal component there is a 25% chance the spell will not work.\n>>>If the spell fails, you still used your action to try to cast it, but the spell did not use any slots or material components.\n>>>The injury heals if you receive magical healing.",
    "Blurred Vision.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting.",
    "Broken Arm or Hand.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the bone with a DC 15 Wisdom (Medicine) check and you spend thirty days doing nothing but resting.",
    "Broken Foot or Leg.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the bone with a DC 15 Wisdom (Medicine) check and you spend thirty days doing nothing but resting.",
    "Kneecapping.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move.\n>>>You fall prone after using the Dash action, and on the initial hit.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the bone with a DC 15 Wisdom (Medicine) check and you spend thirty days doing nothing but resting.",
    "Ringing Ears.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on hearing.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting.",
    "Limp.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is reduced by 5 feet.\n>>>You must make a DC 10 Dexterity saving throw after using the Dash action.\n>>>If you fail the save, you fall prone.\n>>>Magical healing removes the limp.",
    "Break a Finger.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves tools) using the hand with the broken finger.\nThe injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the finger with a DC 10 Wisdom (Medicine) check and you spend ten days doing nothing but resting.",
    "Break an Item.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, a randomly determined nonmagical item you hold, wear, or carry on your person is broken or ruined.\n>>>Roll a d10. On a roll of 1, the item broken is a weapon, on a roll of 2 the item is armor or a shield, and on a roll of 3-10 it is an item that's not a shield or weapon."
]

#Injuries for critical hit Slashing/Necrotic attacks
sinjury = [
    "Lose an Eye.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>Magic such as the regenerate spell can restore the lost eye.\n>>>If you have no eyes left after sustaining this injury, you are blinded.",
    "Lose an Arm or a Hand.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>Magic such as the regenerate spell can restore the lost appendage",
    "Lose a Foot or Leg.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move unless you have a peg leg or other prosthesis.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>Magic such as the regenerate spell can restore the lost appendage",
    "Lose a Finger.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves' tools) using the hand with which you lost the finger.\n>>>Magic such as the regenerate spell can restore the lost finger.\n>>>If you lose all the fingers from one hand, then it functions as if you had lost a hand.",
    "Limp.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is reduced by 5 feet.\n>>>You must make a DC 10 Dexterity saving throw after using the Dash action.\n>>>If you fail the save, you fall prone.\n>>>Magical healing removes the limp.",
    "Open Wound.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you lose 1 hit point every hour the wound persists.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every hour.\n>>>After ten success, the injury heals.",
    "Painful Scar.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have a scar which gets painful whenever it rains, sleets, hails, or snows.\n>>>Whenever you attempt an action in combat and your scar is giving you pain, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing.",
    "Horrible Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and advantage on Charisma (Intimidation) checks.\n>>>Magical healing of 3rd level or higher removes the injury.",
    "Minor Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, the scar doesn't have any adverse effect, but chicks dig it.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the scar."
]

#Injuries for critical hit Piercing attacks
pinjury = [
    "Lose an Eye.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>Magic such as the regenerate spell can restore the lost eye.\n>>>If you have no eyes left after sustaining this injury, you are blinded.",
    "Open Wound.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you lose 1 hit point every hour the wound persists.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every hour.\n>>>After ten success, the injury heals.",
    "Punctured Lung.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you can take either an action or a bonus action or your turn, but not both.\n>>>The injury heals if you receive magical healing.\n>>>If you puncture both lungs your hit points drop to 0 and you immediately begin dying.",
    "Painful Scar.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have a scar which gets painful whenever it rains, sleets, hails, or snows.\n>>>Whenever you attempt an action in combat and your scar is giving you pain, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing.",
    "Limp.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is reduced by 5 feet.\n>>>You must make a DC 10 Dexterity saving throw after using the Dash action.\n>>>If you fail the save, you fall prone.\n>>>Magical healing removes the limp.",
    "Festering Wound.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your hit point maximum is reduced by 1 every 24 hours the wound persists.\n>>>If your hit point maximum drops to 0, you die.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every 24 hours.\n>>>After ten success, the injury heals.",
    "Horrible Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and advantage on Charisma (Intimidation) checks.\n>>>Magical healing of 3rd level or higher removes the injury.",
    "Minor Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, the scar doesn't have any adverse effect, but chicks dig it.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the scar.",
]

#Injuries for critical hit Poison attacks
poison_injury = [
    "Internal Injury.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 10 Constitution saving throw.\n>>>On a failed save, you lose your action until the start of your next turn.\n>>>The condition ends if you receive magical healing or if you spend ten days doing nothing but resting.",
    "Disoriented.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 10 Constitution saving throw.\n>>>On a failed save, you lose your action until the start of your next turn.\n>>>The condition ends if you receive magical healing or if you spend ten days doing nothing but resting.",
    "Paralized.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, a randomly determined limb becomes paralized.\n>>>The limb returns to normal if you receive magical healing or poison effect ends.",
    "Blinded.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>The condition ends if you receive magical healing or if you spend ten days doing nothing but resting."
]

#Injuries for critical hit Acid attacks
ainjury = [
    "Lose an Eye.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>Magic such as the regenerate spell can restore the lost eye.\n>>>If you have no eyes left after sustaining this injury, you are blinded.",
    "Lose an Arm or a Hand.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>Magic such as the regenerate spell can restore the lost appendage",
    "Lose a Foot or Leg.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move unless you have a peg leg or other prosthesis.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>Magic such as the regenerate spell can restore the lost appendage",
    "Lose an Ear.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and Wisdom (Perception) checks that rely on hearing.\n>>>You have advantage on Charisma (Intimidation) checks.\n>>>Magic such as the regenerate spell can restore the lost ear.",
    "Lose Nose.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and Wisdom (Perception) checks that rely on smell.\nYou have advantage on Charisma (Intimidation) checks.\nMagic such as the regenerate spell can restore the lost nose.",
    "Lose a Finger.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves' tools) using the hand with which you lost the finger.\n>>>Magic such as the regenerate spell can restore the lost finger.\n>>>If you lose all the fingers from one hand, then it functions as if you had lost a hand.",
    "Open Wound.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you lose 1 hit point every hour the wound persists.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every hour.\n>>>After ten success, the injury heals.",
    "Painful Scar.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have a scar which gets painful whenever it rains, sleets, hails, or snows.\n>>>Whenever you attempt an action in combat and your scar is giving you pain, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing.",
    "Horrible Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and advantage on Charisma (Intimidation) checks.\n>>>Magical healing of 3rd level or higher removes the injury.",
    "Break an Item.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, a randomly determined nonmagical item you hold, wear, or carry on your person is broken or ruined.\n>>>Roll a d10. On a roll of 1, the item broken is a weapon, on a roll of 2 the item is armor or a shield, and on a roll of 3-10 it is an item that's not a shield or weapon.",
    "Minor Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, the scar doesn't have any adverse effect, but chicks dig it.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the scar."
]

#Injuries for critical hit Fire/Radient attacks
frinjury = [
    "Burned Arm or Hand.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone applies bandages to the burn with a DC 15 Wisdom (Medicine) check and you spend fifteen days doing nothing but resting.",
    "Burned Foot or Leg.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone applies bandages to the burn with a DC 15 Wisdom (Medicine) check and you spend fifteen days doing nothing but resting.",
    "Burn a Finger.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves tools) using the hand with the broken finger.\nThe injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone tends to the finger with a DC 10 Wisdom (Medicine) check and you spend ten days doing nothing but resting.",
    "Burned Item.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, a randomly determined nonmagical item you hold, wear, or carry on your person is broken or ruined.\n>>>Roll a d10. On a roll of 1, the item broken is a weapon, on a roll of 2 the item is armor or a shield, and on a roll of 3-10 it is an item that's not a shield or weapon.",
    "Painful Scar.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have a scar which gets painful whenever it rains, sleets, hails, or snows.\n>>>Whenever you attempt an action in combat and your scar is giving you pain, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing.",
    "Horrible Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and advantage on Charisma (Intimidation) checks.\n>>>Magical healing of 3rd level or higher removes the injury.",
    "Minor Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, the scar doesn't have any adverse effect, but chicks dig it.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the scar."
]

#Injuries for critical hit Cold attacks
cinjury = [
    "Frozen Arm or Hand.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone applies bandages to the burn with a DC 15 Wisdom (Medicine) check and you spend fifteen days doing nothing but resting.",
    "Frozen Foot or Leg.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone applies bandages to the burn with a DC 15 Wisdom (Medicine) check and you spend fifteen days doing nothing but resting.",
    "Frozen Finger.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves tools) using the hand with the broken finger.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone tends to the finger with a DC 10 Wisdom (Medicine) check and you spend ten days doing nothing but resting.",
    "Reduced Movement Speed\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your movement speed is halfed.\n>>>The condition ends if you receive magical healing.\n>>>Alternatively, the condition ends after spending at least ten minutes around a fire or after a short or long rest."
]

#Injuries for critical hit Lightning attacks
linjury = [
    "Painful Scar.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have a scar which gets painful whenever it rains, sleets, hails, or snows.\n>>>Whenever you attempt an action in combat and your scar is giving you pain, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing.",
    "Horrible Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and advantage on Charisma (Intimidation) checks.\n>>>Magical healing of 3rd level or higher removes the injury.",
    "Minor Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, the scar doesn't have any adverse effect, but chicks dig it.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the scar.",
    "Ringing Ears.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on hearing.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting.",
    "Bite Tongue. \n>>>Make a constitution saving throw DC: 11\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks.\n>>>When you cast a spell with a verbal component there is a 1d4 chance the spell will not work.\n>>>If the spell fails, you still used your action to try to cast it, but the spell did not use any slots or material components.\n>>>The injury heals if you receive magical healing, or complete a short or long rest.",
    "Muscle Contractions.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you experience severe muscle contractions paralizing you dropping you prone.\n>>>The contractions end after one round."
]

#Injuries for critical hit Thunder attacks
thunder_injury = [
    "Disoriented.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 10 Constitution saving throw.\n>>>On a failed save, you lose your action until the start of your next turn.\n>>>The condition ends if you receive magical healing or if you spend ten days doing nothing but resting.",
    "Ringing Ears.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on hearing.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting."
]

#Disarm/knocked prone situations
dp = [
    "Disarmed!\n>>>Enemy is disarmed, throwing there weapon 5 feet away in a random direction.",
    "Disarmed!\n>>>Enemy is disarmed, throwing there weapon 10 feet away in a random direction.",
    "Disarmed!\n>>>Enemy is disarmed, throwing there weapon 15 feet away in a random direction.",
    "Knocked Prone!\n>>>Enemy is knocked prone.",
    "Knocked Prone!\n>>>Enemy is knocked prone.",
    "Knocked Prone!\n>>>Enemy is knocked prone."
]

additionalDie = "Devistating Critical!\n>>>Spend one hit die to add an additional damage die to the damage."

#############
# Functions #
#############

def start_fn():
    print("")
    print("Welcome to Fumble Buddy!            ")
    print("1) Get Critical Miss Situation      ")
    print("2) Get Critical Hit Situation       ")
    print("3) Get Random Injury                ")
    print("0) Quit                           ")
    print("")
    userChoice = input("What would you like to do? ")
    print("")
    while not(userChoice.lower() == "quit" or userChoice.lower() == 'q' or userChoice == "0"):
        if (userChoice == "1"):
            if (rollDie(10) > 4):
                missPicker()
            else :
                print("")
                print("Normal Critical Miss...")
                print("")
        elif (userChoice == "2"):
            if (rollDie(10) > 4):
                hitPicker()
            else :
                print("")
                print("Normal Critical Hit...")
                print("")
        elif (userChoice == "3"):
            injury()
        else :
            print("")
            print("Invalid Input, try again!         ")
        print("")
        print("1) Get Critical Miss Situation      ")
        print("2) Get Critical Hit Situation       ")
        print("3) Get Random Injury                ")
        print("0) (Q)uit                           ")
        print("")
        userChoice = input("What would you like to do? ")
    print("Fubmle Buddy Terminated!        ")
    print("")

def hitPicker():
    print("")
    print("1) (B)ludgeoning                    ")
    print("2) (S)lashing                       ")
    print("3) (P)iercing                       ")
    print("4) Poison                           ")
    print("5) (A)cid                           ")
    print("6) (F)ire                           ")
    print("7) (C)old                           ")
    print("8) (R)adiant                        ")
    print("9) (L)ightning                      ")
    print("10) (T)hunder                       ")
    print("11) Force                           ")
    print("12) (N)ecrotic                      ")
    print("13) Psychic                         ")
    print("")
    damageType = input("Select damage type:")
    print("")

    if (damageType == "1" or damageType.lower() == "b" or damageType.lower() =="bludgeoning"):
        roll = rollDie(100)
        if (roll < 45):         #Disarms enemy or knocks them prone
            print(dp[listPicker(5)])
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Special Trait
            print("Crushing Blow!\n>>>If the target is wielding a nonmagical shield, the shield is broken.\n>>If the target is not wielding a shield, their weapon is destroyed instead.")
            print("")
        elif (roll < 100):          #Injury
            print(binjury[listPicker(11)])
            print("")
        else :      #Super Critical!
            print("SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following injury:")
            print("")
            print(major_injury[7])
            print("")
    elif (damageType == "2" or damageType.lower() == "s" or damageType.lower() =="slashing"):
        roll = rollDie(100)
        if (roll < 45):         #Disarms enemy or knocks them prone
            print(dp[listPicker(5)])
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Special Trait
            print("Bleeding Strike!\n>>>Target takes 1d4 bleading damage each round for one minute.\n>>>Alternatively, the bleeding stops after a Medicine check DC:12.")
            print("")
        elif (roll < 100):          #Injury
            print(sinjury[listPicker(8)])
            print("")
        else :              #Super Critical!
            print("SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following effect:")
            print("")
            print("Critical Wound. \n>>>Target's max hp is reduced 1d8 each round until the wound is treated with magical healing, or after a Medicine check DC:14.")
    elif (damageType == "3" or damageType.lower() == "p" or damageType.lower() =="piercing"):
        roll = rollDie(100)
        if (roll < 45):         #Disarms enemy or knocks them prone
            print(dp[listPicker(5)])
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Special Trait
            print("Pinning Shot!\n>>>Target is pinned to either the ground or wall by the projectile or spear.\n>>>The target is restrained until they use an action to pull themselves free, Strength check DC:13.")
            print("")
        elif (roll < 100):          #Injury
            print(pinjury[listPicker(7)])
            print("")
        else :          #Super Critical!
            print("SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following effect:")
            print("")
            print(pinjury[2])
            print("")
            print("Piercing Strike!\n>>>Creatures behind the target up to 10 feet take half damage.")
            print("")
    elif (damageType == "4" or damageType.lower() =="poison"):
        roll = rollDie(100)
        if (roll < 45):         #Nothing happens
            print("")
            print("Normal Critical Hit...")
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Special Trait
            print("Alergic Reaction!\n>>>Movement speed is halfed for the duration of the poison condition.")
            print("")
        elif (roll < 100):          #Injury
            print(poison_injury[listPicker(3)])
            print("")
        else :              #Super Critical!
            print("SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following effect:")
            print("")
            print("Anaphylactic Shock. \n>>>Target breaks out in hives and massive swelling starts all over their body.\n>>>For the duration of the poison condition, the target is sufficating, blinded, and deafened.")
    elif (damageType == "5" or damageType.lower() == "a" or damageType.lower() =="acid"):
        roll = rollDie(100)
        if (roll < 45):         #Nothing happens
            print("")
            print("Normal Critical Hit...")
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Special Trait
            print("Corrosion!\n>>>Any nonmagical weapon made of metal or wood that the target is holding corrodes.\n>>>The weapon takes a permanent and cumulative −1 penalty to damage rolls.\n>>>If its penalty drops to −5, the weapon is destroyed.")
            print("")
        elif (roll < 100):          #Injury
            print(ainjury[listPicker(7)])
            print("")
        else :          #Super Critical!
            print("SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following effect:")
            print("")
            print("Acid bath!\n>>>If the target is wearing armor, the armor is destroyed (if non-magical) or rendered useless until cleaned during a long rest (if magical).\n>>>If the creature is not wearing armor, add an additional damage die.")
            print("")
    elif (damageType == "6" or damageType.lower() == "f" or damageType.lower() =="fire"):
        roll = rollDie(100)
        if (roll < 45):         #Nothing happens
            print("")
            print("Normal Critical Hit...")
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Special Trait
            print("Hot flash!\n>>>Target catches on fire.\n>>>While the target is on fire it takes 2d4 fire damage at the start of each of its turns.\n>>>The target can end this condition by dropping prone and using 5 feet of movement to roll on the ground.")
            print("")
        elif (roll < 100):          #Injury
            print(frinjury[listPicker(6)])
            print("")
        else :                      #Super Critical!
            print("SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following effect:")
            print("")
            print("Additionally, the target is on fire.\n>>>While the creature is on fire it takes 2d8 fire damage at the start of each of its turns.\n>>>The target can end this condition by dropping prone and using 5 feet of movement to roll on the ground.")
            print("")
    elif (damageType == "7" or damageType.lower() == "c" or damageType.lower() =="cold"):
        roll = rollDie(100)
        if (roll < 45):         #Nothing happens
            print("")
            print("Normal Critical Hit...")
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Special Trait
            print("Reduced Movement Speed!\n>>>Movement speed is halfed.\n>>>The condition ends if the target receives magical healing.\n>>>Alternatively, the condition ends after spending at least ten minutes around a fire or after a short or long rest.")
            print("")
        elif (roll < 100):          #Injury
            print(crinjury[listPicker(3)])
            print("")
        else :                      #Super Critical!
            print("SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following effect:")
            print("")
            print("Frozen solid!\n>>>The target is frozen in place and is paralyzed for 1 minute.\n>>>The target can make a Constitution saving throw DC: 15 each round to end the condition.")
            print("")
    elif (damageType == "8" or damageType.lower() == "r" or damageType.lower() =="radiant"):
        roll = rollDie(100)
        if (roll < 45):         #Nothing happens
            print("")
            print("Normal Critical Hit...")
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Special Trait
            print("Blinded!\n>>>Target has disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>The condition ends after 12 seconds, or if they receive magical healing.")
            print("")
        elif (roll < 100):          #Injury
            print(frinjury[listPicker(6)])
            print("")
        else :                      #Super Critical!
            print("SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following effect:")
            print("")
            print("Righteous mark!\n>>>The target glows for the next minute.\n>>>While glowing it produces bright light up to 10 feet and dim light up to 30 feet.\n>>>All successful attacks against the creature deal an additional 1d6 radiant damage.")
            print("")
    elif (damageType == "9" or damageType.lower() == "l" or damageType.lower() =="lightning"):
        roll = rollDie(100)
        if (roll < 45):         #Nothing happens
            print("")
            print("Normal Critical Hit...")
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Special Trait
            print("Tazed!\n>>>Target's speed is reduced to 0 and they cannot take the attack action until their next turn.")
            print("")
        elif (roll < 100):          #Injury
            print(linjury[listPicker(6)])
            print("")
        else :                      #Super Critical!
            print("SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following effect:")
            print("")
            print("Chain Lightning!\n>>>Three bolts then leap from that target to as many as three other Targets, each of which must be within 30 feet of the first target.\n>>>A target can be a creature or an object and can be targeted by only one of the bolts.\n>>>A target must make a Dexterity saving throw.\n>>>The target takes full lightning damage on a failed save, or half as much on a successful one.")
            print("")
    elif (damageType == "10" or damageType.lower() == "t" or damageType.lower() =="thunder"):
        roll = rollDie(100)
        if (roll < 45):         #Nothing happens
            print("")
            print("Normal Critical Hit...")
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Special Trait
            print("Ringing Ears!\n>>>Target has disadvantage on Wisdom (Perception) checks that rely on hearing.\n>>>The condition ends if you receive magical healing.\n>>>Alternatively, the condidtion ends after 1 minute.")
            print("")
        elif (roll < 100):          #Injury
            print(thunder_injury[listPicker(1)])
            print("")
        else :                      #Super Critical!
            print("SUPER CRITICAL!!!\n>>>Add an additional damage die and deal maximum critical damage.")
            print("")
    elif (damageType == "11" or damageType.lower() =="force"):
        roll = rollDie(100)
        if (roll < 45):         #Disarms enemy or knocks them prone
            print(dp[listPicker(5)])
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Special Trait
            print("Crushing Blow!\n>>>If the target is wielding a nonmagical shield, the shield is broken.\n>>If the target is not wielding a shield, their weapon is destroyed instead.")
            print("")
        elif (roll < 100):          #Injury
            print(binjury[listPicker(11)])
            print("")
        else :      #Super Critical!
            print("SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following injury:")
            print("")
            print(major_injury[9])
            print("")
    elif (damageType == "12" or damageType.lower() == "n" or damageType.lower() =="necrotic"):
        roll = rollDie(100)
        if (roll < 45):         #Normal Critical
            print("")
            print("Normal Critical Hit...")
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Special trait
            print("Decay!\n>>>Damage from this attack reduces the target's maximum hit points by the same amount.\n>>>The target cannot regain hit points for the next minute.\n>>>It may make a Constitution saving throw DC: 16 at the end of each of its turns to end this effect.")
            print("")
        elif (roll < 100):          #Injury
            print(sinjury[listPicker(8)])
            print("")
        else :          #Super Critical!
            print("SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following effect:")
            print("")
            print("Putrefy!\n>>>Target is dropped prone and has their movement reduced to 0.\n>>>The target cannot regain hit points until the end of this condition.\n>>>This condition heals if they receive magical healing or after a long rest.")
            print("")
    elif (damageType == "13" or damageType.lower() =="psychic"):
        roll = rollDie(100)
        if (roll < 45):         #Normal Critical
            print("")
            print("Normal Critical Hit...")
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Domination
            print("Dominated!\n>>>Attacker controls the target for their next turn.")
            print("")
        elif (roll < 100):          #Overwhelmed
            print("Overwhelmed!\n>>>If the target does not have immunity or resistance to psychic damage, they gain vulnerability to psychic damage.\n>>>If they have resistance to psychic damage, they lose it.\n>>>If they have immunity to psychic damage, they lose it but gain resistance to psychic damage.")
        else :
            print("SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following effect:")
            print("")
            print("Suicidal!\n>>>At the beginning each of the target's turn, they must pass a Wisdom saving throw DC: 12 or make an attempt to end their own life.")
            print("")
    else:
        print("")
        print("Invalid damage type, please try again.")
        print("")
        hitPicker()

def missPicker():
    print("")
    print("1) (B)ludgeoning, (S)lashing, or (P)iercing")
    print("2) Poison                           ")
    print("3) (A)cid                           ")
    print("4) (F)ire                           ")
    print("5) (C)old                           ")
    print("6) (R)adiant                        ")
    print("7) (L)ightning                      ")
    print("8) (T)hunder                       ")
    print("9) Force                           ")
    print("10) (N)ecrotic                      ")
    print("11) Psychic                         ")
    print("")
    damageType = input("Select damage type:")
    print("")

    if (damageType == "1" or damageType.lower() == "b" or damageType.lower() =="bludgeoning" or damageType == "2" or damageType.lower() == "s" or damageType.lower() =="slashing" or damageType == "3" or damageType.lower() == "p" or damageType.lower() =="piercing"):
        roll = rollDie(100)
        if (roll < 45):         #
            pass
        elif (roll > 44 and roll < 75):         #
            pass
        elif (roll > 74 and roll < 90):         #
            pass
        elif (roll < 100):          #
            injury()
        else :
            print("Player gets another chance, re-roll attack!")
            print("")
    elif (damageType == "2" or damageType.lower() =="poison"):
        roll = rollDie(100)
        if (roll < 45):         #
            pass
        elif (roll > 44 and roll < 75):         #
            pass
        elif (roll > 74 and roll < 90):         #
            pass
        elif (roll < 100):          #
            injury()
        else :
            print("Player gets another chance, re-roll attack!")
            print("")
    elif (damageType == "3" or damageType.lower() == "a" or damageType.lower() =="acid"):
        roll = rollDie(100)
        if (roll < 45):         #
            pass
        elif (roll > 44 and roll < 75):         #
            pass
        elif (roll > 74 and roll < 90):         #
            pass
        elif (roll < 100):          #
            injury()
        else :
            print("Player gets another chance, re-roll attack!")
            print("")
    elif (damageType == "4" or damageType.lower() == "f" or damageType.lower() =="fire"):
        roll = rollDie(100)
        if (roll < 45):         #
            pass
        elif (roll > 44 and roll < 75):         #
            pass
        elif (roll > 74 and roll < 90):         #
            pass
        elif (roll < 100):          #
            injury()
        else :
            print("Player gets another chance, re-roll attack!")
            print("")
    elif (damageType == "5" or damageType.lower() == "c" or damageType.lower() =="cold"):
        roll = rollDie(100)
        if (roll < 45):         #
            pass
        elif (roll > 44 and roll < 75):         #
            pass
        elif (roll > 74 and roll < 90):         #
            pass
        elif (roll < 100):          #
            injury()
        else :
            print("Player gets another chance, re-roll attack!")
            print("")
    elif (damageType == "6" or damageType.lower() == "r" or damageType.lower() =="radiant"):
        roll = rollDie(100)
        if (roll < 45):         #
            pass
        elif (roll > 44 and roll < 75):         #
            pass
        elif (roll > 74 and roll < 90):         #
            pass
        elif (roll < 100):          #
            injury()
        else :
            print("Player gets another chance, re-roll attack!")
            print("")
    elif (damageType == "7" or damageType.lower() == "l" or damageType.lower() =="lightning"):
        roll = rollDie(100)
        if (roll < 45):         #
            pass
        elif (roll > 44 and roll < 75):         #
            pass
        elif (roll > 74 and roll < 90):         #
            pass
        elif (roll < 100):          #
            injury()
        else :
            print("Player gets another chance, re-roll attack!")
            print("")
    elif (damageType == "8" or damageType.lower() == "t" or damageType.lower() =="thunder"):
        roll = rollDie(100)
        if (roll < 45):         #
            pass
        elif (roll > 44 and roll < 75):         #
            pass
        elif (roll > 74 and roll < 90):         #
            pass
        elif (roll < 100):          #
            injury()
        else :
            print("Player gets another chance, re-roll attack!")
            print("")
    elif (damageType == "9" or damageType.lower() =="force"):
        roll = rollDie(100)
        if (roll < 45):         #Disarms enemy or knocks them prone
            print(dp[listPicker(5)])
            print("")
        elif (roll > 44 and roll < 75):         #Adds another damage die (Costs 1 hit die)
            print(additionalDie)
            print("")
        elif (roll > 74 and roll < 90):         #Special Trait
            print("Crushing Blow!\n>>>If the target is wielding a nonmagical shield, the shield is broken.\n>>If the target is not wielding a shield, their weapon is destroyed instead.")
            print("")
        elif (roll < 100):          #Injury
            print(binjury[listPicker(11)])
            print("")
        else :      #Super Critical!
            print("SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following injury:")
            print("")
            print(major_injury[7])
            print("")
    elif (damageType == "10" or damageType.lower() == "n" or damageType.lower() =="necrotic"):
        roll = rollDie(100)
        if (roll < 45):         #
            pass
        elif (roll > 44 and roll < 75):         #
            pass
        elif (roll > 74 and roll < 90):         #
            pass
        elif (roll < 100):          #
            injury()
        else :
            print("Player gets another chance, re-roll attack!")
            print("")
    elif (damageType == "11" or damageType.lower() =="psychic"):
        roll = rollDie(100)
        if (roll < 45):         #
            pass
        elif (roll > 44 and roll < 75):         #
            pass
        elif (roll > 74 and roll < 90):         #
            pass
        elif (roll < 100):          #
            injury()
        else :
            print("Player gets another chance, re-roll attack!")
            print("")
    else:
        print("")
        print("Invalid damage type, please try again.")
        print("")
        missPicker()

def injury():
    print("")
    print("Injury Severity                     ")
    print("1) (M)inor injury                   ")
    print("2) (S)evere injury                  ")
    print("")
    injuryType = input("Select a minor or severe injury: ")
    print("")

    if (injuryType.lower() == "minor" or injuryType.lower() == "m" or injuryType == "1" ):
        print(minor_injury[listPicker(12)])
    elif (injuryType.lower() == "severe" or injuryType.lower() == "s" or injuryType == "2"):
        print(major_injury[listPicker(11)])
    else :
        print("")
        print("Invalid input, please try again")
        injury()

def rollDie(die):
    return random.randint(1, die)

def listPicker(count):
    return random.randint(0, count)

#############
#   Body    #
#############
start_fn()