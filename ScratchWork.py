userNum = input("Enter a number greater than 100: ")
while not userNum.isdigit():
    print("That's not a number!")
    userNum = input("Enter a number greater than 100: ")

sum = 0
number = 0
while number <= int(userNum):
    if number % 2 == 0:
        sum += number
    number += 1
print(sum)