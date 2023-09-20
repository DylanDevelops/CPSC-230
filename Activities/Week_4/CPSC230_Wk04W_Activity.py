'''
1.  Guessing Game. Remember when we asked the user to guess a number and used 
    booleans to tell them if they were correct (see Wk02F_Activity)? Let's 
    make our game more interactive! 

    - First, create a number that will be the answer (answer = 7)
    - Second, create a counter variable to represent userAnswer (userAnswer = 0)
    - Then, create a while loop that repeatedly asks the user to guess a
      number between 1-10. The loop should only stop when userAnswer == answer
    - Congratulate the user when the loop ends (ie when they guess correctly)
'''

# Creates a variable called "correctAnswer" and stores the number 7 in it
correctAnswer = 7

# Asks the user to guess a number between 1 and 10 and stores it in "userNumber"
userNumber = int(input("Enter a number between 1 and 10: "))

# While the user's number is not equal to the correct answer, 
# tell them they're wrong and ask them to guess again.
while userNumber != correctAnswer:
    print("Sorry, that's not the right number.")
    userNumber = int(input("Enter a number between 1 and 10: "))

# When the user's number is equal to the correct answer,
# tell them they're right.
print("Nice work! You guessed the right number!")

'''
2.  Modify your code above to keep track of how many guesses it takes the 
    user to get teh correct answer. Be sure to display their guess count
    when they finally get it right!
'''

# Creates a variable called "correctAnswer" and stores the number 7 in it
correctAnswer = 7

# Asks the user to guess a number between 1 and 10 and stores it in
#  "userNumber" while also telling the "tries" variable to be 1
userNumber = int(input("Enter a number between 1 and 10: "))
tries = 1

# While the user's number is not equal to the correct answer,
# tell them they're wrong, ask them to guess again, and add 1 to the
# "tries" variable
while userNumber != correctAnswer:
    print("Sorry, that's not the right number.")
    tries += 1
    userNumber = int(input("Enter a number between 1 and 10: "))

# When the user's number is equal to the random number,
# tell them they're right and tell them how many tries it took them
print("Nice work! You guessed the right number! It took you " + str(tries) + " tries.")

'''
3.  Modify your code again so that you can play the game yourself! This 
    will require you to use the randint() function in the random module:
    https://docs.python.org/3/library/random.html#module-random
'''

# Imports random module
import random

# Creates a random number between 1 and 10 and stores it in "randomNumber"
randomNumber = random.randrange(1, 11)

# Asks the user to guess a number between 1 and 10 and stores it in
#  "userNumber" while also telling the "tries" variable to be 1
userNumber = int(input("Enter a number between 1 and 10: "))
tries = 1

# While the user's number is not equal to the random number,
# tell them they're wrong, ask them to guess again, and add 1 to the
# "tries" variable
while userNumber != randomNumber:
    print("Sorry, that's not the right number.")
    tries += 1
    userNumber = int(input("Enter a number between 1 and 10: "))

# When the user's number is equal to the random number,
# tell them they're right and tell them how many tries it took them
print("Nice work! You guessed the right number! It took you " + str(tries) + " tries.")

'''
4.  Modify your code one last time. This time, use and/or statements to
    limit the number of guesses the user has to 5. If the user does not
    guess correctly after 5, tell them "Sorry, better luck next time!" 
    If the user does guess correctly, tell them "Nice work! You guessed
    the rignt number in X tries!" (where X is the number of guesses)
'''

# Imports random module (not needed since imported above)
#import random

# Creates a random number between 1 and 10 and stores it in "randomNumber"
randomNumber = random.randrange(1, 11)

# Declares the max amount of guesses
maxGuesses = 5

# Asks the user to guess a number between 1 and 10 and stores it in
#  "userNumber" while also telling the "tries" variable to be 1
userNumber = int(input("Enter a number between 1 and 10: "))
tries = 1

# While the user's number is not equal to the random number,
# tell them they're wrong, ask them to guess again, and add 1 to the
# "tries" variable
while userNumber != randomNumber and tries < maxGuesses:
    print("Sorry, that's not the right number.")
    tries += 1
    userNumber = int(input("Enter a number between 1 and 10: "))

# When the user's number is equal to the random number,
# tell them they're right and tell them how many tries it took them
# and if they didn't guess correctly after 5 tries, tell them they lost.
if(tries == maxGuesses):
    print("Sorry, better luck next time!")
else:
    print("Nice work! You guessed the right number! It took you " + str(tries) + " tries.")