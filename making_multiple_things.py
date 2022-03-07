'''
# Make a Hero, then make more
Goal: Allow the player in this game to setup multiple heroes for their team, but without me needing to know, in advance, how many there wil be.

Problem: I don't know how many (could be between 0-? - typically not more than 15, but there's no technical limit) heroes, 
and thus I don't know how to "add" to my lists/dictionaries without having pre-written variables.

Some Stipulations: I'm trying to do this WITHOUT going into Classes, as I'm still getting up to that point, 
want to be able to make the mini version of my game without using classes at all, then update and add classes.  
Reason for stipulation: Want to learn from the most basic and steadily work up to more advanced topics, 
and right now classes make me want to eat cyanide.

Here is what I *THINK* the data should approximately look like in a given example.

All_of_the_Heroes = [
    hero1 = {
        "Name": "Bob",
        "Spells": [],
        "Skills": ["Tactics": 4]
    },
    hero2 = {
        "Name": "MarySue",
        "Spells": ["Fervor", "Ward", "Mind Leech"],
        "Skills": ["Leadership": 7, "Tactics": 4]
    },
    hero3 = {
        "Name": "CannonFodder",
        "Spells": ["Might"],
        "Skills": ["Leadership": 2]
    },
]

Prenotes before reading the code: yes, I can use functions.  And, I do in the actual game code, but this is broken out into very simplistic steps for sheer readability.

All of the code below works perfectly for making a sinlge hero.
'''
import pyinputplus as pyip

# A basic datablock for a singular hero.
hero_data = {
    "Name": "",
    "Spells": [],
    "Skills": []
    }

# Using Strings for the spell names instead of their full variable terms for simplicity.  
spells = ("Might", "Fervor", "Stalwart" , "Ward", "Celerity", "Forced March",
         "Armament", "True-Cause", "Napoleon", "Mind Leech", "Force Cage")

# Same deal, using Strings for skill names for simplicity
leader_combat_skills = ["leadership", "tactics"]

# Simply asking for an input, I like using PyInputPlus because it's easy to format.
# Storing this into a temporary variable, so that when I convert this to functions - this will be the temp variable that I return to add to the dictionaries/lists.
hero_name = pyip.inputStr("What is your Hero's name? ", blank=False)

# Logic is: if a hero doesn't have any spells, the player simply leaves the entry blank causing the code to break out of the while and not bother to add a spell.
hero_spells=[]
print("What spells does {} know?  Hit enter if none or no more. ".format(hero_name))
choice = 1
while choice != '':
    choice = pyip.inputMenu(spells, numbered=True, blank=True)
    if choice == '':
        break
    else:
        hero_spells.append(choice)

# Same logic as for spells, except that skills have degrees of knowledge to them ("ranks").  So, we ask two questions.  First gets the skill, 2nd gets the # of ranks.
hero_skills={}
print("Which skills does {} know? Hit enter if none or no more. ".format(hero_name))
choice = 1
while choice !='':
    choice = pyip.inputMenu(leader_combat_skills, numbered=True, blank=True)
    if choice == '':
        break
    else:
        num_of_ranks = pyip.inputInt(prompt = "How many ranks in the {} skill ? ".format(choice), blank=False)
        hero_skills.update({choice: num_of_ranks})

# print the temporary components individually to make sure nothing is lost from our expectations.
print(hero_name)
print(hero_spells)
print(hero_skills)

# cram all of the data into hero_data
hero_data.update({"Name": hero_name})
hero_data.update({"Spells": hero_spells})
hero_data.update({"Skills": hero_skills})
print(hero_data)

