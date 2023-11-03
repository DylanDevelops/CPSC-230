# creating a dictionary
student = {"name": "Carl",
"age": 21,
"major": "Electrical Engineering",
"course": ["CPSC392", "CPSC231", "MATH303", "CS618"]}

'''Indexing'''
#print(student["major"])

'''Dictionaries are Mutable'''
'''Adding items'''
student["ChapmanID"] = "0123456"
# print(student)

student["course"] = ["CPSC298", "CPSC393", "CS500", "MGSC310"]
# print(student)

'''keys()'''
# print(student.keys())
# for k in student.keys():
#     print(k)

'''values()'''
# print(student.values())
# for v in student.values():
#     print(v)

'''items()'''
# print(student.items())
# for k,v in student.items():
#     print(k)
#     print(v)

'''get()'''
'''note that get() has two possible arguments, the key, and the value to
   return if the specified key does not exist'''
# n = student.get("name", "NA")
# print(n)

'''HAPPY BIRTHDAY!'''
# student["age"] = student.get("age", 18) + 1
# print(student)

'''New pets!'''
# student["pets"] = student.get("pets",0) + 1
# print(student)

'''Get Example: dice rolls'''
import random

rolls = {}                      ## create empty dictionary
for sim in range(0,1000):       ## roll a 6-sided dice 1000 times
    roll = random.randint(1,6)

    ## if the "roll" (int) key does not exist, create that key
    ## and add one to the value. If the "roll" key does exist
    ## add one to the total
    rolls[roll] = rolls.get(roll,0) + 1

# print(rolls)

# for num, count in rolls.items():
#     print(str(num) + " was rolled " + str(count) + " times.")


'''the in operator with Dictionaries'''
favorite = {"John": "Tuna",
            "Randall": "Eel",
            "Kim": "Goldfish",
            "Linda": "Sculpin",
            "Sarah": "Gar"}

## check if the student is in there
# name = input("Who's favorite do you want? ")
# print(name in favorite) ## check if that key is there
# print(favorite[name])   ## print value

## if not there, add them
# name = input("Who's favorite do you want? ").capitalize()

# if name in favorite:
#     print(favorite[name])
# else:
#     print("This student did not list their favorite fish")
#     fish = input("Please enter their favorite fish now: ")
#     favorite[name] = fish

# print(favorite)

'''SETS'''
my_set1 = {"February", "January", "April"}
my_set2 = {1,1,1,1,1,1,3,5,9,11}

# print(my_set1)
# print(my_set2)

'''creating sets'''
my_list = [10,5,5,9,3,4,9,1,2,6,8,9,4,2,5,7]
my_list_to_set = set(my_list)
# print(my_list_to_set)

'''Mutable objects inside a set'''
### But change to tuples and it will work
# my_mutables = {[1,2,3,4], [5,6,7,8]}
# print(my_mutables)

'''Mixing types'''
my_mixed_set = {1, "ant", "blue", (1,2)}
# print(my_mixed_set)

'''Set Methods'''
my_set1.add("June")
# print(my_set)

my_set1.add("February")
# print(my_set)

my_set1.remove("January")
# print(my_set)


odds = {1,3,5,7,9}
evens = {2,4,6,8,10}
pos_ints = {1,2,3,4,5,6,7,8,9,10}
primes = {2,3,5,7}

'''union'''
# print(odds | evens)
# print(odds.union(evens))

'''intersection'''
# print(odds & pos_ints)
# print(odds.intersection(pos_ints))

'''difference'''
# print(odds - primes)
# print(odds.difference(primes))
# print(primes - odds)
# print(primes.difference(odds))

'''symmetric difference'''
# print(odds^primes)
# print(odds.symmetric_difference(primes))

# print(primes^odds)


# if you switched the order, would the answer be different?


'''
Look through this code askinbg two friends their favorite music artists.
Comment on each line describing what is happening.
'''
songs = {}

for friend in range(0,2):
    f = "friend" + str(friend)

    print("Welcome " + f)

    songs[f] = set()

    artist = input("Name an artist you like, enter a blank string to end: ").lower()
    while artist != "":
        songs[f].add(artist)
        artist = input("Name an artist you like, enter a blank string to end: ").lower()

print("GREAT JOB!")
print("The artists you have in common are: ", ",".join(list(songs["friend0"] & songs["friend1"])))