# --------------------------------------------
# Dylan Ravel
# September 11, 2023
# Total Price Assignment
# References
# 1. https://www.w3schools.com/python/ref_func_round.asp
#
# README
# This code converts the purchase price of an item 
# to a new price that includes sales tax, while
# displaying the current status to the user.
# -----------------------------------------------

# Sets out variables that are needed for the rest of the program
salesTax = 7.25

# Greets the user and asks for the purchase price of the item, 
# converts it to a float (rounding to 2 decimal places)
# and finally stores it in a variable called "purchasePrice".
print("Thank you so much for shopping with us today!")
purchasePrice = round(float(input("What is the price of your item? $")), 2)

# Displays the sales tax and the purchase price to the user as a fake loading screen
print("\nAdding sales tax of " + str(salesTax) + "% to your purchase price of $" + str(purchasePrice) + "...")

# Calculates the new price by diving the sales tax by 100, 
# multiplying it by the purchase price and adding the 
# purchase price to it. Then it rounds it to 2 decimal places
newPrice = round((purchasePrice * (salesTax / 100)) + purchasePrice, 2)

# Displays the new price to the user and says goodbye
print("\nYour new total is $" + str(newPrice) + ".\nHave a great day!\n")