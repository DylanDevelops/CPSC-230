# Class Activities

'''For Loop Example'''
# pie = ["butter", "flour", "apples", "sugar"]

# for food in pie:
#     if food == "apple":
#         print(food, ": those you need to pick yourself")
#     else:
#         print(food, ": that you can get at the store")

# Classwork-----------------------------------------------
'''
1.  Make a list the classes you are taking this semester, then use a 
    for loop which loops throgh the list and prints out "[Class Name] 
    is one of my favotite classes!" for each class containing the word
    "computer" and "[Class Name] sounds like fun!" for all other classes.
'''
# CourseTitles = ["Computer Science 1", "Computer Science Colloquium", "Single Variable Calculus 1", "Engineering 101", "Film and Television Aesthetics", "FFC: Grand Challenges"]

# for i in CourseTitles:
#     if 'computer' in i.lower():
#         print(f"{i} sounds like fun!")
#     else:
#         print(f"{i} is one of my favorite classes!")

'''
2.  Ask a user to input a positive integer. If they enter a float, 0, or 
    a negative number (use isdigit()), keep asking (use a while loop).
    
    Once you have their number, calculate the factorial (see: 
    https://en.wikipedia.org/wiki/Factorial)for each number from 1 to that 
    number, and print it out (HINT, use range()).

    To test it, the answer for 5 is 120
'''

# userInput = input("Please enter a positive integer: ")

# while True:
#     if userInput.isdigit() and type(userInput) != float and userInput != "0":
#         userInput = int(userInput)
#         break
#     else:
#         userInput = input("That was not a valid positive integer! Please enter a positive integer: ")

# factorial = 1

# for i in range(1, userInput + 1):
#     factorial *= i

# print(f'The factorial of {userInput} is {factorial}.')


'''
3.  Ask the user to enter a number greater than 100 [userNum]. Include
    error handling so that your script keeps asking until the user enters
    an integer (using .isdigit()).
    
    Using a for loop, an if statement, and range(), calculate the sum 
    of all the even numbers between 1 and [userNum]. Print out the sum.
    
    HINT: Look at the code you wrote using modulo (%) to determine if a 
        number was odd or even.
    
    To test it, the answer for 110 is 3080
'''

# userInput = input("Enter a number that is greater than 100: ")
# total = 0

# while True:
#     if userInput.isdigit() and int(userInput) > 100:
#         userInput = int(userInput)
#         break
#     else:
#         userInput = input("That's not a valid number! Try again: ")

# for i in range(userInput + 1):
#     if i % 2 == 0:
#         total += i

# print(f"All even numbers between 1 and {userInput} is {total}.")

'''
4.  Update this piece of code to meet the following paramaters: 
        - Re-write the while loop as a for loop
        - Ask the user to enter their own string
        - Change the user's string so it only contains lowercase letters 
          and has no spaces at the start or end using string methods
        - Pick your own "favorite word" to highlight (mine is "Fish" in 
          the example below)
'''

i = 0
word = "If I were a fish..."
while i < len(word):
    print(word[i])
    if word[i] == "f":
        print("Fish starts with the letter F!")
        break
    else:
        i += 1

for i in word:
    if i == "f":
        print("Fish starts with the letter F!")
        break
    else:
        print(i)


'''
5.  Start working on your project.

    Create the "Start of game" section which establishes the chacacter
    dictionaries and asks the user to choose their character. You can
    edit this later of course, but try and outline it now.
'''

# I started this in my own script.