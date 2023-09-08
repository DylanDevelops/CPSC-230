# Class Activities Week 2 - Friday

# Classwork-----------------------------------------------
'''
1.  Use Python to change z into a string. Display the type(z) in the terminal
    before and after making the change.
'''
print("--- Problem 1 ---")

# Assigns the value to z
z = 156

# Prints z's type as an int and z's type as a string
print("z as an int is:", type(z))
print("z as a string is:", type(str(z)))


'''
2.  Write some code that asks the user to guess a number between 1-10.
    Convert that number to an int, and then a use boolean operation to
    check if the number they guessed is 7 (no if-statements required). 
    Print out the resulting Boolean value (True when they guessed 7, 
    and False otherwise.)
'''
print("--- Problem 2 ---")

# Asks the user to guess a number between 1-10 and converts the string (input) to an int
chosenNumber = int(input("Guess a number between 1-10: "))

# Prints either true or false depending on if the user guessed 7
print("Was your guess correct? It was", chosenNumber == 7, end=".\n")

'''
3.  With your group, discuss why this code doesn't work, and what
    would need to be changed to fix it. Add comments to explain 
    what you did.
'''
print("--- Problem 3 ---")

''' Original code doesn't work because you can't divide a string by an int.
i = input("How many times do you eat off campus each week? ")
avg = i/7
print(avg, " times a day on average! Cool!")
'''

# New code

# I convert the user input into a float right away and store it in i
i = float(input("How many times do you eat off campus each week? "))

# I divide the new float by 7 (all days in the week) to get the average and store it in a variable called "avg"
avg = i/7

# I print the average
print(avg, "times a day on average! Cool!")

'''
4.  Ask the user to enter a number, then use the math module to
    calculate the square root of that number and print out the result
'''
print("--- Problem 4 ---")

# Imports the math module
import math

# Converts the user input into a float
userInput = float(input("Enter a number: "))

# Calculates the square root of the user input and stores it in a variable called "squareRoot"
squareRoot = math.sqrt(userInput)

# Prints the square root of the user's input
print("The square root of", userInput, "is", squareRoot, end=".\n")

'''
5.  Pull up the code from the Week 2 - Wednesday activity. Let's make
    the triangle area calculator more interactive. Instead of simply
    defnining x and y yourself, ask the user to enter two numbers (b, h)
    to represent the base and hight of their triangle. Display the result 
    to the user (ex. "The area of your triangle is 15")
'''
print("--- Problem 5 ---")

# Asks the user for the base and height of their triangle and converts the strings to floats
b = float(input("Enter the base of your triangle: "))
h = float(input("Enter the height of your triangle: "))

# Calculates the area of the triangle and stores it in a variable called "area"
area = (b * h) / 2

# Prints the area of the triangle
print("The area of your triangle is", area, end=".\n")

'''
6.  BONUS: Chat with your group about other useful equations you could run using
    input from a user (area of a circle, a backyard, etc.). Make a plan and
    write a small chunk of code that takes at least 2 user inputs and 
    displays the result of at least 1 calculation. Feel free to use the 
    monitors at your tables and work together.
'''

# Asks the user for the radius and the height of their cylinder and converts the strings to floats
radius = float(input("Enter the radius of your cylinder: "))
height = float(input("Enter the height of your cylinder: "))

# Calculates the volume of the cylinder and stores it in a variable called "volume"
# Equation for the volume of a cylinder: V = pi * r^2 * h
volume = math.pi * (radius ** 2) * height

# Prints the volume of the cylinder
print("The volume of your cylinder is", volume, end=".\n")