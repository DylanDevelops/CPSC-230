'''Last Class'''
'''
1.  Work on your while loop from last class. If you need to, draw 
    your branching diagram back up on the board. If you make any 
    changes, re-upload a photo to Canvas. If you already wrote your
    loop, copy-paste it here. Add comments so I know what your loop
    is meant do do.
    
    NOTE: You can use the monitors at your tables to code together
'''

# Has the user enter the money amount
userMoney = int(input("Enter your money amount: "))
moneyInBank = True

# while they have money, subtract 1 every loop and break if no more money
while moneyInBank:
  if userMoney > 0:
    userMoney -= 1
    print(f"You have {userMoney} money!")
  else:
    moneyInBank = False

# Tells the user they have no more money if the while loop is broken
print("You are poor! L")


'''Strings'''
'''
2.  Use a while loop to create a list of classes a student is taking.
        - Ask the user to enter the course code (e.g. CPSC 230)
        - If they enter a course code, print out "Cool! [course] sounds 
          like a fun class!"
        - If they enter an empty string, break the loop.
'''

# declares the dependency variables
hasEmptyString = False
listOfClasses = []

# while the string is not empty, loop until that happens
while not hasEmptyString:
  userAnswer = input("Enter a class name: ")
  if userAnswer == "":
    print("That class doesn't exist!")
    hasEmptyString = True
  else:
    listOfClasses.append(userAnswer)
    print(f"{userAnswer} is a cool class!")

# print the classes in the console
print("Your classes are " + str(listOfClasses))

'''
3.  Write some code that asks the user to input all the fish species they can name. 
        - If the user types "done," break out of the loop.
        - Otherwise, Add the species they've inputted to a string, my_fish, 
          that stores the species they've input so far (use the + operator).
        - If the word "fish" is in the name (ie "Clown Fish and Trigger Fish, 
          but not Eel or Trout), print out "Double Fish!"
        - Print out my_fish at the end.
'''
### EXAMPLE CODE ###
print("!" in "Hello!")  # this is True
print("He" in "Hello!") # this is True
print("HE" in "Hello")   # this is False
print(" " in "This is Boring.") # this is True
print(" " in "ThisIsBoring.")   # this is False

# list all the dependant variables
my_fish = "" # to keep track of inputs
isDone = False
endingString = "done"
userInput = ""

# while the loop is still running do the following code
while not isDone:
  userInput = input("Enter a fish name: ")
  if userInput != endingString:
    if userInput != "":
      if "fish" in userInput:
        print("Double fish!")
      my_fish += f"\n{userInput}"
    else:
      print("Incorrect input. Try again or type \'done\'!")
  else:
    isDone = True 

# if the user types 'done', break the loop and run the code below:
print(f"Your fish are: {my_fish}")


'''
4.  Grab and print the species "Clown Fish" from the following 
    strings using string slicing.
'''

s1 = "Clown Fish"
s2 = "Nemo is a Clown Fish"
s3 = "Dory is not a Clown Fish"
s4 = "FishClown" # hint [::]
s5 = "hsiF nwolC"
s6 = "hesmivFx wnnweoglmC"

print(s1)
print(s2[10:20])
print(s3[14:24])
print(s4[4:9], s4[0:4]) # not sure how I would do this with [::] so hopefully this is okay for now
print(s5[::-1])
print(s6[::-2])

# Hint: what will this print out?
y = "piUk pudolYj oeVvliPGm  alnlntokG  NreeJvWeON"
print(y[::-1])
print(y[::-2])