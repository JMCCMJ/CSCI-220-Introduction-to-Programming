


from random import randint

def goodInput():
    while True:  
        x = eval(input("Enter a number between 1 and 10: "))
        if 1 <= x <= 10:
            return x
        else:
            print("The value you entered was not between 1 and 10. Try again.")

def hiLoGame():
    rand_num = randint(1,100)
    print("Try to guess a number between 1 and 100.")
    for i in range(1,9):
        if i == 8:
            print(("Sorry you lose. The number was {0}.".format(rand_num)))
            break
        user_num = eval(input("Enter your guess: "))
        if user_num == rand_num:
            print("Correct!")
            print("You won in {0} guesses.".format(i))
            break
        elif user_num < rand_num:
            print("Too low!")
        elif user_num > rand_num:
            print("Too high!")


def is_day_valid(day,month):
    day_int = int(day)
    month_int = int(month)
    is_it_leap_year = leap_year(month)
    #print(is_it_leap_year)
    if month_int == 2:
        if is_it_leap_year == 1:
            if 1 <= day_int <= 29:
                return True
            else:
                return False
        elif 1 <= day_int <= 28:
            return True
        
        else:
            return False
    elif month_int == 1:
        if 1 <= day_int <= 31:
            return True
        else:
            return False
    elif month_int == 3:
        if 1 <= day_int <= 31:
            return True
        else:
            return False
    elif month_int == 4:
        if 1 <= day_int <= 30:
            return True
        else:
            return False
    elif month_int == 5:
        if 1 <= day_int <= 31:
            return True
        else:
            return False
    elif month_int == 6:
        if 1 <= day_int <= 30:
            return True
        else:
            return False
    elif month_int == 7:
        if 1 <= day_int <= 31:
            return True
        else:
            return False
    elif month_int == 8:
        if 1 <= day_int <= 31:
            return True
        else:
            return False
    elif month_int == 9:
        if 1 <= day_int <= 30:
            return True
        else:
            return False
    elif month_int == 10:
        if 1 <= day_int <= 31:
            return True
        else:
            return False
    elif month_int == 11:
        if 1 <= day_int <= 30:
            return True
        else:
            return False
    elif month_int == 12:
        if 1 <= day_int <= 31:
            return True
        else:
            return False
    
    else:
        return False
def month_days(month):
    month_int = int(month)
    x = 30
    y = 31
    z = 28
    a = 29
    is_it_leap_year = leap_year(month)
    if month_int == 1:
        return y
    if month_int == 2:
        if is_it_leap_year == 1:
            return a
        else:
            return z
    if month_int == 3:
        return y
    if month_int == 4:
        return x
    if month_int == 5:
        return y
    if month_int == 6:
        return x
    if month_int == 7:
        return y
    if month_int == 8:
        return y
    if month_int == 9:
        return x
    if month_int == 10:
        return y
    if month_int == 11:
        return x
    if month_int == 12:
        return y
        

def is_month_valid(month):
    month_int = int(month)
    if 1 <= month_int <= 12:
        return True
    else:
        return False
def is_year_valid(year):
    year_int = int(year)
    if 1<= year_int <= 2500:
        return True
    else:
        return False
def leap_year(year):
    year_int = int(year)
    y1 = 400
    y2 = 100
    y3 = 4
    x = 1
    y = 0
    if (year_int%y1 == 0):
        return x
    elif ((year_int%y3 == 0) and (year_int%y2 != 0)):
        return x
    else:
        return y
        
def verify_date(dates_file):
    infile = open(dates_file,'r')
    file_string = infile.read()
    infile.close()
    file_string_replace = file_string.replace("/"," ").replace("."," ").replace("-"," ")
    file_string_split = file_string_replace.split()
    file_splitted = []
    len_file = len(file_string_split)
    for x in range(0, len_file,3):
        file_splitted.append(file_string_split[x:x+3])

    dates = ''
    for i in file_splitted:
        
        day_valid = is_day_valid(i[1],i[0])
       
        month_valid = is_month_valid(i[0])
        year_valid = is_year_valid(i[2])
   
        
        
        if day_valid == True:
            if month_valid == True:
                if year_valid == True:
                    dates = dates + str(int(i[0]))
        else:
            dates = dates + "-"

    print(dates)
                
    
    

def main():

  
    verify_date("dates_to_be_verified.txt")
    
    



main()
    
