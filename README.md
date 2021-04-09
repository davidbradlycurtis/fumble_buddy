# Fumble Buddy

Everyone loves critical hits in Dungeons and Dragons 5e, but critical misses never get any of the love. While no one enjoys getting a critical miss on an attack, Fumble Buddy makes them far more interesting and challenging!  

## Use
Fumble Buddy offers three randomly generated services: critical hits, critical misses, and injuries. For critical hits/misses, the program randomly determines the outcome of the attack and generates a scenario based on the damage type of the attack. For injuries, the program randomly selects an injury based on desired severity of the injury. You may also specify a ```repeat``` value to generate multiple scenarios to pick from.

* Note: This command-line client is meant only as inspiration for the dungeon master, and should only be used at the dungeon master's discretion.  

### Examples
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

## Prerequisites

To run this script you must have Python 3.0 or greater installed. If you do not have Python installed, follow [this guide](https://www.tutorialdocs.com/tutorial/python3/setup-guide.html) to install.

```
Give examples
```

## Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo



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
