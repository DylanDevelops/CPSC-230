# CLASSES

class Cat():
    sound = "meow"
    diet = "Carnivore"

myCat = Cat()
print(myCat.sound)
print(myCat.diet)



'''Simple Square'''
## NOTE: The __init__ method is a constructors. Constructors are used to 
## initialize the object’s state. It runs as soon as an object of a class  
## is instantiated. It's is useful if you want anytihng to run when you 
## create your object, but it is not required.

class Square():    ## generally folks use a capital leter
    shape = "square"
    def __init__(self, side):
        # What do you want to run when you create a new square?
        self.side_length = side
        print("Hello There! I am a Square!")

# square1 = Square(4)
# square2 = Square(10)

# print(square2.side_length)
# print(friend.side_length*2)
# print(square1.shape)



'''Advanced Square'''
class Square():
    shape = "square"
    side_count = 4

    def __init__(self, side):
        self.side_length = side
        print("Hello There! I am a Square!")

    # you can return things with instance methods and 
    # store them in new variables later
    def area(self):
        return(self.side_length ** 2)

    # these functions can take in both class attributes (like side_count)
    # and instance attributes (like side_length)
    def perimeter(self):
        return(self.side_count * self.side_length)

    def scaleSize(self, scaler):
        self.side_length *= scaler

# testSquare = Square(5)

# print(testSquare.area())
# print(testSquare.perimeter())

# bob = Square(4)
# print(bob.side_length)
# bob.scaleSize(2)
# print(bob.side_length)



''' Another example'''
class Dog():

    family = "mammal"
    species = "dog"
 
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    # A sample method
    def describe(self):
        print("I'm a", self.species)
        print("My breed is", self.breed)
    
    def walk(self):
        if self.age < 2:
            return 4
        elif self.age > 2 and self.age < 6:
            return 2
        else:
            return 1

 
# rover = Dog("Lab", 3)
# rover.describe()
# walkLength = rover.walk()
# print("I should walk for", walkLength, "miles per day!")