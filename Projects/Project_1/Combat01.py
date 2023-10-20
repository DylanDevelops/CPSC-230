import random
import time

characters = [
    {
        "name": "cleric",
        "health": 100,
        "attack": 10,
        "dodge": 0.2,
        "winMessage": "May the divine have mercy on your soul.",
        "loseMessage": "I have been defeated, but my faith remains unbroken."
    },
    {
        "name": "barbarian",
        "health": 120,
        "attack": 12,
        "dodge": 0.1,
        "winMessage": "You fought well, but strength alone cannot overcome skill.",
        "loseMessage": "I have been defeated, but I will return stronger than ever."
    },
    {
        "name": "druid",
        "health": 90,
        "attack": 9,
        "dodge": 0.3,
        "winMessage": "The power of nature has triumphed over your technology.",
        "loseMessage": "I have been defeated, but the spirits of the forest will guide me to victory next time."
    },
    {
        "name": "monk",
        "health": 80,
        "attack": 8,
        "dodge": 0.4,
        "winMessage": "Your mind was weak, but your spirit was strong.",
        "loseMessage": "I have been defeated, but my mind remains sharp and my spirit unbroken."
    },
    {
        "name": "warlock",
        "health": 110,
        "attack": 11,
        "dodge": 0.15,
        "winMessage": "Your light was no match for the darkness within me.",
        "loseMessage": "I have been defeated, but the light will always triumph over darkness."
    },
    {
        "name": "bard",
        "health": 95,
        "attack": 9.5,
        "dodge": 0.25,
        "winMessage": "Your silence has been broken by the power of music!",
        "loseMessage": "I have been defeated, but the power of music will always live on."
    },
    {
        "name": "wizard",
        "health": 85,
        "attack": 8.5,
        "dodge": 0.35,
        "winMessage": "Your knowledge was no match for my mastery of the arcane.",
        "loseMessage": "I have been defeated, but my thirst for knowledge remains unquenched."
    },
    {
        "name": "ranger",
        "health": 100,
        "attack": 10,
        "dodge": 0.25,
        "winMessage": "The wilderness has claimed another victim.",
        "loseMessage": "I have been defeated, but the wilderness will always be my home."
    },
    {
        "name": "paladin",
        "health": 130,
        "attack": 13,
        "dodge": 0.05,
        "winMessage": "Your evil has been vanquished by the power of righteousness!",
        "loseMessage": "I have been defeated, but the power of righteousness will always triumph over evil."
    },
    {
        "name": "sorcerer",
        "health": 100,
        "attack": 10,
        "dodge": 0.2,
        "winMessage": "Your mortal blood was no match for the power of my bloodline.",
        "loseMessage": "I have been defeated, but the power of my bloodline will always live on."
    },
]

player = {}
computer = {}

adjectives = ["glorious", "evil", "fun", "powerful", "brave", "rascal like", "bombastic", "nerdy", "spooky", "cringe", "mysterious", "goofy", "sad"]

playing = True

