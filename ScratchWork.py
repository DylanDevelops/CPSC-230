temperature = 75.3
isItRaining = True # Needs to be capitol "T"

if temperature <= 60 and isItRaining: # needs colon
    print("You need a jacket and umbrella!")

elif temperature > 60 and isItRaining: # needs colon
    print("You don't need a jacket only an umbrella!") # needs quotation marks

elif temperature <= 60 and not isItRaining: #needs colon
    print("You need a jacket but not an umbrella!")

elif temperature > 60 and not isItRaining: # Needs to be lowercase "not" and colon
    print("You need some sunscreen!")

else: #needs colon
    print("WHERE ARE YOU?")