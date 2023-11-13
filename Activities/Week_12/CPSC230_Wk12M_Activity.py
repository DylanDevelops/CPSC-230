# Class Activities + Review (Classes)


'''
1.  Create a class called Card. The card should have two instance attributes:
        - value: (2-10, Ace, Jack, King, Queen)
        - suit: (hearts, spades, diamonds, clubs)
    Make sure you write an __init__ method to be sure to assign value and suit
    to your card object.

    Then write three instance methods:
        - getSuit() which returns the suit of the card.
        - getValue() which returns the value of the card (in terms of blackjack).
          numbered cards (2-10) are worth their respective points. Face cards (Jack, 
          King, Queen) are worth 10 points. And an Ace is worth 11.
        - __str__() (note the two underscores before and after) which returns a string
          "[value] of [suit]" (e.g. "Ace of Spades", or "Queen of Hearts"). The 
          __str__() method is another special method like __init__. It tells python 
          what to print when you call print(object).
'''

class Card():
    def __init__(self, cardValue, cardSuit):
        self.value = cardValue
        self.suit = cardSuit

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def getSuit(self):
        return self.suit

    def getValue(self):
        if self.value.isdigit():
            return int(self.value)
        else:
            if self.value.lower() == 'ace':
                return 11
            else:
                return 10

card01 = Card("Ace", "Hearts")
print(card01)
print(card01.getValue())



'''
2.  Create another Class called Deck. This class should have two attribute.
        - suits (a list of suits ['hearts', 'spades', 'diamonds', 'clubs'])
        - values (a list of values ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'King', 'Queen', 'Ace'])
    
    Create an __init__ method for Deck that creates the deck of 52 cards. Each of those
    52 cards should be created using the Card class.
        HINT: start off with an empty list self.cards = []
        HINT: You can use a double for-loop and your Card class to create your deck
              more easily than copy-pasting all 52 options
    
    Define an instance method, shuffle() which shuffles the order of your deck.
    look up some of the functions in the random library for this
        - 
    Define an instance method, draw(), which "deals" the last card in cards by removing
    it from cards, and returning it (hint: pop).

    Create a Deck object, shuffle it, and print out the result of drawing 5 cards

    BONUS: Also return the cumulative value using the getValue function in your Card
    class
'''