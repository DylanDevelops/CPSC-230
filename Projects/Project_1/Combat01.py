import random
import time

player = {}
computer = {}

characters = [
    {
        "name": "cleric",
        "health": 100,
        "attack": 10,
        "dodge": 0.2
    },
    {
        "name": "barbarian",
        "health": 120,
        "attack": 12,
        "dodge": 0.1
    },
    {
        "name": "druid",
        "health": 90,
        "attack": 9,
        "dodge": 0.3
    },
    {
        "name": "monk",
        "health": 80,
        "attack": 8,
        "dodge": 0.4
    },
    {
        "name": "warlock",
        "health": 110,
        "attack": 11,
        "dodge": 0.15
    },
    {
        "name": "bard",
        "health": 95,
        "attack": 9.5,
        "dodge": 0.25
    },
    {
        "name": "wizard",
        "health": 85,
        "attack": 8.5,
        "dodge": 0.35
    },
    {
        "name": "ranger",
        "health": 100,
        "attack": 10,
        "dodge": 0.25
    },
    {
        "name": "paladin",
        "health": 130,
        "attack": 13,
        "dodge": 0.05
    },
    {
        "name": "sorcerer",
        "health": 100,
        "attack": 10,
        "dodge": 0.2
    },
]

adjectives = ["glorious", "evil", "fun", "powerful", "rascal like", "bombastic", "nerdy", "spooky", "cringe", "mysterious", "goofy"]

print("\nWelcome to the arena! Before we let you into battle, you are going to have to choose a character!")
print("The character you choose is going to be an important role in how you play so choose wisely.\n")
print("Please enter the name of the character you would like to play as.")
print("The options are the Cleric, Barbarian, Druid, Monk, Warlock, Bard, Wizard, Ranger, Paladin, and Sorcerer.")
playerChoice = input("Your choice: ")

done = False
while not done:
    for character in characters:
        if character['name'] == playerChoice.lower():
            player = character
            done = True
            break
    else:
        print("\nThat is not a valid character. Please make sure you spelled it correctly!")
        playerChoice = input("Please enter your desired character: ")

computer = random.choice(characters)

print(f"\nYou will be playing as the {random.choice(adjectives)} {player['name'].capitalize()}. Here are your stats:\nHealth: {player['health']} hp\nAttack: {player['attack']} dmg\nDodge: {player['dodge'] * 100}% dmg reduction")
print(f"\nYour opponent will be the {random.choice(adjectives)} {computer['name'].capitalize()}. Their stats are:\nHealth: {computer['health']} hp\nAttack: {computer['attack']} dmg\nDodge: {computer['dodge'] * 100}% dmg reduction")

print(f"\nThe {computer['name']} approaches you looking {random.choice(adjectives)} as ever.")
print(f"You, the {player['name']}, are feeling {random.choice(adjectives)} and are ready to fight.")

def registerLogic(playerChoice, user):
    # 0 = Dodge
    # 1 = Attack
    # user = either the computer or 
    computerChoice = random.randint(0, 1)
    
    if playerChoice == 1 and computerChoice == 1:
        # both loose the full attack damage from their health
        computer['health'] = computer['health'] - player['attack']
        player['health'] = player['health'] - computer['attack']

        print(f"\nYou and the {computer['name']} both attacked each other resulting in both of you taking damage!")

    elif playerChoice == 1 and computerChoice == 0:
        # computer loses the player's attack damage changed by their own dodge modifer. player takes no damage
        computer['health'] -= player['attack'] * (1 - computer['dodge'])

        print(f"\nYou attacked the {computer['name']} while they dodged! They took less damage.")
        
    elif playerChoice == 0 and computerChoice == 1:
        # player loses the computer's attack damage changed by their own dodge modifier. computer takes no damage
        player['health'] -= computer['attack'] * (1 - player['dodge'])

        print(f"\nThe {computer['name']} attacked while you dodged! You took less damage.")

    elif playerChoice == 0 and computerChoice == 0:
        # if both the player and computer choose dodge, no one takes any damage
        print(f"\nYou and the {computer['name']} both dodged each other resulting in no one taking damage!")

    else:
        # WHATTTTTTT
        print("WHAT HOW DID THIS HAPPEN")

while computer["health"] > 0 or player["health"] > 0:
    print(f"You have:\n    {player['health']} hp\n    {player['attack']} dmg")
    print(f"The {computer['name']} has:\n    {computer['health']} hp\n    {computer['attack']} dmg")
    print("\nWould you like to attack or dodge?")
    playerChoice = input("Enter your choice (A) or (D): ")

    while True:
        if playerChoice.upper() == 'A':
            ComputerTurn(1)
            break
        elif playerChoice.upper() == 'D':
            ComputerTurn(0)
            break
        else:
            print(f"Unable to register the meaning of \'{playerChoice}\'.\n")
            playerChoice = input("Enter your choice (A) or (D): ")

print('someone got to 0 health')

