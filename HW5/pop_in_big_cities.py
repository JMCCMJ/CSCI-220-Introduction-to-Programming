###Jan-Michael Carrington
###pop_in_big_cities.py
##
##
##pg 160 multiple choice
##1. D
##2. C
##3. A
##4. C
##5. C
##6. C
##7. D
##8. C
##9. C
##10. A
##
##discussion
##1.
##(a)"The Knights who say, ni!"
##(b)"spamspamspamni!ni!"
##(c)"p"
##(d)"pa"
##(e)"ani"
##(f)"spam!"
##(g)"SPAM"
##(h)"NI! NI! NI!"
##2.
##(a)s2[0:2].upper()
##(b)s2+s1+s2
##(c)s1.capitalize()+" "+s2.capitalize()+"  "+s1.capitalize()+" "+s2.capitalize()+"  "+s1.capitalize()+" "+s2.capitalize()
##(d)s1
##(e)s1[0:2],s1[3]
##(f)s1[0:2]+s1[3]
##3.
##(a)
##a
##a
##r
##d
##v
##a
##r
##k
##(b)
##Now
##is
##the
##winter
##of
##our
##discontent...
##(c)M ss ss pp
##(d)scrt
##(e)tfdsfu
##4.
##(a)"Looks like spam and eggs for breakfast"
##(b)"There is 1 spam 4 you"
##(c)"Hello Susan"
##(d)"2.302.30"
##(e)The operation is not legal becuase the index of the tuple is out of its range.
##(f)"Time left 01:37.37"
##(g)The operation is not legal becuase the tuple is out of range.
##





#This program will import a text file, display the states,
#and display the percentage of the population that
#are in cities with over 100,000 people.


#***NOTE: When the program is run it outputs everything fine
#but gives an error at the end of it of which I have no idea why.


#defining 
def main():
    #opening and reading the file
    infile = open('states_with_cities_over_100K.txt','r')
    file_string = infile.read()
    infile.close()
    
    #getting rid of the commas in the numbers
    file_string = file_string.replace(',','')
    my_file = file_string
    
    #splitting the file by lines
    lines = my_file.split('\n')
    even = 2
    odd = 1

    #begin calculations for each line
    for line in lines:
        words = line.split('\t')
        total = 0
        for i in range(3, len(words)+1,2):
    
            x = eval(words[i])
            total = total + x
                

            #even,odd = odd,even

        #getting averages
        average = (total / eval(words[1])) * 100
        average = round(average,2)

        #printing results
        print(words[0], '\t',average, '%',sep='')
        
                
            
            
            
            
        

        
        
        

main()
    
