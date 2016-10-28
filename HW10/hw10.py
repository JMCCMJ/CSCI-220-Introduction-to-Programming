#hw10.py
#Jan-Michael Carrington
#Purpose: To construct a class for a deck of cards.
#Authenticity: I certify this code is my own work.
##
##True or False
##1. True
##2. False
##3. False
##4. False
##5. True
##6. True
##7. False
##8. False
##9. False
##10. True

##Multiple Choice
##1. B
##2. C
##3. D
##4. B
##5. C
##6. D
##7. C
##8. A
##9. C
##10. C
##
##Discussion
##1. Instance variables are able to be passed around in a class among multiple
##methods. A regular variable acts as a local variable within a method in a class.
##2.
##(a) A method is kind of like a function but is inside of a class. It can be
##used by calling it from an object such as example.run() where run is the method.
##(b) An instance variable is a variable that is accessible within all of a class.
##For example, self.example would be an instance variable within a class.
##(c) A constructor is a function that creates a new object. In a class
##it is the __init__ method.
##(d) An accessor is a method that returns a value of one or more of an object's
##instance variable(s), but does not modify the object. For example,
##example.getValue() that getValue() is the accessor that returns a certain
##value from the object example.
##(e) A mutator is a method that changes the state of an object. For example,
##example.Add() where Add() changes an instance variable within the object example.
##3. The output is:
##Clowning around now.
##Creating a Bozo from: 3
##Creating a Bozo from: 4
##Clowning: 3
##18
##9
##Clowning: 2
##12
##Clowning: 8
##64
##16


from random import *

#creating class
class Deck:
    def __init__(self,rank,suit):
        self.card = []
        #suits = ['d','c','h','s']
        #ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.card.append(rank)
        self.card.append(suit)
        #print(self.card)
    def getRank(self):
        self.card_rank = self.card[0]
        return self.card_rank
    def getSuit(self):
        self.card_suit = self.card[1]
        return self.card_suit
    def BJValue(self):
        card_rank = self.card[0]
        if card_rank == 11:
            card_rank = 10
            return card_rank
        elif card_rank == 12:
            card_rank = 10
            return card_rank
        elif card_rank == 13:
            card_rank = 10
            return card_rank
        else:
            return card_rank
    def __str__(self):
        self.card_suit = self.getSuit()
        self.card_rank = self.getRank()
        #print(self.card_rank)
        suit_string = ""
        rank_string = ''
        if self.card_suit == "s":
            suit_string = "Spades"
        elif self.card_suit == "d":
            suit_string = "Diamonds"
        elif self.card_suit == "h":
            suit_string = "Hearts"
        else:
            suit_string = "Clubs"
            
        if self.card_rank == 1:
            rank_string = "Ace"
        elif self.card_rank == 2:
            rank_string = "Two"
        elif self.card_rank == 3:
            rank_string = "Three"
        elif self.card_rank == 4:
            rank_string = "Four"
        elif self.card_rank == 5:
            rank_string = "Five"
        elif self.card_rank == 6:
            rank_string = "Six"
        elif self.card_rank == 7:
            rank_string = "Seven"
        elif self.card_rank == 8:
            rank_string = "Eight"
        elif self.card_rank == 9:
            rank_string = "Nine"
        elif self.card_rank == 10:
            rank_string = "Ten"
        elif self.card_rank == 11:
            rank_string = "Jack"
        elif self.card_rank == 12:
            rank_string = "Queen"
        elif self.card_rank == 13:
            rank_string = "King"
        full_string = rank_string + " of " + suit_string + "."
        return full_string
        


def main():
    num_cards = eval(input("Enter the number of cards to generate: "))
    suits = ["s","d","c","h"]
    for i in range(num_cards):
        suit_num = randint(0,3)
        card_num = randint(1,13)
        if suit_num == 0:
            suit = suits[0]
        elif suit_num == 1:
            suit = suits[1]
        elif suit_num == 2:
            suit = suits[2]
        elif suit_num == 3:
            suit = suits[3]

        card = Deck(card_num,suit)
        print(card)
        BJVal = card.BJValue()
        print(BJVal)
        print()
        
main()
