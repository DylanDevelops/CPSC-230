--------------------------------------------

Dylan Ravel
November 29th, 2023
Project 1 - Part 3

Collaborators: 
    1. Sammy Rokaw - I gave my transcript class to him

References: 
    1. https://book.pythontips.com/en/latest/for_-_else.html
    2. https://realpython.com/python-sleep/
    3. https://www.geeksforgeeks.org/ternary-operator-in-python/
    4. https://www.programiz.com/python-programming/global-keyword
    5. https://www.geeksforgeeks.org/python-pass-statement/

README:

                    ~ Combat03.py ~

    The game is a text-based combat simulator where you select a character 
and engage in a duel against a computer-controlled opponent. 

    Before any gameplay begins, the user is able to choose a name of their
game. This is then used to title the transcript file, "CHOSEN-NAME_transcript.txt"
and is created in the directory at which they are in when running the .py file. 

The game begins with the selection of a character, deciding a name, and a difficulty
level. You are also able to get stats about the character by passing a "-i"
in after typing a character name. The chosen difficulty modifies the stats 
of both the player's and the computer's characters.

    In each round, which are counted and displayed, players can choose to either 
attack or dodge. If both the player and the computer choose to attack, both 
characters take damage. If the player attacks while the computer dodges, the 
computer takes reduced damage. If the player dodges while the computer attacks, 
the player takes less damage and vice versa. If both parties dodge, no damage is 
dealt to either one.

    Each character also has a special ability that can be used once per game. 
These abilities can either heal the player or deal extra damage to the
opponent, depending on the character chosen. The special abilities also 
change based on the selected difficulty level.

    The game concludes when either the player's or the computer's health drops to 
0 or below. The player wins if the computer's health reaches 0 first, while the 
computer wins if the player's health depletes first. A tie occurs if both the 
player and the computer's health reach 0 simultaneously.

    After each game, players are given the option to play again or exit the game. If 
they choose to play again, the game restarts with the character and difficulty 
selection. If they choose to exit, the game ends.

-----------------------------------------------