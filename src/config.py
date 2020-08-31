'''
Config file containing scenarios and outcomes
'''

# pylint: disable=line-too-long

MAJOR_INJURY = [
    'Lose an Eye.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>Magic such as the regenerate spell can restore the lost eye.\n>>>If you have no eyes left after sustaining this injury, you are blinded.\n',
    'Lose an Arm or a Hand.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>Magic such as the regenerate spell can restore the lost appendage\n',
    'Lose a Foot or Leg.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move unless you have a peg leg or other prosthesis.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>Magic such as the regenerate spell can restore the lost appendage.\n',
    'Lose an Ear.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and Wisdom (Perception) checks that rely on hearing.\n>>>You have advantage on Charisma (Intimidation) checks.\n>>>Magic such as the regenerate spell can restore the lost ear.\n',
    'Lose Nose.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and Wisdom (Perception) checks that rely on smell.\nYou have advantage on Charisma (Intimidation) checks.\nMagic such as the regenerate spell can restore the lost nose.\n',
    "Lose a Finger.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves' tools) using the hand with which you lost the finger.\n>>>Magic such as the regenerate spell can restore the lost finger.\n>>>If you lose all the fingers from one hand, then it functions as if you had lost a hand.\n",
    'Open Wound.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you lose 1 hit point every hour the wound persists.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every hour.\n>>>After ten success, the injury heals.\n',
    "Skull Fracture.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 13 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing or if you spend thirty days doing nothing but resting.\n",
    'Punctured Lung.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you can take either an action or a bonus action or your turn, but not both.\n>>>The injury heals if you receive magical healing.\n>>>If you puncture both lungs your hit points drop to 0 and you immediately begin dying.\n',
    "Broken Ribs.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 10 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing or if you spend ten days doing nothing but resting.\n",
    "Painful Scar.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have a scar which gets painful whenever it rains, sleets, hails, or snows.\n>>>Whenever you attempt an action in combat and your scar is giving you pain, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing.\n"
]

MINOR_INJURY = [
    'Blurred Vision.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting.',
    'Broken Arm or Hand.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the bone with a DC 15 Wisdom (Medicine) check and you spend thirty days doing nothing but resting.',
    'Broken Foot or Leg.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the bone with a DC 15 Wisdom (Medicine) check and you spend thirty days doing nothing but resting.',
    'Ringing Ears.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on hearing.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting.',
    'Limp.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is reduced by 5 feet.\n>>>You must make a DC 10 Dexterity saving throw after using the Dash action.\n>>>If you fail the save, you fall prone.\n>>>Magical healing removes the limp.',
    'Break a Finger.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves tools) using the hand with the broken finger.\nThe injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the finger with a DC 10 Wisdom (Medicine) check and you spend ten days doing nothing but resting.',
    "Break an Item.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, a randomly determined nonmagical item you hold, wear, or carry on your person is broken or ruined.\n>>>Roll a d10. On a roll of 1, the item broken is a weapon, on a roll of 2 the item is armor or a shield, and on a roll of 3-10 it is an item that's not a shield or weapon.",
    'Teeth Knocked Out.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks.\n>>>When you cast a spell with a verbal component there is a 25% chance the spell will not work.\n>>>If the spell fails, you still used your action to try to cast it, but the spell did not use any slots or material components.\n>>>The injury heals if you receive magical healing.',
    'Festering Wound.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your hit point maximum is reduced by 1 every 24 hours the wound persists.\n>>>If your hit point maximum drops to 0, you die.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every 24 hours.\n>>>After ten success, the injury heals.',
    'Internal Injury.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 10 Constitution saving throw.\n>>>On a failed save, you lose your action until the start of your next turn.\n>>>The injury heals if you receive magical healing or if you spend ten days doing nothing but resting.',
    'Horrible Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and advantage on Charisma (Intimidation) checks.\n>>>Magical healing of 3rd level or higher removes the injury.',
    "Minor Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, the scar doesn't have any adverse effect, but chicks dig it.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the scar."
]

