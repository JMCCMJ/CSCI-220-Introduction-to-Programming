""" Samples provided by Randall Alexander

Name:
Authenticity:

Work all the T/F, Multiple Choice and Discussion for Chapter 7
T/F

Multiple Choice

Discussion

"""
from graphics import *
from time import sleep


def main():
    '''Create a graphics window and 3 buttons, Start, Stop and End.
    You must change the buttons to the correct labels'''
    
    win = GraphWin("Jumping Jack", 400, 400)
    jump = Button(win,Point(75,100), 100, 100,'JUMP','light blue')
    rest = Button(win,Point(200,200),100, 100, 'REST', 'light green')
    vanish = Button(win,Point(325,300),100, 100, 'VANISH', 'red')
    sun = Circle(Point(325,75),50)
    sun.setFill('yellow')
    sun.draw(win)

    # Loop until the vanish rectangle is clicked.    
    while True:

        # sample the mouse and save the clicked point
        cPt = win.checkMouse()

        # was jump clicked, flash the sun on and off 
        if jump.clicked(cPt):
            while True:
                jump_once(win,sun)
                
                cPt = win.checkMouse()
                    
                # if rest clicked, exit the loop             
                if rest.clicked(cPt):
                    break

                # if vanish clicked, exit the loop
                if vanish.clicked(cPt):
                    break
        # if vanish clicked, exit the program
        if vanish.clicked(cPt):
            break
        
    # close the window
    win.close()

def jump_once(win, sun_object):
    '''This function handles the movement, the drawing and undrawing of the
    jumping. You may add parameters and you can return something if
    need it. This function must produce one movement (or one
    complete cycle) and end so a button click can be detected.
    '''
    sun_object.undraw()
    sleep (0.3)
    sun_object.draw(win)
    sleep (0.3)
    
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
    
