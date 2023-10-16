# Class Activities

'''
0. Call Stacks
Look through these functions and try to guess what will print out
when a() is called on line 26
'''

def a():
    fish = "Ribbon Eel"
    print("my favorite fish is a " + fish)
    b()
    print("my favorite fish is a " + fish)

def b():
    fish = "Electric Eel"
    print("my favorite fish is a " + fish)
    c()
    print("my favorite fish is a " + fish)

def c():
    fish = "Garden Eel"
    print("my favorite fish is a " + fish)

# what will print out?
a() 

'''
Since it jumps around, here is my guess:

my favorite fish is a Ribbon Eel
my favorite fish is a Electric Eel
my favorite fish is a Garden Eel
my favorite fish is a Electric Eel
my favorite fish is a Ribbon Eel

'''

'''
1.  Write a function, tens(), that takes in an integer and returns True if 
    the integer is divisible by 10, and False if it is not.
'''

def tens(theNumber):
    if theNumber % 10 == 0:
        return True
    else:
        return False

userInput = int(input("Please enter a whole number: "))
print(f"Is {userInput} divisible by 10? Answer: {tens(userInput)}.")


'''
2.  Let's re-visit our art-piece dictionary problem.
    
    Create a list of 5 dictionaries containing the title, artist, and cost 
    of 5 different paintings in a museum (or any 5 dictionaries containing
    the same 3 keys to define an object).

    Write a function that 
        - takes a dictionary as an input and tells the user the title, 
          artist, and cost in sentence form.
        - returns the cost of the painting as a float

    Write a for-loop to go through your list of dictionarues, adding up
    the cost of each painting along the way. Tell the user the total 
    value of all the paintings in your museum 
'''

# First part of the question

art = [
    {"title": "The Starry Night", "artist": "Vincent van Gogh", "cost": 1},
    {"title": "The Scream", "artist": "Edvard Munch", "cost": 2},
    {"title": "The Persistence of Memory", "artist": "Salvador Dalí", "cost": 3},
    {"title": "The Last Supper", "artist": "Leonardo da Vinci", "cost": 4},
    {"title": "The Creation of Adam", "artist": "Michelangelo", "cost": 5}
]

def artInfo(artPiece):
    print(f"Name: {artPiece['title']} - Artist: {artPiece['artist']} - Cost: ${artPiece['cost']}")
    totalCost = 0
    for painting in art:
        totalCost += painting['cost']
    print(totalCost)


userArtPiece = int(input("There are 5 paintings. Get information on the painting by entering the number (1, 2, 3, 4, 5): "))
artInfo(art[userArtPiece - 1])

'''
3.  Distance Formula
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
'''
## The answer with these coordinates will be 13.928
pt1 = [5, 2]
pt2 = [10, 15]



'''
4.  BONUS CHALLENGE: Global Distance
    Write a functions that calculates the distance between two points on earth
    https://www.igismap.com/haversine-formula-calculate-geographic-distance-earth/
    You will yse the Haversine formula (link above)
        - The function should take 2 lists as inputs (you can get lattitude and
          longetude using google maps)
            - pt1 = [lattitude1, longetude1]
            - pt2 = [lattitude2, longetude2]
        - The function should return the distance in kilometers
        - Don't be afraid to dig around on Google!
'''