BLUDGEONING_FORCE_INJURY = [
    "Broken Ribs.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 10 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing or if you spend ten days doing nothing but resting.\n",
    "Skull Fracture.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 13 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing or if you spend thirty days doing nothing but resting.\n",
    'Lose Nose.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and Wisdom (Perception) checks that rely on smell.\nYou have advantage on Charisma (Intimidation) checks.\nMagic such as the regenerate spell can restore the lost nose.\n',
    'Teeth Knocked Out.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks.\n>>>When you cast a spell with a verbal component there is a 25% chance the spell will not work.\n>>>If the spell fails, you still used your action to try to cast it, but the spell did not use any slots or material components.\n>>>The injury heals if you receive magical healing.\n',
    'Blurred Vision.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting.\n',
    'Broken Arm or Hand.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the bone with a DC 15 Wisdom (Medicine) check and you spend thirty days doing nothing but resting.\n',
    'Broken Foot or Leg.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the bone with a DC 15 Wisdom (Medicine) check and you spend thirty days doing nothing but resting.\n',
    'Kneecapping.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move.\n>>>You fall prone after using the Dash action, and on the initial hit.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the bone with a DC 15 Wisdom (Medicine) check and you spend thirty days doing nothing but resting.\n',
    'Ringing Ears.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on hearing.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting.\n',
    'Limp.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is reduced by 5 feet.\n>>>You must make a DC 10 Dexterity saving throw after using the Dash action.\n>>>If you fail the save, you fall prone.\n>>>Magical healing removes the limp.\n',
    'Break a Finger.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves tools) using the hand with the broken finger.\nThe injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone sets the finger with a DC 10 Wisdom (Medicine) check and you spend ten days doing nothing but resting.\n',
    "Break an Item.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, a randomly determined nonmagical item you hold, wear, or carry on your person is broken or ruined.\n>>>Roll a d10. On a roll of 1, the item broken is a weapon, on a roll of 2 the item is armor or a shield, and on a roll of 3-10 it is an item that's not a shield or weapon.\n"
]

CRUSHING_BLOW = 'Crushing Blow!\n>>>If the target is wielding a nonmagical shield, the shield is broken.\n>>If the target is not wielding a shield, their weapon is destroyed instead.\n'

SLASHING_NECROTIC_INJURY = [
    'Lose an Eye.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>Magic such as the regenerate spell can restore the lost eye.\n>>>If you have no eyes left after sustaining this injury, you are blinded.\n',
    'Lose an Arm or a Hand.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>Magic such as the regenerate spell can restore the lost appendage.\n',
    'Lose a Foot or Leg.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move unless you have a peg leg or other prosthesis.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>Magic such as the regenerate spell can restore the lost appendage.\n',
    "Lose a Finger.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves' tools) using the hand with which you lost the finger.\n>>>Magic such as the regenerate spell can restore the lost finger.\n>>>If you lose all the fingers from one hand, then it functions as if you had lost a hand.\n",
    'Limp.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is reduced by 5 feet.\n>>>You must make a DC 10 Dexterity saving throw after using the Dash action.\n>>>If you fail the save, you fall prone.\n>>>Magical healing removes the limp.\n',
    'Open Wound.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you lose 1 hit point every hour the wound persists.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every hour.\n>>>After ten success, the injury heals.\n',
    "Painful Scar.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have a scar which gets painful whenever it rains, sleets, hails, or snows.\n>>>Whenever you attempt an action in combat and your scar is giving you pain, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing.\n",
    'Horrible Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and advantage on Charisma (Intimidation) checks.\n>>>Magical healing of 3rd level or higher removes the injury.\n',
    "Minor Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, the scar doesn't have any adverse effect, but chicks dig it.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the scar.\n"
]

BLEEDING_STRIKE = 'Bleeding Strike!\n>>>Target takes 1d4 bleading damage each round for one minute.\n>>>Alternatively, the bleeding stops after a Medicine check DC:12.\n'

CRITICAL_WOUND = "Critical Wound. \n>>>Target's max hp is reduced 1d8 each round until the wound is treated with magical healing, or after a Medicine check DC:14.\n"

