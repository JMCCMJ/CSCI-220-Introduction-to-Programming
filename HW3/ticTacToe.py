#Tic Tac Toe
#Jan-Michael Carrington
#This program will create a tic-tac-toe game that can be played
#by two players. I must create a program that makes a 3x3 grid
#and when a mouse click happens in a square of the tic-tac-toe game
#a X or O will appear at the respective turns.


#importing graphics
from graphics import *


#defining
def main():

    #creating the window
    win = GraphWin("Tic Tac Toe", 300, 300)
    win.setCoords(0,0,3,3)

    #creating the board
    line1 = Line(Point(1,0),Point(1,3))
    line1.draw(win)

    line2 = Line(Point(2,0),Point(2,3))
    line2.draw(win)

    line3 = Line(Point(0,1),Point(3,1))
    line3.draw(win)

    line4 = Line(Point(0,2),Point(3,2))
    line4.draw(win)

    #setting variables
    even = 1
    odd = 2

    #creating the X's and O's
    gameX = Polygon(Point(0,0),Point(1,1),Point(0.5,0.5),Point(0,1),Point(1,0),Point(0.5,0.5))
    gameO = Circle(Point(0.5,0.5),0.5)

    

    
    
    #algorithms
    for i in range(1, 10):
        variable = even
        
        user_pt = win.getMouse()
        userX = user_pt.getX()
        userY = user_pt.getY()

        even,odd = odd,even

        if userX < 1:
            if userY < 1:
                if variable == 1:
                    cloneX = gameX.clone()
                    cloneX.draw(win)
                else:
                    cloneO = gameO.clone()
                    cloneO.draw(win)
                    
        if userX > 2:
            if userY > 2:
                if variable == 1:
                    cloneX = gameX.clone()
                    cloneX.draw(win)
                    cloneX.move(2,2)
                else:
                    cloneO = gameO.clone()
                    cloneO.draw(win)
                    cloneO.move(2,2)
                    
        if userX < 1:
            if userY > 1:
                if userY < 2:
                    if variable == 1:
                        cloneX = gameX.clone()
                        cloneX.draw(win)
                        cloneX.move(0,1)
                    else:
                        cloneO = gameO.clone()
                        cloneO.draw(win)
                        cloneO.move(0,1)

        if userX < 1:
             if userY > 2:
                if variable == 1:
                    cloneX = gameX.clone()
                    cloneX.draw(win)
                    cloneX.move(0,2)
                else:
                    cloneO = gameO.clone()
                    cloneO.draw(win)
                    cloneO.move(0,2)

        if userX > 1:
            if userX < 2:
                if userY < 1:
                    if variable == 1:
                        cloneX = gameX.clone()
                        cloneX.draw(win)
                        cloneX.move(1,0)
                    else:
                        cloneO = gameO.clone()
                        cloneO.draw(win)
                        cloneO.move(1,0)

        if userX > 1:
            if userX < 2:
                if userY > 1:
                    if userY < 2:
                        if variable == 1:
                            cloneX = gameX.clone()
                            cloneX.draw(win)
                            cloneX.move(1,1)
                        else:
                            cloneO = gameO.clone()
                            cloneO.draw(win)
                            cloneO.move(1,1)

        if userX > 1:
            if userX < 2:
                if userY > 2:
                    if userY < 3:
                        if variable == 1:
                            cloneX = gameX.clone()
                            cloneX.draw(win)
                            cloneX.move(1,2)
                        else:
                            cloneO = gameO.clone()
                            cloneO.draw(win)
                            cloneO.move(1,2)

        if userX > 2:
            if userX < 3:
                if userY < 1:
                    if variable == 1:
                        cloneX = gameX.clone()
                        cloneX.draw(win)
                        cloneX.move(2,0)
                    else:
                        cloneO = gameO.clone()
                        cloneO.draw(win)
                        cloneO.move(2,0)

        if userX > 2:
            if userX < 3:
                if userY > 1:
                    if userY < 2:
                        if variable == 1:
                            cloneX = gameX.clone()
                            cloneX.draw(win)
                            cloneX.move(2,1)
                        else:
                            cloneO = gameO.clone()
                            cloneO.draw(win)
                            cloneO.move(2,1)

    #ending and closing
    endText = Text(Point(1.5,1.5),"Click anywhere to close the game.")
    endText.draw(win)
    win.getMouse()

    win.close()




main()
