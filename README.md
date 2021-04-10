# Fumble Buddy

I have always felt there are certain elements missing in combat in Dungeons and Dragons 5e, such as broken swords/shields, disarming apponents, grusome injuries, and dramatic weapon drops. Unfortunatly, the RAW for these events leave their frequency entierly up to the DM which puts them in an awkward situation. 

"When do I make the players drop their weapons on a critical failur? Everytime? Never? What about injuries? How do I decide what limb gets hacked off?"

I wanted to avoid these hard questions while I managed the game, and thus Fumble Buddy was born!

## Use
Fumble Buddy offers three randomly generated services: critical hits, critical misses, and injuries. For critical hits/misses, the program randomly determines the outcome of the attack and generates a scenario based on the damage type of the attack. For injuries, the program randomly selects an injury based on desired severity of the injury. You may also specify a ```repeat``` value to generate multiple scenarios to pick from.

* Note: This command-line client is meant only as inspiration for the dungeon master, and should only be used at the dungeon master's discretion.  

## Prerequisites

To run this script you must have Python 3.0 or greater installed. If you do not have Python installed, follow [this guide](https://www.tutorialdocs.com/tutorial/python3/setup-guide.html) to install.

```
Give examples
```

## Installing

Clone this repo or copy the contents of the fumble.py to an easily available location on your computer.

```
git clone https://github.com/davidbradlycurtis/fumble_buddy.git
```

### Use Examples
#### Critical Hit
My player attacks a Gnoll with a sword and rolls and natural 20, instead of following the RAW critical hit rules I enter the following command:

```
python fumble.py hit -s
```

Which gives me:
```
Critical Wound. 
>>>Target's max hp is reduced 1d8 each round until the wound is treated with magical healing, or after a Medicine check DC:14.
```

So instead of the player doing a little bit more damage to the Gnoll (boring), the Gnoll is given a deadly lingering injury which will completely alter the battle.

#### Critical Miss
My player attacks a Gnoll with a sword and rolls and natural 1, instead of following the RAW critical miss rules I enter the following command:

```
python fumble.py miss -s
```

Which gives me:
```
Player gets another chance, re-roll attack!
```

So instead of the player missing the attack and moving on with game, the player gets a second chance.

#### Injury
My player falls from a cliff taking 35 damage in process. It makes sense the character would get some sort of small linguring injury from this, so enter the following command:

```
python fumble.py injury -m
```

Which gives me:
```
Teeth Knocked Out.
>>>Make a consitition saving throw DC: 14
>>>On a failed save, you have disadvantage on Charisma (Persuasion) checks.
>>>When you cast a spell with a verbal component there is a 25% chance the spell will not work.
>>>If the spell fails, you still used your action to try to cast it, but the spell did not use any slots or material components.
>>>The injury heals if you receive magical healing.
```

So now in addtion to the damage from the fall, I will tell the player they landed on a rock (mouth first) knocking their teeth out.



## Built With

* [Visual Studio Code](https://code.visualstudio.com/) - The IDE used
* [Python](https://www.python.org/) - Programming Language


## Authors

* **David Curtis** - *Initial work* - [davidbradlycurtis](https://github.com/davidbradlycurtis)

## License

This project is licensed under the MIT License

## Acknowledgments

* Injury Tables from James Introcaso
* Inspiration from https://sterlingvermin.com/
