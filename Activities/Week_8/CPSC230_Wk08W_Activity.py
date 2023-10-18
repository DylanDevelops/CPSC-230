# Class Activities


'''
1.  Distance Formula
    NOTE: Add default arguments for pt1 (pt1 = [0,0])
    Write a functions that calculates the distance between two points
    https://en.wikipedia.org/wiki/Distance (just 2D distance is fine)
        - The function should take 2 lists as inputs
            - pt1 = [x1, y1]
            - pt2 = [x2, y2]
        - The function should return the distance
        - Remember that a distance cannot be a negative number
        - BONUS 01: Write your script so that the user can enter the 
          X and Y coordinates of their two points
        - BONUS 02: Write your function so it only returns 3 
          significant digits
    
    NOTE: Add to your function to give the user the option to cauclulate 
          either Euclidean or Manhattan distance (Euclidean) is the formula 
          you used Monday, Manhattan is linked here:
          https://algodaily.com/lessons/what-is-the-manhattan-distance
'''
## The answer with these coordinates will be 13.928
pt1 = [5, 2]
pt2 = [10, 15]




#### D&D Dice roller

'''
2.  Write a function dice_roller() which takes in in an argument, sides, 
    and uses the random.randint() function to "roll" a die with the set
    number of sides. Set the default value to 20. Return the value.
'''

import random

def dice_roller(sides = 20):
  return random.randint(1, sides)

print(dice_roller())


'''
3.  Write a while loop that uses keeps printing "not yet!" until the random number
    generator rolls a "nat20" using your dice_roller function
    https://dungeonsdragons.fandom.com/wiki/Natural_20
'''

while dice_roller() != 20:
  print("Has not rolled 20...")

print("Finally rolled 20!")

'''
4.  Write a for loop that loops through a list of the most commonly available dice 
    types (https://easyrollerdice.com/blogs/rpg/dd-dice).
        - use your dice_roller() function to roll the die
        - tell the user which die they rolled, and their result
          (ie: "You rolled a D4 and got 3!")
'''



'''
5.  BONUS extension to #4
        - BONUS 01: Include a special message if they got the highest number on 
          the die (ie a 20 on a 20 sided dice)
        - BONUS 02: Include a special message if they got the lowest number on 
          the die (ie a 1)
'''


