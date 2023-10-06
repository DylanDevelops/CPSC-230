# --------------------------------------------
# Dylan Ravel
# October 6th, 2023
# Homework 03 - Total Price Assignment
# Collaborators
# 1. Divi Newton
# References
# 1. https://www.w3schools.com/python/ref_func_round.asp
#
# README
# This code converts the purchase price of an item 
# to a new price that includes sales tax, while
# displaying the current status to the user. It also
# now handles input errors.
# -----------------------------------------------

# Declares the sales tax variable
salesTax = 7.25

# Greets the user and asks them to put in a price
print("Thank you so much for shopping with us today!")
purchasePrice = input("Please enter the price of your item: $")

# declares true as a general statement to run the while loop
while True:
    # checks if the purchasePrice is a number and checks if the purchase price is greater than 0
    if purchasePrice.isdigit() and float(purchasePrice) > 0:
        # rounds purchase price to 2 decimal places like money values should be
        purchasePrice = round(float(purchasePrice), 2)
        # tells the user it is doing the calculations before breaking out of the loop
        print(f"\nAdding sales tax of {salesTax}% to your purchase price of ${purchasePrice}...")
        break
    else:
        # if it is not a number or if it is 0 or below, it will tell the user it isn't valid and allow them to input again
        print("That's not a valid price!")
        purchasePrice = input("Enter a valid price: $")

# Once the while loop is broken out of, it does the calculations to get the new price
newPrice = round((purchasePrice * (salesTax / 100)) + purchasePrice, 2)

# prints out the new price in the console
print(f"\nYour new total is ${newPrice}.\nHave a great day!\n")