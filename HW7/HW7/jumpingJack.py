""" Samples provided by Randall Alexander

Name: Jan-Michael Carrington
Authenticity: I certify that this program is entirely my own work.

Work all the T/F, Multiple Choice and Discussion for Chapter 7
T/F

True/False
1. True
2. False
3. True
4. False 
5. True
6. True
7. True
8. False
9. True
10. False

Multiple Choice
1. C
2. C
3. B
4. C
5. B
6. C
7. A
8. C
9. A
10. C

Discussion
1.
(a) A simple decision makes use of a single if statement where if
one particular thing happens, the if statement runs its course.
(b) A two-way decision involves an if and an else statement. If one
particular thing happens, the if statements runs. Otherwise, the else
statement runs.
(c) A multiway decision makes use of an if, elif or muliple elifs, and
an else statement. This statement can handle many different decisions.
2.
(a)
Trees
Larch
Done
(b)
Trees
Chestnut
Done
(c)
Spam Please!
Done
(d)
Cheese Shoppe
Cheddar
Done
(e)
It's a late parrot!
Done
(f)
Cheese Shoppe
Cheddar
Done
3. Using exception handling with try/except is different from ordinary
decision structures by letting a program crash gracefully
letting an error not crash the entire program, but rather
return useful information as to what happened and allowing the program to
continue. They are similar by trying to run a piece of code like
how an if statement would try to run a piece of
code and will if the correct boolean requirements are supplied.


"""
from graphics import *
from time import sleep



    
    

def main():
    '''Create a graphics window and 3 buttons, Start, Stop and End.
    You must change the buttons to the correct labels'''
    
    win = GraphWin("Jumping Jack", 400, 400)
    jump = Button(win,Point(75,325), 100, 100,'JUMP','light blue')
    rest = Button(win,Point(200,325),100, 100, 'REST', 'light green')
    vanish = Button(win,Point(325,325),100, 100, 'VANISH', 'red')
    #sun = Circle(Point(325,75),50)
    #sun.setFill('yellow')
    #sun.draw(win)
    head = Circle(Point(200,50),25)
    head.draw(win)
    body = Line(Point(200,75),Point(200,150))
    body.draw(win)

    #creating the first position
    right_arm1 = Line(Point(200,100),Point(250,150))
    left_arm1 = Line(Point(200,100),Point(150,150))
    right_leg1 = Line(Point(200,150),Point(225,225))
    left_leg1 = Line(Point(200,150),Point(175,225))
    right_arm1.draw(win)
    left_arm1.draw(win)
    right_leg1.draw(win)
    left_leg1.draw(win)


    # Loop until the vanish rectangle is clicked.    
    while True:

        # sample the mouse and save the clicked point
        cPt = win.checkMouse()

        #jump button code
        #i can use multiple ifs
        if jump.clicked(cPt):
            while True:
                
                
                jump_once(win, right_arm1, left_arm1, right_leg1, left_leg1)
                
                
                cPt = win.checkMouse()
                    
                # if rest clicked, exit the loop             
                if rest.clicked(cPt):
                    right_arm1 = Line(Point(200,100),Point(250,150))
                    left_arm1 = Line(Point(200,100),Point(150,150))
                    right_leg1 = Line(Point(200,150),Point(225,225))
                    left_leg1 = Line(Point(200,150),Point(175,225))
                    right_arm1.draw(win)
                    left_arm1.draw(win)
                    right_leg1.draw(win)
                    left_leg1.draw(win)
                    break

                # if vanish clicked, exit the loop
                if vanish.clicked(cPt):
                    break
        # if vanish clicked, exit the program
        if vanish.clicked(cPt):
            break
        
    # close the window
    win.close()

def jump_once(win, right_arm1, left_arm1, right_leg1, left_leg1):
    '''This function handles the movement, the drawing and undrawing of the
    jumping. You may add parameters and you can return something if
    need it. This function must produce one movement (or one
    complete cycle) and end so a button click can be detected.
    '''

    #code for 1 loop cycle
    
    right_arm1.undraw()
    left_arm1.undraw()
    right_leg1.undraw()
    left_leg1.undraw()

    
    
    right_arm2 = Line(Point(200,100),Point(275,100))
    left_arm2 = Line(Point(200,100),Point(125,100))
    right_leg2 = Line(Point(200,150),Point(250,200))
    left_leg2 = Line(Point(200,150),Point(150,200))
    right_arm2.draw(win)
    left_arm2.draw(win)
    right_leg2.draw(win)
    left_leg2.draw(win)

    sleep(0.7)
    
    right_arm2.undraw()
    left_arm2.undraw()
    right_leg2.undraw()
    left_leg2.undraw()

    

    right_arm3 = Line(Point(200,100),Point(275,50))
    left_arm3 = Line(Point(200,100),Point(125,50))
    right_leg3 = Line(Point(200,150),Point(225,225))
    left_leg3 = Line(Point(200,150),Point(175,225))
    right_arm3.draw(win)
    left_arm3.draw(win)
    right_leg3.draw(win)
    left_leg3.draw(win)

    sleep(0.7)
    
    right_arm3.undraw()
    left_arm3.undraw()
    right_leg3.undraw()
    left_leg3.undraw()

    

    right_arm4 = Line(Point(200,100),Point(275,100))
    left_arm4 = Line(Point(200,100),Point(125,100))
    right_leg4 = Line(Point(200,150),Point(250,200))
    left_leg4 = Line(Point(200,150),Point(150,200))
    right_arm4.draw(win)
    left_arm4.draw(win)
    right_leg4.draw(win)
    left_leg4.draw(win)

    sleep(0.7)

    right_arm4.undraw()
    left_arm4.undraw()
    right_leg4.undraw()
    left_leg4.undraw()

    right_arm1 = Line(Point(200,100),Point(250,150))
    left_arm1 = Line(Point(200,100),Point(150,150))
    right_leg1 = Line(Point(200,150),Point(225,225))
    left_leg1 = Line(Point(200,150),Point(175,225))

    right_arm1.draw(win)
    left_arm1.draw(win)
    right_leg1.draw(win)
    left_leg1.draw(win)

    sleep(0.7)

    right_arm1.undraw()
    left_arm1.undraw()
    right_leg1.undraw()
    left_leg1.undraw()

    

    

    
    
    
class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label,color):
        """
        Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit')
        """ 
        self.p1 = Point(center.x - width/2, center.y - height/2)
        self.p2 = Point(center.x + width/2, center.y + height/2)
        self.rect = Rectangle(self.p1,self.p2)
        self.color = color
        self.rect.setFill(color)
        self.rect.setWidth(2)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        
    def setLabel(self,label):
        self.label.setText(label)

    def setFill(self,color):
        self.rect.setFill(color)
        self.color = color
        
    def undraw(self):
        self.rect.undraw()
        self.label.undraw()

    def move(self,dx,dy):
        self.rect.move(dx,dy)
        self.label.move(dx,dy)

    def clicked(self, p):
        "Returns True if p is not None and p is inside the button"
        if p == None: return False
        return (self.p1.x <= p.x <= self.p2.x and
                self.p1.y <= p.y <= self.p2.y)
    
main()   
    
