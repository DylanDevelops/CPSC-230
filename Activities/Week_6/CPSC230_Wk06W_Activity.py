'''
1.  Write a while loop asking students to enter the names of the classes
    they are taking this semester. They should be able to enter DONE when
    they have no classes to list. Each time they enter a class, print out
    "Wow, [Class Name], sounds fun!". If the class contains the word 
    "computer" (like CPSC 230: Computer Science 1) use string methods to 
    change the text to be entirely upper-case. (you can also modify to 
    highlight your own favorite topic other than "computer")
'''

userInput = input("Enter a class you are taking: ")

while True:
    if "DONE" not in userInput:
        if "computer" in userInput.lower():
            print(f"Wow, {userInput}, sounds fun!".upper())
        else:
            print(f"Wow, {userInput}, sounds fun!")
        
        userInput = input("Enter another class you are taking: ")
    else:
        print("You have exited the class selector!")
        break

'''
2.  Ask the user to enter a number greater than 100 [userNum]. Include
    error handling in a while loop so that your script keeps asking 
    until the user enters an integer (using .isdigit()).
    
    Using another while loop and modulo, calculate the sum of all the 
    even numbers between 1 and [userNum]. Print out the sum.
    
    HINT: Look at the code you wrote using modulo (%) to determine if 
        a number was odd or even. (and look at the example code from 
        lecture today)
'''

userInput = input("Enter a number that is greater than 100: ")

while True:
    if not userInput.isdigit() or int(userInput) <= 100:
        userInput = input("Please enter a valid integer that is greater than 100: ")
    else:
        i = 0
        total = 0
        while i <= int(userInput):
            if i % 2 == 0:
                total += i
            i += 1
        print(f"The sum of all even numbers between 1 and {userInput} is: {total}.")
        break
    

'''
3.  Update this piece of code to meet the following paramaters: 
        - Ask the user to enter their own string
        - Use string methods to change the user's string so it only 
          contains lowercase letters and has no spaces at the start or end
        - Pick your own "favorite word" to highlight (mine is "Fish" in 
          the example below)
'''
i = 0
word = input("Please enter a string: ").lower().strip()
while i < len(word):
    print(word[i])
    if word[i] == "o":
        print("My dog's name starts with \"o\" and is \"Oreo!\"")
        break
    else:
        i += 1

