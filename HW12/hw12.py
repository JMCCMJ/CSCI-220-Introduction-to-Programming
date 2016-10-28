#hw12.py
#Jan-Michael Carrington
#Purpose: To construct a class for a deck of cards.
#Authenticity: I certify this code is my own work.


from graphics import *
from random import *
from time import sleep

class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label, color):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit','yellow') """ 
        self.xmax, self.xmin = center.getX()+width/2.0, center.getX()-width/2.0
        self.ymax, self.ymin = center.getY()+height/2.0, center.getY()-height/2.0
        p1,p2 = Point(self.xmin, self.ymin), Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(color)
        self.label = Text(center, label)
        self.win = win
        self.active = False

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def activate(self):
        "Sets this button to active and draws the button."
        if self.active == False:
            self.active = True
            self.rect.draw(self.win)
            self.label.draw(self.win)

    def deactivate(self):
        "Sets this button to 'inactive' and undraws the button."
        if self.active == True:
            self.active = False
            self.rect.undraw()
            self.label.undraw()
            
class Words:
    '''reads a file of words and creates a list of words'''
    def __init__(self,filename):
        infile = open(filename,'r')
        self.file_string = infile.read()
        infile.close()
        self.file_string_split = self.file_string.split()
        #print(self.file_string_split)
    def get_word(self):
        '''returns a random word from the list'''
        self.amt_words = len(self.file_string_split)
        
        rand_num = randrange(0,self.amt_words)
        self.rand_word = self.file_string_split[rand_num]
        self.file_string_split.pop(rand_num)
        return self.rand_word
    def length_of_file(self):
        
        return self.amt_words
        #print(self.rand_word)
        #print(self.file_string_split)
        
class Guess:
    def __init__ (self,word,win,head,body,left_leg,right_leg,left_arm,right_arm,right_eye_1,right_eye_2,eye1,eye2):
        self.win = win
        self.let_guessed = []
        self.word = word
        self.head=head
        self.body = body
        self.left_leg = left_leg
        self.right_leg = right_leg
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.right_eye_1 = right_eye_1
        self.right_eye_2 = right_eye_2
        self.eye1 = eye1
        self.eye2 = eye2
        #print(self.word)
        list_letters = {}
        length = (len(self.word))
        for letter in self.word:
            list_letters[letter] = list_letters.get(letter,0)+1
        #print(list_letters)
        #x = list_letters.get('c')
        #print(x)
        self.word_letters = []
        for i in range(length):
            self.word_letters.append(self.word[i])
        #print(self.word_letters)
        self.word_empty = []
        for i in range(length):
            under = '_'
            self.word_empty.append(under)
        #print(self.word_empty)
        self.word_third = []
        for i in range(length):
            #self.word_third.append(self.word[i])
            under = '_'
            self.word_third.append(under)
        #print(self.word_third)
        #print(self.word_third)

        #self.letters_guessed = ''
        self.num_guesses = 7
    def missed (self):
        '''returns the word string that could not be guessed'''


        
        
    def guess_letter (self,letter):
        '''uncovers letters that match the guess, counts the bad guesses
        and keeps track of the letters guessed. It returns a number, 0,
        if the letter has already been guessed, 1 if the letter is NOT
        in the word and 2 if the letter IS in the word
        '''
        try:
            
            self.guessed_letter = self.word_letters.index(letter)
            self.word_empty[self.guessed_letter] = self.word_letters[self.guessed_letter]
            #self.word_letters.remove(letter)
            self.word_letters[self.guessed_letter] = self.word_third[self.guessed_letter]
            #print(self.word_empty)
            #print(self.guessed_letter)
            self.finished = ""
            
            for letter in self.word_empty:
                self.finished = self.finished + letter
            
            return self.guessed_letter
        except ValueError:
            #self.num_guesses = self.num_guesses + 1
            #print(self.num_guesses)
            return None
        
    def gameover (self,letter):
        '''returns Boolean, T if word is guessed or the number of guesses
        has exceeded the limit and F otherwise'''
        
        try:
            guess = self.word_letters.index(letter)
            return 7
            
        except:
            self.num_guesses = self.num_guesses - 1
            #print('Wrong letter.')
            #print('You have', self.num_guesses, 'guesses left.')
            self.noose_num = self.num_guesses
            noose = Noose(self.win,self.noose_num,self.head,self.body,self.left_leg,self.right_leg,self.left_arm,self.right_arm,self.right_eye_1,self.right_eye_2,self.eye1,self.eye2)
            noose.wrong()
            
            
            return self.num_guesses
    def gameover_win(self):
        try:
            if self.finished == self.word:
                return 1
        except AttributeError:
            return 0
        
        
        
        
        
    def num_of_guesses(self):
        '''returns a STRING with the number of remaining guesses'''
        
        
    def letters_guessed (self,let):
        '''returns a string, in alphabetical order, of all the letters
        that have been guessed'''
        try:
            z = self.let_guessed.index(let)
            if z == -7:
                #print("You already guessed that.")
                self.num_guesses = self.num_guesses + 1
        except ValueError:
            
            self.let_guessed.append(let)
            self.let_guessed.sort()
            
            
            
    def letters_guessed_print(self):
        #print(self.let_guessed)
        #print()
        return self.let_guessed
    
    
        
    def   __str__ (self):
        '''returns a string with the letters in the word and _ for each
        unguessed letter separated by spaces'''
        self.string = ""
        for letter in self.word_empty:
            self.string = self.string + letter + " "
        return self.string
            
        