PIERCING_INJURY = [
    'Lose an Eye.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>Magic such as the regenerate spell can restore the lost eye.\n>>>If you have no eyes left after sustaining this injury, you are blinded.\n',
    'Open Wound.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you lose 1 hit point every hour the wound persists.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every hour.\n>>>After ten success, the injury heals.\n',
    'Punctured Lung.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you can take either an action or a bonus action or your turn, but not both.\n>>>The injury heals if you receive magical healing.\n>>>If you puncture both lungs your hit points drop to 0 and you immediately begin dying.\n',
    "Painful Scar.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have a scar which gets painful whenever it rains, sleets, hails, or snows.\n>>>Whenever you attempt an action in combat and your scar is giving you pain, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing.\n",
    'Limp.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is reduced by 5 feet.\n>>>You must make a DC 10 Dexterity saving throw after using the Dash action.\n>>>If you fail the save, you fall prone.\n>>>Magical healing removes the limp.\n',
    'Festering Wound.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your hit point maximum is reduced by 1 every 24 hours the wound persists.\n>>>If your hit point maximum drops to 0, you die.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every 24 hours.\n>>>After ten success, the injury heals.\n',
    'Horrible Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and advantage on Charisma (Intimidation) checks.\n>>>Magical healing of 3rd level or higher removes the injury.\n',
    "Minor Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, the scar doesn't have any adverse effect, but chicks dig it.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the scar.\n",
]

PINNING_SHOT = 'Pinning Shot!\n>>>Target is pinned to either the ground or wall by the projectile or spear.\n>>>The target is restrained until they use an action to pull themselves free, Strength check DC:13.\n'

PIERCING_SHOT = 'Piercing Strike!\n>>>Creatures behind the target up to 10 feet take half damage.\n'

POISON_INJURY = [
    'Internal Injury.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 10 Constitution saving throw.\n>>>On a failed save, you lose your action until the start of your next turn.\n>>>The condition ends if you receive magical healing or if you spend ten days doing nothing but resting.\n',
    'Disoriented.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 10 Constitution saving throw.\n>>>On a failed save, you lose your action until the start of your next turn.\n>>>The condition ends if you receive magical healing or if you spend ten days doing nothing but resting.\n',
    'Paralized.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, a randomly determined limb becomes paralized.\n>>>The limb returns to normal if you receive magical healing or poison effect ends.\n',
    'Blinded.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>The condition ends if you receive magical healing or if you spend ten days doing nothing but resting.\n'
]

ALERGIC_REACTION = 'Alergic Reaction!\n>>>Movement speed is halfed for the duration of the poison condition.\n'

SHOCK = 'Anaphylactic Shock. \n>>>Target breaks out in hives and massive swelling starts all over their body.\n>>>For the duration of the poison condition, the target is sufficating, blinded, and deafened.\n'

ACID_INJURY = [
    'Lose an Eye.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>Magic such as the regenerate spell can restore the lost eye.\n>>>If you have no eyes left after sustaining this injury, you are blinded.\n',
    'Lose an Arm or a Hand.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>Magic such as the regenerate spell can restore the lost appendage\n',
    'Lose a Foot or Leg.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move unless you have a peg leg or other prosthesis.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>Magic such as the regenerate spell can restore the lost appendage\n',
    'Lose an Ear.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and Wisdom (Perception) checks that rely on hearing.\n>>>You have advantage on Charisma (Intimidation) checks.\n>>>Magic such as the regenerate spell can restore the lost ear.\n',
    'Lose Nose.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and Wisdom (Perception) checks that rely on smell.\nYou have advantage on Charisma (Intimidation) checks.\nMagic such as the regenerate spell can restore the lost nose.\n',
    "Lose a Finger.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves' tools) using the hand with which you lost the finger.\n>>>Magic such as the regenerate spell can restore the lost finger.\n>>>If you lose all the fingers from one hand, then it functions as if you had lost a hand.\n",
    'Open Wound.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you lose 1 hit point every hour the wound persists.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, someone can tend to the wound and make a DC 15 Wisdom (Medicine) check once every hour.\n>>>After ten success, the injury heals.\n',
    "Painful Scar.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have a scar which gets painful whenever it rains, sleets, hails, or snows.\n>>>Whenever you attempt an action in combat and your scar is giving you pain, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing.\n",
    'Horrible Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and advantage on Charisma (Intimidation) checks.\n>>>Magical healing of 3rd level or higher removes the injury.\n',
    "Break an Item.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, a randomly determined nonmagical item you hold, wear, or carry on your person is broken or ruined.\n>>>Roll a d10. On a roll of 1, the item broken is a weapon, on a roll of 2 the item is armor or a shield, and on a roll of 3-10 it is an item that's not a shield or weapon.\n",
    "Minor Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, the scar doesn't have any adverse effect, but chicks dig it.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the scar.\n"
]

