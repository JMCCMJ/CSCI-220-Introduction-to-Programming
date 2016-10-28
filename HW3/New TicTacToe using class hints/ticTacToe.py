#Tic Tac Toe
#Jan-Michael Carrington
#This program will create a tic-tac-toe game that can be played
#by two players. I must create a program that makes a 3x3 grid
#and when a mouse click happens in a square of the tic-tac-toe game
#a X or O will appear at the respective turns.


from graphics import *


def find_nearest_center(point):
    x = point.getX()
    y = point.getY()
    new_x = x // 100 * 100 + 50
    new_y = y // 100 * 100 + 50
    #return command gives back a new point to the function
    #calling find_nearest_center
    return Point(new_x, new_y)
    

def main():
    #creating the window
    win = GraphWin("Tic Tac Toe", 300, 300)

    #board
    line1 = Line(Point(0,100),Point(300,100))
    line2 = Line(Point(0,200),Point(300,200))
    line3 = Line(Point(100,0),Point(100,300))
    line4 = Line(Point(200,0),Point(200,300))
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4.draw(win)

    #variables
    even = 2
    odd = 1

  
    
    #algorithms
    for i in range(9):
        pt = win.getMouse()
        new_pt = find_nearest_center(pt)
        if even == 2:
            user_x1_linept = new_pt.getX() - 50
            user_y1_linept = new_pt.getY() - 50
            user_x2_linept = new_pt.getX() + 50
            user_y2_linept = new_pt.getY() + 50
            xLine1 = Line(Point(user_x1_linept,user_y1_linept),Point(user_x2_linept,user_y2_linept))
            xLine1.draw(win)

            user_x3_linept = new_pt.getX() + 50
            user_y3_linept = new_pt.getY() - 50
            user_x4_linept = new_pt.getX() - 50
            user_y4_linept = new_pt.getY() + 50
            xLine2 = Line(Point(user_x3_linept,user_y3_linept),Point(user_x4_linept,user_y4_linept))
            xLine2.draw(win)

        if even == 1:
            user_center_pt = new_pt
            radius = 50
            user_o = Circle(user_center_pt,radius)
            user_o.draw(win)

        even,odd = odd,even

    #ending and closing
    txt1 = Text(Point(150,150),"Click anywhere to close.")
    txt1.draw(win)
    win.getMouse()

    win.close()
    
        
        














main()
