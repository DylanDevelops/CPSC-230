# Class Activities + Review (Week2 Wednesday)

# Classwork-----------------------------------------------

'''
1.  The code below calculates the area of a triangle. Add comments to each
    line explaining what it is doing.
'''
print("--- Problem 1 ---")

# Defines the variables b and h and assigns them values
b = 10
h = 3

# Multiplies b and h and assigns the value to x
x = b * h

# Divides x by 2 and assigns the value to area
area = x/2

# Prints the value of area to the console
print(area)


'''
2.  What type is x? Add a line of code that tells the user the type in 
    the termial.
'''
print("--- Problem 2 ---")

# Assigns 10 to x
x = 10

# Prints the type to the console
print(type(x))

'''
3.  The == is the "equal to" operator. It returns True if two objects are 
    equal, and False if they are not (see below for examples). Add a line 
    of code to check if the Boolean "True" is equal to 1. Display the result.
'''
print("--- Problem 3 ---")
# examples
1 == 2 # False
3 <= 10 # True

# Prints the result of the comparison to the console
print(True == 1)

'''
4. Print the type of each of these variables.
'''
print("--- Problem 4 ---")

# Assigns a bunch of values to variables
my_int = 9
my_string = "quod erat demonstrandum"
my_list = [1,2,3,4,5]
my_dict = {"name": "Jessie", "age": 27, "team": "Rocket"}
my_set = {1,1,2,3,5,8,13}

# Prints the type of each of the variables
print(type(my_int))
print(type(my_string))
print(type(my_list))
print(type(my_dict))
print(type(my_set))

'''
5.  Write some code that uses a boolean operator to check whether
    7 * 2 + 4 / 9 is bigger than 9 * 10 / 2 + 3 - 4 and displays 
    the result.
'''
print("--- Problem 5 ---")

# Assigns the values to x and y
x = 7 * 2 + 4 / 9
y = 9 * 10 / 2 + 3 - 4

# Checks if x is greater than y and prints the result to the console
print("x is " + str(x))
print("y is " + str(y))
print(x > y)


