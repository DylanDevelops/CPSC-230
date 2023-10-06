# --------------------------------------------
# Dylan Ravel
# October 6th, 2023
# Homework 03 - fishVSFishes Assignment
#
# README
# Takes the user input of fish names and stores
# them in a set. Then, checks how big the set is,
# and prints the correct plural usage in the console.
# -----------------------------------------------

# Takes three inputs from the user storing them in variables
fish1 = input("Enter a fish species: ")
fish2 = input("Enter another fish species: ")
fish3 = input("Enter one last fish species: ")

# puts all three variables in a set
fishNameSet = {fish1, fish2, fish3}

# checks if the set has more than one item in it and prints the corresponding plural of fish  
if len(fishNameSet) > 1:
    print("The plural of your group would be \"fishes\"")
else:
    print("The plural of your group would be \"fish\"")