CORROSION = 'Corrosion!\n>>>Any nonmagical weapon made of metal or wood that the target is holding corrodes.\n>>>The weapon takes a permanent and cumulative −1 penalty to damage rolls.\n>>>If its penalty drops to −5, the weapon is destroyed.\n'

ACID_BATH = 'Acid bath!\n>>>If the target is wearing armor, the armor is destroyed (if non-magical) or rendered useless until cleaned during a long rest (if magical).\n>>>If the creature is not wearing armor, add an additional damage die.\n'

ACID_BURN = 'Acid Burn!\n>>>Player must suffer the effects of their own acid attack.\n'

FIRE_RADIENT_INJURY = [
    'Burned Arm or Hand.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone applies bandages to the burn with a DC 15 Wisdom (Medicine) check and you spend fifteen days doing nothing but resting.\n',
    'Burned Foot or Leg.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone applies bandages to the burn with a DC 15 Wisdom (Medicine) check and you spend fifteen days doing nothing but resting.\n',
    'Burn a Finger.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves tools) using the hand with the broken finger.\nThe injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone tends to the finger with a DC 10 Wisdom (Medicine) check and you spend ten days doing nothing but resting.\n',
    "Burned Item.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, a randomly determined nonmagical item you hold, wear, or carry on your person is broken or ruined.\n>>>Roll a d10. On a roll of 1, the item broken is a weapon, on a roll of 2 the item is armor or a shield, and on a roll of 3-10 it is an item that's not a shield or weapon.\n",
    "Painful Scar.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have a scar which gets painful whenever it rains, sleets, hails, or snows.\n>>>Whenever you attempt an action in combat and your scar is giving you pain, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing.\n",
    'Horrible Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and advantage on Charisma (Intimidation) checks.\n>>>Magical healing of 3rd level or higher removes the injury.\n',
    "Minor Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, the scar doesn't have any adverse effect, but chicks dig it.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the scar.\n"
]

SEVERE_BURNS = 'Severe Burns!\n>>>Player must suffer the effects of their own fire attack.\n'

HOT_FLASH = 'Hot flash!\n>>>Target catches on fire.\n>>>While the target is on fire it takes 2d4 fire damage at the start of each of its turns.\n>>>The target can end this condition by dropping prone and using 5 feet of movement to roll on the ground.\n'

BLESSED = 'Blessed!\n>>>Player rolls damage for the attack, then heals for half of that damage.\n'

ADDITIONAL_FIRE = 'Additionally, the target is on fire.\n>>>While the creature is on fire it takes 2d8 fire damage at the start of each of its turns.\n>>>The target can end this condition by dropping prone and using 5 feet of movement to roll on the ground.\n'

BLINDED = 'Blinded!\n>>>Target has disadvantage on Wisdom (Perception) checks that rely on sight and on ranged attack rolls.\n>>>The condition ends after 12 seconds, or if they receive magical healing.\n'

