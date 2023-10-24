## lists
myFishList = ["Tuna", "Eel", "Goldfish", "Carp", "Shark"]

# print(myFishList[1])

# for fish in myFishList:
#     print(fish + "s are cool!")

days = ["Monday","Tuesday", "Wednesday",
        "Thursday","Friday","Saturday",
        "Sunday"]

# for day in days:
#     if day == "Friday":
#         print("TGIF")
#     elif day == "Saturday":
#         print("Sleep in!")
#     elif day == "Monday":
#         print("Keep on keeping on!")

'''Indexing'''

myFishList = ["Tuna", "Eel", "Goldfish", "Carp", "Shark"]
# print(days[0])
# print(myFishList[2:4])
# print(myFishList[::-1])

# print(myFishList)

'''List Mutability'''
# myFishList[0] = "Whales"
# print(myFishList)

'''Nested Lists (row by column)'''
#              0       1       2
database = [["Name", "Age", "Status"],          # 0
            ["Bill",  24,   "Active Member"],   # 1
            ["Kara",  41,   "Not Paid"],        # 2
            ["Tony",  95,   "Retired Member"]]  # 4

#### how do I grab Bill's age?
# print(database[0][1])

'''Looping through Nested Lists'''
   #           0       1       2
database = [["Name", "Age", "Status"],          # 0
            ["Bill",  24,   "Active Member"],   # 1
            ["Kara",  41,   "Not Paid"],        # 2
            ["Tony",  95,   "Retired Member"]]  # 4

# start looping through rows
# for row in database:
#     # then columns
#     for cell in row:
#         print(cell)

'''Tuples'''
my_tup = (1,2,3,4,5)

# print(my_tup[0])
# my_tup[0] = 0

'''Arbutrary Keyword Arguments'''
### *args and *kwargs
### use any variable name, the key syntax is the *

### Use *args for variable number of arguments
### creates a tuple
def myFun(*argv):
    for arg in argv:
        print(arg)
    return(argv)

''' MORE WITH LISTS '''
'''List Operators (+ * - /)'''

my_list = [1,2,3,4]
# print(my_list * 5)

my_list2 = [5,6,7,8]
# print(my_list + my_list2)

## NOTE: Cannot add lists to ints
# print(my_list + 6)

'''comparisons/logical operators'''
[1,2,3] == [1,2,3,4]

[1,2,3,4] > [1,2,3,3]

# print([1,5,2,2,2,2] < [1,6])

'''Non-modifying List Methods'''

fruit = ["apple", "orange", "banana", "grape", "apple", "apple"]
# print(fruit)

# print(fruit.count("apple"))

# print(fruit.index("apple"))

'''Modifying List Methods'''

### append
# fruit.append("cherimoya")
# print(fruit)

### pop
# popped_element = fruit.pop()
# print(popped_element)
# print(fruit)

### insert
# fruit.insert(0, "apple")
# print(fruit)

### remove
# fruit.remove("orange")
# print(fruit)

# fruit.remove("apple")
# fruit.remove("apple")
# print(fruit)

### sort
m = [4,3,2,6,7,8]
# m.sort()
# print(m)

''' List functions '''
m = [4,3,2,6,7,8]

### len
# print(len(m))

### min, max
# print(min(m))
# print(max(m))

### sum
# print(sum(m))

## sorted
## differnt than m.sort()
m = [4,3,2,6,7,8]
# m.sort()
# print(sorted(m))
# print(m)

## to actually store the sorted value assign to a new variable
# m = sorted(m)

## split and join, string methods but often used with lists
words = "Welcome to the ministry of silly walks".split(" ")
# print(our_words)

words_ = "_".join(words)
# print(words_)

### mini activity
'''
Word Guessing Game!
- Create a list of 5 fish (someFish) (or some other list of things)
- Copy paste -> randint(0,len(someFish)-1) <- to save a random word 
  from your list as a new variable (oneFish)
- Convert oneFish into a list using the list() operator
- Shuffle oneFish using random.shuffle(oneFish)
- Join the newly shuffled characters using the list.join() method
- Print the shuffled string and ask your table-mates to unscramble 
  the wordd and guess the fish
'''

import random

someFish = ["Goldfish", "Salmon", "Catfish", "Tuna", "Clownfish"]
oneFish = list(random.choice(someFish))

theAnagram = oneFish.copy()
random.shuffle(theAnagram)

print("Try to guess the word that these letters make up.")
print(f"Your letters: \'{' '.join(theAnagram)}\'")
userGuess = input("Your guess: ")

analyzing = True
while analyzing:
    for word in someFish:
        if userGuess.lower() == word.lower() and userGuess.lower() == ''.join(oneFish).lower():
            print("That was correct!")
            analyzing = False
            break
    else:
        print("That was not correct. Try again!")
        userGuess = input("Your guess: ")


'''
Mutability and Functions
'''
## immutable objects, new variable created in the function
## only exists in the function namespace
def my_f(x):
    print("1)", id(x))
    x = 24
    print("2)",id(x))

# h = 2
# print("3)",id(h))
# my_f(h)
# print("4)",id(h))

## mutable objects, change variable within the function
## variable remains changed outside the function
def my_f2(x):
    print("1)", id(x))
    x[0] = 24
    print("2)", id(x))

# h = [1,2,3]
# print(h)
# print("3)", id(h))
# my_f2(h)
# print("4)", id(h))
# print(h)


def add_student(l, studentName):
    l.append(studentName)

students = ["Frasier", "Niles", "Daphne"]

add_student(students, "Roz")
# print(students)

'''returning multiples, and multiple assignment'''
import random

def roll_3_dice():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)

    return [d1,d2,d3]

dice_list = roll_3_dice()
# print(dice_list)

die1, die2, die3 = roll_3_dice()
# print(die1)
# print(die2)
# print(die3+6)