while playing:
    player.clear()
    computer.clear()

    print("\nWelcome to the arena! Before we let you into battle, you are going to have to choose a character!")
    print("The character you choose is going to be an important role in how you play so choose wisely.\n")
    print("Please enter the name of the character you would like to play as.")
    print("The options are the Cleric, Barbarian, Druid, Monk, Warlock, Bard, Wizard, Ranger, Paladin, and Sorcerer.")
    playerChoice = input("Your choice: ")

    done = False
    while not done:
        for character in characters:
            if character['name'] == playerChoice.lower():
                player = character.copy()
                done = True
                break
        else:
            print("\nThat is not a valid character. Please make sure you spelled it correctly!")
            playerChoice = input("Please enter your desired character: ")

    computer = random.choice(characters).copy()

    print(f"\nYou will be playing as the {random.choice(adjectives)} {player['name'].capitalize()}. Here are your stats:\nHealth: {player['health']} hp\nAttack: {player['attack']} dmg\nDodge: {player['dodge'] * 100}% dmg reduction")
    print(f"\nYour opponent will be the {random.choice(adjectives)} {computer['name'].capitalize()}. Their stats are:\nHealth: {computer['health']} hp\nAttack: {computer['attack']} dmg\nDodge: {computer['dodge'] * 100}% dmg reduction")
    time.sleep(1)
    print("\n3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print(f"\n\n\n\n\n\n\n\nThe {computer['name']} approaches you looking {random.choice(adjectives)} as ever.")
    print(f"You, the {player['name']}, are feeling {random.choice(adjectives)} and are ready to fight.")

    def PlayMove(playerChoice):
        # 0 = Dodge
        # 1 = Attack
        # user = either the computer or 
        computerChoice = random.randint(0, 1)

        print(f"\n\n\n\n\n\n\n\nThe {computer['name']} chose to {'Dodge' if computerChoice == 0 else 'Attack'}!")
        
        if playerChoice == 1 and computerChoice == 1:
            # both loose the full attack damage from their health
            computer['health'] = int(round(computer['health'] - player['attack'], 0))
            player['health'] = int(round(player['health'] - computer['attack'], 0))

            print(f"\nYou and the {computer['name']} both attacked each other resulting in both of you taking damage!")

        elif playerChoice == 1 and computerChoice == 0:
            # computer loses the player's attack damage changed by their own dodge modifer. player takes no damage
            computer['health'] -= int(round(player['attack'] * (1 - computer['dodge']), 0))

            print(f"\nYou attacked the {computer['name']} while they dodged! They took less damage.")
            
        elif playerChoice == 0 and computerChoice == 1:
            # player loses the computer's attack damage changed by their own dodge modifier. computer takes no damage
            player['health'] -= int(round(computer['attack'] * (1 - player['dodge']), 0))

            print(f"\nThe {computer['name']} attacked while you dodged! You took less damage.")

        elif playerChoice == 0 and computerChoice == 0:
            # if both the player and computer choose dodge, no one takes any damage
            print(f"\nYou and the {computer['name']} both dodged each other resulting in no one taking damage!")

        else:
            # WHATTTTTTT
            print("WHAT!???!?!?!?!!???! HOW DID THIS HAPPEN")

    while computer["health"] > 0 and player["health"] > 0:
        print(f"You have:\n    {player['health']} hp\n    {player['attack']} dmg")
        print(f"The {computer['name']} has:\n    {computer['health']} hp\n    {computer['attack']} dmg")
        print("\nWould you like to attack or dodge?")
        playerChoice = input("Enter your choice (A) or (D): ")

        while True:
            if playerChoice.upper() == 'A':
                PlayMove(1)
                break
            elif playerChoice.upper() == 'D':
                PlayMove(0)
                break
            else:
                print(f"\'{playerChoice}\' is not a valid choice.")
                playerChoice = input("Enter your choice (A) or (D): ")

    def Win(winningStats, winningUser):
        global playing
        time.sleep(1)
        if winningUser == 'player':
            # This means that the person who won is the player
            print(f"\n\n\n\n\n\n\n\nAs you were fighting, all of a sudden the {computer['name']} fell to the ground...")
            time.sleep(3)
            print(f"You walked up to the {random.choice(adjectives)} {computer['name']} as they laid on the ground looking back up to you.")
            time.sleep(3)
            print(f"You looked down at the {computer['name']} and said, \"{player['winMessage']}\"")
            time.sleep(3)
            print(f"The {computer['name']} raised their head to look up at you and said, \"{computer['loseMessage']}\"")
            time.sleep(3)
            print(f"You took one last look at the {computer['name']} before finishing them off.")
            time.sleep(3)
            print(f"You, the {player['name']}, were triumphant. You were victorious. You felt {random.choice(adjectives)}.")
            time.sleep(3)
            print('You left the arena feeling more powerful than you ever had before. Would you retire or fight again?')
            time.sleep(3)
        elif winningUser == 'computer':
            # This means that the person who won is the computer
            print("\n\n\n\n\n\n\n\nAs you were fighting, all of a sudden a cold feeling rushed into your head.")
            time.sleep(3)
            print(f"You, the {player['name']} fell to the ground. Overcome with fear, you watched as the {computer['name']} walked over to you.")
            time.sleep(3)
            print(f"The {computer['name']} looked down at you and said, \"{computer['winMessage']}\"")
            time.sleep(3)
            print(f"Even though you knew it was over, you looked up at the {computer['name']} and said, \"{player['loseMessage']}\"")
            time.sleep(3)
            print("You took one last breath before the world went black.")
            time.sleep(3)

        playAgain = input('\n\nWill you fight again? Type \'Continue\' to play again or \'Exit\' to exit the arena: ')

        checkInput = True
        while checkInput:
            if playAgain.lower() == 'continue':
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                checkInput = False
                break
            elif playAgain.lower() == 'exit':
                print('\n\n\nThank you for playing!\n\n\n')
                playing = False
                checkInput = False
            else:
                print('\nNot a valid choice!')
                playAgain = input('\n\nWill you play again? Type \'Continue\' to play again or \'Exit\' to exit the arena: ')

    def Tie():
        # this code gets called when both players get to 0 health at the same time
        time.sleep(1)
        print("\n\n\n\n\n\n\n\nAs you were fighting, all of a sudden a cold feeling rushed into your head.")
        time.sleep(3)
        print(f"You, the {player['name']} fell to the ground. Overcome with fear, you worried that any moment your opponent, the {computer['name']} would come over to you.")
        time.sleep(3)
        print(f"As you waited, however, nothing happened. You lifted your head to see that the {computer['name']} was also on the ground.")
        time.sleep(3)
        print(f"You had both tied. There was no winner only losers in this arena.")
        time.sleep(3)
        print("You looked up at the judges of the fight remembering that it was a fight to the death. Both fighters were maimed and that meant only one thing.")
        time.sleep(3)
        print(f"Next thing you knew a horn blew and a swarm of arrows came over the arena wall headed right toward you and the {computer['name']}. Before you had a chance to think, the world went black.")
        time.sleep(3)

        playAgain = input('\n\nWill you fight again? Type \'Continue\' to play again or \'Exit\' to exit the arena: ')

        checkInput = True
        while checkInput:
            if playAgain.lower() == 'continue':
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                checkInput = False
                break
            elif playAgain.lower() == 'exit':
                print('\n\n\nThank you for playing!\n\n\n')
                playing = False
                checkInput = False
            else:
                print('\nNot a valid choice!')
                playAgain = input('\n\nWill you play again? Type \'Continue\' to play again or \'Exit\' to exit the arena: ')

    if player['health'] <= 0 and computer['health'] <= 0:
        Tie()
    elif player['health'] <= 0:
        # This is called when the computer loses
        Win(computer, 'computer')
    elif computer['health'] <= 0:
        # This is called when the computer loses
        Win(player, 'player')