COLD_INJURY = [
    'Frozen Arm or Hand.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you can no longer hold anything with two hands, and you can hold only a single object at a time.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone applies bandages to the burn with a DC 15 Wisdom (Medicine) check and you spend fifteen days doing nothing but resting.\n',
    'Frozen Foot or Leg.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your walking speed is halved and you must use a cane or crutch to move.\n>>>You fall prone after using the Dash action.\n>>>You have disadvantage on Dexterity checks made to balance.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone applies bandages to the burn with a DC 15 Wisdom (Medicine) check and you spend fifteen days doing nothing but resting.\n',
    'Frozen Finger.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Dexterity (Sleight of Hand) checks and Dexterity checks to use fine tools (such as thieves tools) using the hand with the broken finger.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after someone tends to the finger with a DC 10 Wisdom (Medicine) check and you spend ten days doing nothing but resting.\n',
    'Reduced Movement Speed\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, your movement speed is halfed.\n>>>The condition ends if you receive magical healing.\n>>>Alternatively, the condition ends after spending at least ten minutes around a fire or after a short or long rest.\n'
]

COLD_CHILL = 'Cold Chill!\n>>>Player must suffer the effects of their own cold attack.\n'

FROZEN_SOLID = 'Frozen solid!\n>>>The target is frozen in place and is paralyzed for 1 minute.\n>>>The target can make a Constitution saving throw DC: 15 each round to end the condition.\n'

REDUCED_MOVEMENT = 'Reduced Movement Speed!\n>>>Movement speed is halfed.\n>>>The condition ends if the target receives magical healing.\n>>>Alternatively, the condition ends after spending at least ten minutes around a fire or after a short or long rest.\n'

LIGHTNING_INJURY = [
    "Painful Scar.\n>>>Make a consitition saving throw DC: 11\n>>>On a failed save, you have a scar which gets painful whenever it rains, sleets, hails, or snows.\n>>>Whenever you attempt an action in combat and your scar is giving you pain, you must make a DC 15 Constitution saving throw.\n>>>On a failed save, you lose your action and can't use reactions until the start of your next turn.\n>>>The injury heals if you receive magical healing\n",
    'Horrible Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks and advantage on Charisma (Intimidation) checks.\n>>>Magical healing of 3rd level or higher removes the injury.\n',
    "Minor Scar.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, the scar doesn't have any adverse effect, but chicks dig it.\n>>>Magical healing of 6th level or higher, such as heal and regenerate, removes the scar.\n",
    'Ringing Ears.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on hearing.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting.\n',
    'Bite Tongue. \n>>>Make a constitution saving throw DC: 11\n>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks.\n>>>When you cast a spell with a verbal component there is a 1d4 chance the spell will not work.\n>>>If the spell fails, you still used your action to try to cast it, but the spell did not use any slots or material components.\n>>>The injury heals if you receive magical healing, or complete a short or long rest.\n',
    'Muscle Contractions.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you experience severe muscle contractions paralizing you dropping you prone.\n>>>The contractions end after one round.\n'
]

SHORT_CIRCUIT = 'Short Circuit!\n>>>Player must suffer the effects of their own lightning attack.\n'

TAZED = "Tazed!\n>>>Target's speed is reduced to 0 and they cannot take the attack action until their next turn.\n"

CHAIN_LIGHTNING = 'Chain Lightning!\n>>>Three bolts then leap from that target to as many as three other Targets, each of which must be within 30 feet of the first target.\n>>>A target can be a creature or an object and can be targeted by only one of the bolts.\n>>>A target must make a Dexterity saving throw.\n>>>The target takes full lightning damage on a failed save, or half as much on a successful one.\n'

THUNDER_INJURY = [
    'Disoriented.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, whenever you attempt an action in combat, you must make a DC 10 Constitution saving throw.\n>>>On a failed save, you lose your action until the start of your next turn.\n>>>The condition ends if you receive magical healing or if you spend ten days doing nothing but resting.\n',
    'Ringing Ears.\n>>>Make a consitition saving throw DC: 14\n>>>On a failed save, you have disadvantage on Wisdom (Perception) checks that rely on hearing.\n>>>The injury heals if you receive magical healing.\n>>>Alternatively, the injury heals after you spend three days doing nothing but resting.\n'
]

UNWANTED_SOUND = 'Unwanted Sound!\n>>>Player must suffer the effects of their own thunder attack.\n'

