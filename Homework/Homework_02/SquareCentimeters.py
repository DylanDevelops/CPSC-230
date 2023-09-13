# --------------------------------------------
# Dylan Ravel
# September 12, 2023
# Homework 02 - Square Centimeters Assignment
# Collaborators:
# 1. Divi Newton
# 2. Sammy Rokaw
# References
# 1. https://www.tutorialspoint.com/python-program-to-calculate-the-cube-root-of-the-given-number
#
# README
# This code converts the volume of a tank in liters to the
# footprint of the tank in square centimeters, while
# displaying the current status to the user.
# -----------------------------------------------

# Imports the math module
import math

# Greets the user, asks for the volume of the tank in liters, 
# converts it to a float and finally stores it in a variable 
# called "tankInLiters". It also asked for a reptile species
# just for fun.
print("Welcome to reptile tank calculator!")
tankInLiters = float(input("Please enter the volume of your tank in liters: "))
speciesOfReptile = input("Please enter the species of your reptile: ")

# Calculates the side length of the tank in centimeters by
# taking the cube root of the tank in liters times 1000.
sideLengthInCm = math.pow(tankInLiters * 1000, 1/3)

# Then it calculates the footprint of the tank by squaring
# the side length in centimeters and rounding it to 2 decimal
# places.
footprintOfTank = round(math.pow(sideLengthInCm, 2), 2)

# Displays the footprint of the tank to the user.
print("The footprint of your" + speciesOfReptile + "'s tank is " + str(footprintOfTank) + " square centimeters.")