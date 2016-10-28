#hw11.py
#Jan-Michael Carrington
#Purpose: To construct a class for a deck of cards.
#Authenticity: I certify this code is my own work.
##
##True or False
##1. False
##2. True
##3. False
##4. False
##5. False
##6. False
##7. False
##8. True
##9. True
##10. True
##
##Multiple Choice
##1. B
##2. D
##3. D
##4. C
##5. D
##6. A
##7. D
##8. D
##9. C
##10. B
##
##Discussion Questions
##1.
##(a)[2, 1, 4, 3, 'c', 'a', 'b']
##(b)[2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 'c', 'a', 'b', 'c', 'a', 'b']
##(c)1
##(d)[1, 4]
##(e)TypeError
##2.
##(a)[1, 4, 3]
##['c', 'a', 'b']
##(b)[1, 2, 3, 4]
##['c', 'a', 'b']
##(c)[2, 1, 4, 3, [2]]
##['c', 'a', 'b']
##(d)IndexError
##(e)[2, 1, 4, 3]
##['c', 'a', 'd', 'b']





from random import *
def shuffle(myList):
    n = len(myList)
    new_list = []
    for i in range(n):
        x = len(myList)
        amt = randrange(0,x)
        item = myList[amt]
        new_list.append(item)
        myList.pop(amt)
    return new_list
        
        

class Deck:
    def __init__(self):
        self.full_deck = []
        suits = ['d','c','h','s']
        ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        for i in range(4):
            for j in range(13):
                tupple = (suits[i],ranks[j])
                self.full_deck.append(tupple)
        
    def constructor(self):
        self.full_deck = []
        suits = ['d','c','h','s']
        ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        for i in range(4):
            for j in range(13):
                tupple = (suits[i],ranks[j])
                self.full_deck.append(tupple)
        return self.full_deck
    
    def shuffle(self):
        n = len(self.full_deck)
        self.shuffled_deck = []
        for i in range(n):
            x = len(self.full_deck)
            amt = randrange(0,x)
            item = self.full_deck[amt]
            self.shuffled_deck.append(item)
            self.full_deck.pop(amt)
        return self.shuffled_deck
    def dealCard(self):
        n = len(self.full_deck)
        rand = randrange(0,n)
        self.dealt_card = self.full_deck[rand]
        self.full_deck.pop(rand)
        return self.dealt_card
    def cardsLeft(self):
        num_cards = len(self.full_deck)
        return num_cards
    
        
def main():
    list = [1,3,10,'hello','goodbye',5,8]
    list_shuffled = shuffle(list)
    print(list_shuffled)
    
    x = Deck()
    dealt_cards_list = []
    num_cards_to_deal = eval(input("Enter the number of cards you want dealt: "))
    for i in range(num_cards_to_deal):
        card = x.dealCard()
        dealt_cards_list.append(card)
    print(dealt_cards_list)
    
main()
