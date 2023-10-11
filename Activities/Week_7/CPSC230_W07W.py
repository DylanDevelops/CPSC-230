'''for'''

numbers = [1,2,3,4,5,6]
# for fish in numbers[::2]:
#     print(fish)
#     print("Hello your number is :" + str(fish))


'''range()'''

# for i in range(1,6):
#     print("Easier with range: " + str(i))

'''Example: Evens'''

# for i in range(0,10):
#     if i%2 == 0:
#         print("EVEN")
#     else:
#         print("ODD")

## humuhumunukunukuapuaa
##  It's a great fish! 
##  https://en.wikipedia.org/wiki/Reef_triggerfish

h_count = 0
u_count = 0
m_count = 0
k_count = 0
a_count = 0
n_count = 0
p_count = 0

# for letter in "humuhumunukunukuapuaa":
#     if letter == "h":
#         h_count += 1
#     elif letter == "u":
#         u_count += 1
#     elif letter == "m":
#         m_count += 1
#     elif letter == "k":
#         k_count += 1
#     elif letter == "a":
#         a_count += 1
#     elif letter == "n":
#         n_count += 1
#     else:
#         p_count += 1

# print("H-Count: " + str(h_count))
# print("U-Count: " + str(u_count))
# print("M-Count: " + str(m_count))
# print("K-Count: " + str(k_count)) 
# print("A-Count: " + str(a_count))
# print("N-Count: " + str(n_count))
# print("P-Count: " + str(p_count))


'''Lists'''

nums = [1,2,3,4,5,6,7,8,9,10,11,12]

# for n in nums:
#     if n%3 == 0:
#         print("this is divisible by 3")

names = ["Abby", "Billy", "Cathrine", "Devon","Elon", "Fred"]

# for name in names:
#     print("Hello " + name + "!")


'''
Activity Together
    Re-write this while loop as a for loop
'''
i = 0
word = "No need for while loops here!"
while i < len(word):
    if word[i] == "f":
        print("Fish starts with the letter F!")
        break
    else:
        print(word[i])
        i += 1

for i in word:
    if i == "f":
        print("Fish starts with the letter F!")
        break
    else:
        print(i)


''' 
Activity Together
    Loop through the ingredients below and print
    out each one like a shopping list. If the food
    is an appple, tell the user they have to go apple
    picking to get them. If the food is anything else, 
    tell the user they can get it at the store.
'''

pie = ["butter", "flour", "apples", "sugar"]

for i in pie:
    if i == "apples":
        print(f"Go apple picking to get some {i}!")
    else:
        print(f"Go to the store to get {i}!")