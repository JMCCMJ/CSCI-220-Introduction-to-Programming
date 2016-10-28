#Jan-Mchael Carrington
#Authenticity: I certify this is my own code.


##True or False
##1. False
##2. False
##3. True
##4. True
##5. True
##6. True
##7. True
##8. True
##9. False
##10. False
##
##Multiple Choice
##1. B
##2. C
##3. D
##4. B
##5. C
##6. A
##7. B
##8. A
##9. A
##10. B
##
##Discussion
##1.                             main   --printReport(length,width,amtNeeded)
##                            /    |   \
##                 printIntro()    |    computeAmount(length,width)[sends information to amtNeeded in main]
##                    getDimensions()[sends length and width to main]
##2.
##randint(0,10)
##random() - 0.5
##randint(0,6)
##die_roll = randint(0,6) + randint(0,6)
##(random() * 20) - 10
##
##
##3.
##When encountering some form of new programming, spiral developing is an easy
##way to dive into it by using a prototype. One can easily start out with
##the prototype and building upon it. This makes it easier than top-down
##for new programming because one isn't overwhelmed with a bunch of functions
##that need completed.


from random import *


#Programming Exercise 7
def crapsSimulation():
    dice1 = randrange(1,7)
    dice2= randrange(1,7)
    added_dice = dice1 + dice2
    initial_roll = dice1 + dice2
    if added_dice == 2 or added_dice == 3 or added_dice ==12:
        return False
        
    elif added_dice == 7 or added_dice == 11:
        return True
    else:
        while True:
            dice1 = randrange(1,7)
            dice2 = randrange(1,7)
            added_dice = dice1 + dice2
            if added_dice == initial_roll:
                return True
            elif added_dice == 7:
                return False


def craps():
    player_wins = 0
    player_loses = 0
    num = eval(input("Enter the number of times to simulate Craps: "))
    for i in range(num):
        x = crapsSimulation()
        if x:
            player_wins = player_wins + 1
        else:
            player_loses = player_loses + 1
    prob = (player_wins / num) * 100
    print("The estimated probability of winning Craps is ", prob, "%.",sep = "")

#Programming Exercise 9
def end(points):
    if points >=17 and points <= 21:
        return points
    if points >= 22:
        return points


def blackJackSimulationCards(card_num):
    value = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    points = card_num
    while not end(points):
        dealer_card = value[randrange(13)]
        if dealer_card == 11:
            if points >=6 and points <= 10:
                points = points + 11
            else:
                points = points + 1
        else:
            points = points + dealer_card
    if points >=17 and points <=21:
        return 1
    if points > 21:
        return 0


def blackJackCards():
    length = eval(input("Enter the number of times to run the blackjack simulation: "))
    staysAce = 0
    bustsAce = 0
    for i in range(length):
        x = blackJackSimulationCards(1)
        if x == 1:
            staysAce = staysAce + 1
        if x == 0:
            bustsAce = bustsAce + 1
    ace_perc = (bustsAce / length) * 100
    print("For 1 busted ","{0:0.2f}".format(ace_perc), "% of the time.",sep = "")

    bustsTwo = 0
    for i in range(length):
        x = blackJackSimulationCards(2)
        if x == 0:
            bustsTwo = bustsTwo + 1
    two_perc = (bustsTwo / length) * 100
    print("For 2 busted ","{0:0.2f}".format(two_perc), "% of the time.",sep = "")

    bustsThree = 0
    for i in range(length):
        x = blackJackSimulationCards(3)
        if x == 0:
            bustsThree = bustsThree + 1
    three_perc = (bustsThree / length) * 100
    print("For 3 busted ","{0:0.2f}".format(three_perc), "% of the time.",sep = "")

    bustsFour = 0
    for i in range(length):
        x = blackJackSimulationCards(4)
        if x == 0:
            bustsFour = bustsFour + 1
    four_perc = (bustsFour / length) * 100
    print("For 4 busted ","{0:0.2f}".format(four_perc), "% of the time.",sep = "")

    bustsFive = 0
    for i in range(length):
        x = blackJackSimulationCards(5)
        if x == 0:
            bustsFive = bustsFive + 1
    five_perc = (bustsFive / length) * 100
    print("For 5 busted ","{0:0.2f}".format(five_perc), "% of the time.",sep = "")


    bustsSix = 0
    for i in range(length):
        x = blackJackSimulationCards(6)
        if x == 0:
            bustsSix = bustsSix + 1
    six_perc = (bustsSix / length) * 100
    print("For 6 busted ","{0:0.2f}".format(six_perc), "% of the time.",sep = "")


    bustsSeven = 0
    for i in range(length):
        x = blackJackSimulationCards(7)
        if x == 0:
            bustsSeven = bustsSeven + 1
    seven_perc = (bustsSeven / length) * 100
    print("For 7 busted ","{0:0.2f}".format(seven_perc), "% of the time.",sep = "")


    bustsEight = 0
    for i in range(length):
        x = blackJackSimulationCards(8)
        if x == 0:
            bustsEight = bustsEight + 1
    eight_perc = (bustsEight / length) * 100
    print("For 8 busted ","{0:0.2f}".format(eight_perc), "% of the time.",sep = "")


    bustsNine = 0
    for i in range(length):
        x = blackJackSimulationCards(9)
        if x == 0:
            bustsNine = bustsNine + 1
    nine_perc = (bustsNine / length) * 100
    print("For 9 busted ","{0:0.2f}".format(nine_perc), "% of the time.",sep = "")


    bustsTen = 0
    for i in range(length):
        x = blackJackSimulationCards(10)
        if x == 0:
            bustsTen = bustsTen + 1
    ten_perc = (bustsTen / length) * 100
    print("For 10 busted ","{0:0.2f}".format(ten_perc), "% of the time.",sep = "")



#Programming Exercise 11

def dieSimulation():
    die1 = randrange(1,7)
    die2 = randrange(1,7)
    die3 = randrange(1,7)
    die4 = randrange(1,7)
    die5 = randrange(1,7)

    if die1 == die2 and die1 == die3 and die1 == die4 and die1 == die5:
        return True
    else:
        return False

def diceRoll():
    wins = 0
    length = eval(input("Enter the number of times to simulate rolling 5 of the same die: "))
    for i in range(length):
        x = dieSimulation()
        if x:
            wins = wins + 1
    est = (wins / length) * 100
    #print(wins)
    print("The estimated probability of rolling 5 of the same die is ",est,"%.",sep="")






craps()
diceRoll()
blackJackCards()



    
