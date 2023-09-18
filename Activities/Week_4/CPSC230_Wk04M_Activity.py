'''
1.  Use this space to test out your answers for the quiz. Use 
    comments to make notes about how you answered the question 
    and/or what concepts you would like to focus on in preparation 
    for the midterm.
'''
### Practice Question 1

num01 = 1 + 1
num02 = 10 / 5
num03 = 10 // 5
num04 = 1 * 2.0
num05 = 10 % 8

print(type(num01))
print(type(num02))
print(type(num03))
print(type(num04))
print(type(num05))

### Practice Question 2

userAnswer = int(input("How many classes are you taking? "))

if userAnswer > 0 and userAnswer <= 3:
    print("That sounds pretty manageable.")

elif userAnswer == 4:
    print("Cool, me too!")

elif userAnswer >= 4:
    print("Wow, you must be busy!")

### Practice Question 3

bestGame = {"Game Title": "The Last of Us", "Main Character": "Joel", "Platform": "PC, Playstation"}

if len(bestGame["Game Title"]) >= 10:
    print("Wow, that's a long name!")

elif len(bestGame["Game Title"]) < 10:
    print("Cool, sounds fun!")

''' 
2.  Emojis. Use pip install to install the emojis library.
        To install: pip install emojis

    Use it to print a short story in the terminal where every
    noun is replaced by an emoji.
        https://www.webfx.com/tools/emoji-cheat-sheet/

    If you are having issues with pip, you may need to reinstall
    follow instructions here: https://realpython.com/what-is-pip/
'''

# import emojis
# emojified = emojis.encode("There is a :snake: in my boot !")
# print(emojified)

# Imports the emojis package after installing it using "pip install emojis"
import emojis

# Prints out a short story with emojis replacing any nouns
print(emojis.encode("I walked to my :house_with_garden: and saw my :dog:. I then went to pet my :dog: and my :cat: got mad at me. I pet my :cat: and my :dog: at the same time and we lived happily ever after."))

'''
3.  Find, install, and use one other library of your choosing.
    You can just google "interesting libraries in python"

    NOTE: It is normal to have issues installing libraries. Python
    is open-source, so sometimes working with less commonly used 
    libraries is a pain. It's not you! Google is your friend here. 
'''

# Imports the dadjokes package after installing it using "pip install dadjokes" (https://pypi.org/project/dadjokes/
from dadjokes import Dadjoke

# Prints Tells the user it is retrieving a dad joke
print("Here's a dad joke:")

# Creates a dadjoke
dadjoke = Dadjoke()

# Prints out the dad joke
print(dadjoke.joke)