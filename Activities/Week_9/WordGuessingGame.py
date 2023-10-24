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