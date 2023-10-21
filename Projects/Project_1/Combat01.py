# --------------------------------------------
# Dylan Ravel
# October 20th, 2023
# Project 1
# References: Found in README.txt
# README: Found in README.txt
# -----------------------------------------------

# importing the packages I use throughout the entire game
import random # used to randomize values throughout the game
import time # used to delay when something is outputted to the console to make the game last a little longer

# Declaring all the characters that the player and computer can choose from
characters = [
    {
        "name": "cleric", # name of the character
        "health": 100, # their default health
        "attack": 10, # their default attack damage
        "dodge": 0.2, # their default dodge multiplier
        "winMessage": "May the divine have mercy on your soul.", # their winning message
        "loseMessage": "I have been defeated, but my faith remains unbroken." # their losing message
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

# declares two variables that will eventually be set to a copy of the chosen characters from above
player = {}
computer = {}

# declares a list of adjectives that can be used later in the code
adjectives = ["glorious", "evil", "fun", "powerful", "brave", "rascal like", "bombastic", "nerdy", "spooky", "cringe", "mysterious", "goofy", "sad"]

# Sets the current status to playing. This is used later to decide if the user wants to end the game or continue to play
playing = True
while playing:
    # I clear anything that could be left over from a previous playthrough
    player.clear()
    computer.clear()

    # It welcomes the player and explains the game
    print("\nWelcome to the arena! Before we let you into battle, you are going to have to choose a character!")
    print("The character you choose is going to be an important role in how you play so choose wisely.\n")
    
    # tells the user to choose a character
    print("Please enter the name of the character you would like to play as.")
    print("The options are the Cleric, Barbarian, Druid, Monk, Warlock, Bard, Wizard, Ranger, Paladin, and Sorcerer.")
    playerChoice = input("Your choice: ")

    # this code checks if the choice is valid or not
    done = False
    while not done:
        for character in characters:
            if character['name'] == playerChoice.lower():
                # if the character exists, clone the stats from the characters list to the new value 'player' then break out of the loop and continue on
                player = character.copy()
                done = True
                break
        else:
            # called if they didn't select a valid character
            print("\nThat is not a valid character. Please make sure you spelled it correctly!")
            playerChoice = input("Please enter your desired character: ")

    # chooses a random character and clones the stats to a variable 'computer'
    computer = random.choice(characters).copy()

    # Tells the user to choose a difficulty they want to play on
    difficulty = input("\nChoose the difficulty level ['Easy', 'Medium', 'Hard']: ")
    done = False
    while not done:
        if difficulty == "easy":
            # set all values to the easy values
            player['health'] += 20
            player['attack'] += 6
            player['dodge'] += 0.03

            computer['health'] -= 10
            computer['attack'] -= 5
            computer['dodge'] -= 0.03

            done = True
            break
        elif difficulty.lower() == "medium":
            # keep all the same values if medium
            pass
        elif difficulty.lower() == "hard":
            # set all the values to hard values
            player['health'] -= 20
            player['attack'] -= 5
            player['dodge'] -= 0.03

            computer['health'] += 10
            computer['attack'] += 6
            computer['dodge'] += 0.03

            done = True
            break
        else:
            # if they didn't choose correctly, ask again until they choose correctly
            print("That's not a valid choice!")
            difficulty = input("\nChoose the difficulty level ['Easy', 'Medium', 'Hard']: ")

    # tells the user the stats of themself and their opponent
    print(f"\nYou will be playing as the {random.choice(adjectives)} {player['name'].capitalize()}. Here are your stats:\nHealth: {player['health']} hp\nAttack: {player['attack']} dmg\nDodge: {player['dodge'] * 100}% dmg reduction")
    print(f"\nYour opponent will be the {random.choice(adjectives)} {computer['name'].capitalize()}. Their stats are:\nHealth: {computer['health']} hp\nAttack: {computer['attack']} dmg\nDodge: {computer['dodge'] * 100}% dmg reduction")
    
    # initiates a countdown timer until it is time to play
    time.sleep(1)
    print("\n3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

    # this is the start of the game
    print(f"\n\n\n\n\n\n\n\nThe {computer['name']} approaches you looking {random.choice(adjectives)} as ever.")
    print(f"You, the {player['name']}, are feeling {random.choice(adjectives)} and are ready to fight.")

    # declares a function that handles the logic for every turn
    def PlayMove(playerChoice):
        # 0 = Dodge
        # 1 = Attack
        # user = either the computer or 

        # the computer chooses either to dodge or attack
        computerChoice = random.randint(0, 1)

        # tells the user what the computer chose
        print(f"\n\n\n\n\n\n\n\nThe {computer['name']} chose to {'Dodge' if computerChoice == 0 else 'Attack'}!")
        
        # both loose the full attack damage from their health
        if playerChoice == 1 and computerChoice == 1:
            # handles the calculations for what happens if this choice is chosen
            computer['health'] = int(round(computer['health'] - player['attack'], 0))
            player['health'] = int(round(player['health'] - computer['attack'], 0))

            # tells the user what happened
            print(f"\nYou and the {computer['name']} both attacked each other resulting in both of you taking damage!")

        # computer loses the player's attack damage changed by their own dodge modifier. player takes no damage
        elif playerChoice == 1 and computerChoice == 0:
            # handles the calculations for what happens if this choice is chosen
            computer['health'] -= int(round(player['attack'] * (1 - computer['dodge']), 0))

            # tells the user what happened
            print(f"\nYou attacked the {computer['name']} while they dodged! They took less damage.")
            
        # player loses the computer's attack damage changed by their own dodge modifier. computer takes no damage
        elif playerChoice == 0 and computerChoice == 1:
            # handles the calculations for what happens if this choice is chosen
            player['health'] -= int(round(computer['attack'] * (1 - player['dodge']), 0))
            
            # tells the user what happened
            print(f"\nThe {computer['name']} attacked while you dodged! You took less damage.")

        # if both the player and computer choose dodge, no one takes any damage
        elif playerChoice == 0 and computerChoice == 0:
            # no calculations are needed here because no one inflicted any damage

            # tells the user what happened
            print(f"\nYou and the {computer['name']} both dodged each other resulting in no one taking damage!")

        # WHATTTTTTT     
        else:
            # It is physically impossible for this to ever be called but if by some miracle it does, god help us.
            print("WHAT!???!?!?!?!!???! HOW DID THIS HAPPEN")

    # this loop runs as long as the player and computer health is above 0 otherwise it will break
    # this is basically the main loop for the game
    while computer["health"] > 0 and player["health"] > 0:
        # tells the current stats of the player and computer
        print(f"You have:\n    {player['health']} hp\n    {player['attack']} dmg")
        print(f"The {computer['name']} has:\n    {computer['health']} hp\n    {computer['attack']} dmg")

        # asks if the player would like to attack or dodge
        print("\nWould you like to attack or dodge?")
        playerChoice = input("Enter your choice (A) or (D): ")

        # handles the logic to make sure that the choice they made is valid
        while True:
            if playerChoice.upper() == 'A':
                # calls the function to do a new turn in the 'attack' modifier (1)
                PlayMove(1)
                break
            elif playerChoice.upper() == 'D':
                # calls the function to do a new turn in the 'dodge' modifier (0)
                PlayMove(0)
                break
            else:
                # this is called if the choice is not valid and asks them to reenter a correct choice
                print(f"\'{playerChoice}\' is not a valid choice.")
                playerChoice = input("Enter your choice (A) or (D): ")

    # defines the function for handling a win
    def Win(winningStats, winningUser):
        # sets the variable 'playing' to be mutable globally from inside of function like this
        global playing

        # waits 1 second before displaying everything after
        time.sleep(1)

        # if the winner is the player, run this code
        if winningUser == 'player':
            # this is the story that plays if you win in the console. It waits 3 seconds before printing a new line every time
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
        
        # if the winner is the computer, run this code
        elif winningUser == 'computer':
            # this is the story that plays if you lose in the console. It waits 3 seconds before printing a new line every time
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

        # After the game is over, this asks if the user would like to play again
        playAgain = input('\n\nWill you fight again? Type \'Continue\' to play again or \'Exit\' to exit the arena: ')

        # this handles the logic for playing again
        checkInput = True
        while checkInput:
            if playAgain.lower() == 'continue':
                # if the player chooses to play again, completely clear the console to have a fresh canvas
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                checkInput = False
                break
            elif playAgain.lower() == 'exit':
                # if the player choses to exit the game, thank them for playing and end the program
                print('\n\n\nThank you for playing!\n\n\n')
                playing = False
                checkInput = False
            else:
                # if the choice is not valid, tell them and ask them to enter a valid choice again
                print('\nNot a valid choice!')
                playAgain = input('\n\nWill you play again? Type \'Continue\' to play again or \'Exit\' to exit the arena: ')

    # this code is called if both players both have less than or equal to 0 health when the health check is ran
    def Tie():
        # This code tells the story when you tie. It also waits 3 seconds between each line to print the next
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

        # After the game is over, this asks if the user would like to play again
        playAgain = input('\n\nWill you fight again? Type \'Continue\' to play again or \'Exit\' to exit the arena: ')

        # this handles the logic for playing again
        checkInput = True
        while checkInput:
            if playAgain.lower() == 'continue':
                # if the player chooses to play again, completely clear the console to have a fresh canvas
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                checkInput = False
                break
            elif playAgain.lower() == 'exit':
                # if the player choses to exit the game, thank them for playing and end the program
                print('\n\n\nThank you for playing!\n\n\n')
                playing = False
                checkInput = False
            else:
                # if the choice is not valid, tell them and ask them to enter a valid choice again
                print('\nNot a valid choice!')
                playAgain = input('\n\nWill you play again? Type \'Continue\' to play again or \'Exit\' to exit the arena: ')

    # this if statement is run at the very end of this while loop every time a turn is finalized checking if the user or the computer health is less than or equal to 0
    if player['health'] <= 0 and computer['health'] <= 0:
        # this is run if the player and computer's health is less than or equal to 0 declaring a tie finally calling the Tie() function
        Tie()
    elif player['health'] <= 0:
        # This is called when only the computer's health is less than or equal to 0 meaning that the player won finally calling the Win() function
        Win(computer, 'computer')
    elif computer['health'] <= 0:
        # This is called when only the player's health is less than or equal to 0 meaning that the computer won finally calling the Win() function
        Win(player, 'player')