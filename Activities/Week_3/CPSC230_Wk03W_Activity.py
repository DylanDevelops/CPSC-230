'''
1.  Using modulo, check whether 1069 is odd or even. Try this on a few different
    numbers. Can you use this idea to write an if-statement that tells the user if 
    their number is odd or even?
'''
print(1069%2)
# your code here

# Asks the user to input a number and stores it in the variable "number"
number = int(input("Enter a number: "))

# Checks if the user input is even or odd and prints 
# the result using an if statement.
if(number % 2 == 0):
    print(str(number) + " is even!")
else:
    print(str(number) + " is odd!")

'''
2.  Ask the user for the radius of a circle. Use the full value of pi stored 
    in the math module to calculate the area and circumference of that circle 
    and display the results.
'''

# your code here

# Imports the math module
import math

# Asks the user for the radius of the circle and stores it in the variable "radius"
radius = float(input("Enter the radius of the circle: "))

# Prints the area of the circle by using the formula C = 2 * pi * r 
# and converting to a string
print("The circumference of your circle is " + str(round(2 * math.pi * radius, 2)))


'''
3.  Write some code to tell the user whether or not to water their succulent. 
    You can prompt them with the question "Is the soil wet?". If they say "yes"
    print a statement telling them to leave it alone. If they say "no" print
    a statement telling them to water the plant
'''

# your code here

# Asks the user if the soil is wet and stores the response in the variable "response"
response = input("Is the soil wet? (yes/no): ")

# Checks if the response is "yes" or "no" and prints the appropriate response
# also prints an error message if the response is not "yes" or "no"
if response == "yes":
    print("You don't need to water the plant.")
elif response == "no": 
    print("You need to water your plant!")
else:
    print("Invalid answer format. Please run the code again.")

'''
4.  You can use the len() function to check the length of a collection type
    (ie numbers of characters in a string, individual items in a set, etc.).
    Ask the user to input a word and store it in the variable my_word. Using 
    len() and an if statement, write some code that checks whether the length 
    of a word is greater than or equal to 10. If it is, print out: 
    "Wow, that is a long word!"
'''
exampleWord = "test"

print(len(exampleWord))

# your code here

# Asks the user to input a word and stores it in the variable "my_word"
my_word = input("Please enter a word: ")

# Checks if the length of the word is greater than or equal to 10
if len(my_word) >= 10:
    print("Wow that's a long word!")
else:
    print("That's not that long of a word...")