class Noose:
    def __init__(self,win,num,head,body,left_leg,right_leg,left_arm,right_arm,right_eye_1,right_eye_2,eye1,eye2):
        '''creates a Noose object with 7 sections that can be drawn one at a
        time in the win canvas'''
        
        self.win = win
        self.num = num
        self.head=head
        self.body = body
        self.left_leg = left_leg
        self.right_leg = right_leg
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.right_eye_1 = right_eye_1
        self.right_eye_2 = right_eye_2
        self.eye1 = eye1
        self.eye2 = eye2
        
        
    def wrong(self):
        '''draws another of the 7 sections to the noose platform and/or figure'''
        if self.num == 6:
            self.head.draw(self.win)
        if self.num == 5:
            self.body.draw(self.win)
        if self.num == 4:
            self.left_leg.draw(self.win)
        if self.num == 3:
            self.right_leg.draw(self.win)
        if self.num == 2:
            self.left_arm.draw(self.win)
        if self.num == 1:
            self.right_arm.draw(self.win)
        if self.num == 0:
            self.right_eye_1.draw(self.win)
            self.right_eye_2.draw(self.win)
            self.eye1.draw(self.win)
            self.eye2.draw(self.win)
def play_one_game():
    win = GraphWin('Hangman', 600, 600)
    floor = Line(Point(20,400),Point(200,400))
    floor.draw(win)
    pole = Line(Point(110,400),Point(110,100))
    pole.draw(win)
    upper_pole = Line(Point(110,100),Point(250,100))
    upper_pole.draw(win)
    small_pole = Line(Point(250,100),Point(250,150))
    small_pole.draw(win)
    guess_button = Button(win,Point(550,100),75,75,'Enter','yellow')
    guess_button.activate()
    user_guess = Entry(Point(500,100),1)
    user_guess.draw(win)
    start_button = Button(win,Point(50,50),75,75,'Start','green')
    start_button.activate()
    words_view = Text(Point(300,500), '')
    words_view.draw(win)
    words_used_view = Text(Point(500,300),'')
    letters_you_used = Text(Point(500,285),'Letters you have used:')
    
    guesses_left = Text(Point(485,350),'')
    guesses_left.draw(win)
    you_win_text = Text(Point(300,550),'You Win!')
    you_lose_text = Text(Point(300,550),'You Lose...')
    play_again_text = Text(Point(125,450),'Do you want to play again?')
    yes_button = Button(win,Point(75,500),75,75,'Yes','cyan')
    no_button = Button(win,Point(175,500),75,75,'No','red')
    click_start = Text(Point(125,500),'Hit start when this \n text dissapears to begin.')
    
    head = Circle(Point(250,175),25)
    body = Line(Point(250,200),Point(250,275))
    left_leg = Line(Point(250,275),Point(200,350))
    right_leg = Line(Point(250,275),Point(300,350))
    left_arm = Line(Point(250,225),Point(200,275))
    right_arm = Line(Point(250,225),Point(300,275))
    right_eye_1 = Line(Point(235,180),Point(245,165))
    right_eye_2 = Line(Point(235,165),Point(245,180))
    right_eye_1.setFill('red')
    right_eye_2.setFill('red')
    eye1 = right_eye_1.clone()
    eye2 = right_eye_2.clone()
    eye1.move(20,0)
    eye2.move(20,0)

    
    words = Words('wordlist.txt')
    rand_word = words.get_word()
    amt_of_plays = words.length_of_file()
    #print(rand_word)
    
    while True:
        mouse = win.getMouse()
        user_guess.setText('')
        if start_button.clicked(mouse):
            letters_you_used.draw(win)
            words_used_view.draw(win)
            
            for i in range(amt_of_plays):
                x = Guess(rand_word,win,head,body,left_leg,right_leg,left_arm,right_arm,right_eye_1,right_eye_2,eye1,eye2)
                x.letters_guessed_print()
                #print(x)
                words_view.setText(x)
                while True:
                    
                    point = win.getMouse()
                    if guess_button.clicked(point):
                        user_letter = user_guess.getText()
                        letters = x.letters_guessed(user_letter)
                        guess_wrong_count = x.gameover(user_letter)
                        string_guesses_left = 'You have ' + str(guess_wrong_count) + ' wrong guesses left.'
       
                        if guess_wrong_count == 0:
                            you_lose_text.draw(win)
                            you_win_text.move(1000,1000)
                            you_win_text.draw(win)
                            sleep(3)
                            you_win_text.undraw()
                            you_win_text.move(-1000,-1000)
                            you_lose_text.undraw()
                            play_again_text.draw(win)
                            yes_button.activate()
                            no_button.activate()
                            pt = win.getMouse()
                            
                            break;
                        while True:
                            a = x.guess_letter(user_letter)
                            
                            
                            if a == None:
                                break;
                    guesses_left.setText(string_guesses_left)
                    words_view.setText(x)    
                    #print(x)
                    letters_used = x.letters_guessed_print()
                    words_used_view.setText(letters_used)
                    guess_right = x.gameover_win()
                    if guess_right == 1:
                        you_win_text.draw(win)
                        you_lose_text.move(1000,1000)
                        sleep(3)
                        you_win_text.undraw()
                        you_lose_text.undraw()
                        you_lose_text.move(-1000,-1000)
                        play_again_text.draw(win)
                        yes_button.activate()
                        no_button.activate()
                        pt = win.getMouse()
                        
                        break;
                rand_word = words.get_word()
                break;
            if no_button.clicked(pt):
                win.close()
                break;
            if yes_button.clicked(pt):
                head.undraw()
                body.undraw()
                left_leg.undraw()
                right_leg.undraw()
                right_arm.undraw()
                left_arm.undraw()
                right_eye_1.undraw()
                right_eye_2.undraw()
                eye1.undraw()
                eye2.undraw()
                yes_button.deactivate()
                no_button.deactivate()
                click_start.draw(win)
                guesses_left.undraw()
                letters_you_used.undraw()
                words_used_view.undraw()
                play_again_text.undraw()
                sleep(4)
                click_start.undraw()
                
                
                

play_one_game()
