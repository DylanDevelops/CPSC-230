# --------------------------------------------
# Dylan Ravel
# August 28th, 2023
# Homework 01
# References
# 1. https://www.geeksforgeeks.org/taking-input-in-python/
# 2. https://www.programiz.com/python-programming/if-elif-else
#
# README
# This code has a conversation with the user and displays their answers inline.
# It also makes use of an if statement to give a different answer based on what they put.
# -----------------------------------------------

# says hello to the user in the terminal!
print("Hello kind person!")

# asks the user for their name and stores it in a variable called 'name'
print("What's your name?")
name = input()

# says hello the the user and displays the 'name' variable
print("Hello " + name + "!")

# asks the user for their name and stores it in a variable called 'favoriteColor'
print("What is your favorite color?")
favoriteColor = input()

# If their favorite color matches my favorite color, you get a special message
if (favoriteColor == "Orange" or favoriteColor == "orange"):
    # displays this line if their favorite color is 'Orange' or 'orange' (my favorite color)
    print("Thats awesome, " + name + "! My favorite color is " + favoriteColor + " too!")
else:
    # displays this line if their favorite color is not 'Orange' or 'orange' (not my favorite color)
    print("Thats awesome, " + name + "! You are a little less cool because your favorite color is " + favoriteColor + ", but it's okay!")