RINGING_EARS = 'Ringing Ears!\n>>>Target has disadvantage on Wisdom (Perception) checks that rely on hearing.\n>>>The condition ends if you receive magical healing.\n>>>Alternatively, the condidtion ends after 1 minute.\n'

REDIRECTED = 'Redirected Impact!\n>>>Player must suffer the effects of their own force attack.\n'

CONTAMINATED = 'Contaminated!\n>>>Player must suffer the effects of their own necrotic attack.\n'

OVERWHELMED = 'Overwhelmed!\n>>>If the target does not have immunity or resistance to psychic damage, they gain vulnerability to psychic damage.\n>>>If they have resistance to psychic damage, they lose it.\n>>>If they have immunity to psychic damage, they lose it but gain resistance to psychic damage.\n'

DOMINATED = 'Dominated!\n>>>Attacker controls the target for their next turn.\n'

SUICIDAL = "Suicidal!\n>>>At the beginning each of the target's turn, they must pass a Wisdom saving throw DC: 12 or make an attempt to end their own life.\n"

IN_YOUR_HEAD = 'Contaminated!\n>>>Player must suffer the effects of their own necrotic attack.\n'

DECAY = "Decay!\n>>>Damage from this attack reduces the target's maximum hit points by the same amount.\n>>>The target cannot regain hit points for the next minute.\n>>>It may make a Constitution saving throw DC: 16 at the end of each of its turns to end this effect.\n"

PUTREFY = 'Putrefy!\n>>>Target is dropped prone and has their movement reduced to 0.\n>>>The target cannot regain hit points until the end of this condition.\n>>>This condition heals if they receive magical healing or after a long rest.\n'

RIGHTEOUS_MARK = 'Righteous mark!\n>>>The target glows for the next minute.\n>>>While glowing it produces bright light up to 10 feet and dim light up to 30 feet.\n>>>All successful attacks against the creature deal an additional 1d6 radiant damage.\n'

DISARM_PRONE = [
    'Disarmed!\n>>>Target is disarmed, throwing there weapon 5 feet away in a random direction.\n',
    'Disarmed!\n>>>Target is disarmed, throwing there weapon 10 feet away in a random direction.\n',
    'Disarmed!\n>>>Target is disarmed, throwing there weapon 15 feet away in a random direction.\n',
    'Knocked Prone!\n>>>Target is knocked prone.\n',
    'Knocked Prone!\n>>>Target is knocked prone.\n',
    'Knocked Prone!\n>>>Target is knocked prone.\n'
]

DISARM_PRONE_MISS = [
    'Disarmed!\n>>>Player is disarmed, throwing there weapon 5 feet away in a random direction.\n',
    'Disarmed!\n>>>Player is disarmed, throwing there weapon 10 feet away in a random direction.\n',
    'Disarmed!\n>>>Player is disarmed, throwing there weapon 15 feet away in a random direction.\n',
    'Knocked Prone!\n>>>Player is knocked prone.\n',
    'Knocked Prone!\n>>>Player is knocked prone.\n',
    'Knocked Prone!\n>>>Player is knocked prone.\n'
]

ADDITIONAL_DIE = 'Devistating Critical!\n>>>Spend one hit die to add an additional damage die to the damage.\n'

END_ACTION = 'Critical Miss! Player ends their action.'

RIPOSTE = 'Riposte!\n>>>Player triggers an opportunity attack for their target if they are in range.\n'

SUPER_CRITICAL = 'SUPER CRITICAL!!!\n>>>Deal maximum critical damage, as well as the following effect:\n'

END_ACTION = 'Critical Miss! Player ends their action.\n'

SECOND_CHANCE = 'Player gets another chance, re-roll attack!\n'

WRONG_TARGET = 'Wrong Target!\n>>>Player hits a random creature within range that is not the intended target.\n>>>If there are no targets in range, the player hits themselves.\n'

COMPROMISED = 'Compromised!\n>>>Player must suffer the effects of their own poison.\n'

NORMAL_MISS = '\nNormal Critical Miss...\n'

NORMAL_HIT = '\nNormal Critical Hit...\n'
