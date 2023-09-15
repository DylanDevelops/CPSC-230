
'''
1.  Ask the user to guess how many pets you have. Print a statement 
    telling them how close they are. (i.e. "Your guess is 5 away from
    the correct answer"). No if-statements needed. Just a single print
    statement with the results of your calculation
'''
# your code here

# Declares how many pets I have
myPets = 4

# Takes the user input for the guess, convert it to an int, and store it in "userGuess"
userGuess = int(input("How many pets do you think I have? "))

# Prints the result of | myPets - userGuess |. By using absolute value, it always returns a positive number.
print("Your guess is " + str(abs(myPets - userGuess)) + " away from the actual number of " + str(myPets) + ".")

'''
2.  Write some code that asks the user for 5 different numbers, and stores
    them in the variables x1, x2, x3, x4, and x5. Use a set to create a
    unique set of numbers entered (e.g. if they enter 5 twice, only count 
    it once.) Print out the set.
'''
# your code here

# Asks the user to input 5 numbers and stores them in the corresponding variables
x1 = int(input("Enter your first number: "))
x2 = int(input("Enter your second number: "))
x3 = int(input("Enter your third number: "))
x4 = int(input("Enter your fourth number: "))
x5 = int(input("Enter your fifth number: "))

# Creates a new set called "numberSet" and stores all the inputs from above in it.
numberSet = {x1, x2, x3, x4, x5}

# Displays the set and the length of the set
print("Your unique set is: " + str(numberSet) + " and it has a length of " + str(len(numberSet)) + ".")

'''
3.  Create three dictionaries storing the title, artist, and value of three 
    paintings in an art gallary of your choosing. Print out a string listing
    the title, artist, and value of your favorite of the paintings (use the 
    items in the dictionary not a new string) (no if-statement needed, just
    regular dictionary indexing)
'''
## There are two different ways to make a dictionary. Both are indexed in the same way ##
### 1) Curly Brackets
# myDog = {"Name": "Rex", "Age" : 4}
# print(myDog["Name"])

### 2)  dict() constructor
# myDog2 = dict(Name = "Rover", Age = 3)
# print(myDog2["Name"])

# your code here

# Defines three dictionaries with values accordingly
art1 = {"Title": "Mona Lisa", "Artist": "Leonardo da Vinci", "Value": "1,000,000,000"}
art2 = {"Title": "The Starry Night", "Artist": "Vincent van Gogh", "Value": "100,000,000"}
art3 = {"Title": "A Sunday Afternoon on the Island of La Grande Jatte", "Artist": "Georges Seurat", "Value": "650,000,000"}

# I then print out the title, artist, and value of my favorite piece in the console
print("The title of my favorite piece is \"" + art2["Title"] + "\" by " + art2["Artist"] + ". It's estimated value is $" + art2["Value"] + "+")

'''
4.  Write some code that asks the user to name the first woman to win a
    Nobel prize (just last name is fine). Write an if-statement that 
    tells the user if they got the answer right. BONUS: Have your code
    tell them they got the right answer even if they forget to capitalize
    the name
'''
# your code here

# Defines correct answer
correctAnswer = "Marie Curie"

# Stores user guess in "userGuess"
userGuess = input("Who was the first woman to win the nobel prize? ")

# Converts user guess all to lowercase and then compares to the correct answer in lower case
# and does the same thing with the last name being character 6 thru 10
if userGuess.lower() == correctAnswer.lower() or userGuess.lower() == correctAnswer[6:11].lower():
    print("You guessed correct!")
else:
    print("You guessed wrong!")

'''
5.  You are swimming in a pool and want to increase the length of the laps you
    are taking, so you start swimming diagonally from corner to corner. You know
    the length (35 ft) and width (20ft) of the pool, but not the length of the 
    diaganoal. Using the Pythagorean theoum (and the math module) write some code 
    that asks the user for the number of laps they took across the diagonal of
    the pool and display the total distance they swam.
'''

# your code here

# Imports the math module
import math

# Defines the length and width of the pool
length = 35
width = 20

# Asks the user for how many laps diagonally they swam 
# and stores it in "totalNumOfLaps"
totalNumOfLaps = int(input("Please enter how many laps you took diagonally across the pool: "))

# Calculates the total amount of distance with the calculations below
lengthOfDiagonalPath = math.sqrt(math.pow(length, 2) + math.pow(width, 2))
totalDistance = lengthOfDiagonalPath * totalNumOfLaps

# Prints the total amount of distance traveled in feet
print("The total distance you traveled is " + str(round(totalDistance, 2)) + "ft.")

'''
6.  BONUS: Using your operators (%,/,//,*), write some code to convert time in 
    minutes (e.g. 257) to hours and minutes (e.g. 4 hours and 17 minutes).
    Print out the numbers of hours/minutes in the form "X hours, Y minutes".
        Try it with multiple values:
            - 12,938 (answer: 215 hours, 38 minutes)
            - 55 (answer: 0 hours, 55 minutes)
            - 525,600 (answer: 8760 hours, 0 minutes )
            - 432 (answer: 7 hours, 12 minutes)
'''

# your code here

# Asks the user for the minutes
totalMinutes = int(input("Enter the number of minutes: "))

# Does the calculations for retrieving hours and minutes
totalNumOfHours = totalMinutes // 60
totalNumOfMinutes = totalMinutes % 60

print(str(totalNumOfHours) + " hour(s) and " + str(totalNumOfMinutes) + " minute(s)")