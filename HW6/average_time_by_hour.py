#Jan-Michael Carrington

# average_time_by_hour.py

# answers to T/F, Multiple Choice and Discussion on p194-196 (30% of hw grade)
##True/False pg 194
##1. False
##2. False
##3. True
##4. True
##5. False
##6. False
##7. False
##8. True
##9. True
##10. True
##
##Multiple Choice
##1. B
##2. A
##3. A
##4. A
##5. D
##6. A
##7. D
##8. C
##9. D
##10. A
##
##Discussion
##1. Defining functions in a program allow the program to appear more organized and
##easier to read by other programmers.
##2. Yes, because when a program hits a function, it pauses the current work it is doing and
##completes the called function, before returning back to it's original task.
##3.
##(a) Parameters are special variables in a function that are initialized at the time of call
##with information passed from the caller.
##(b) An actual parameter is a value that is passed to a function when it is called. Formal parameters
##are only accessible within the body of the function.
##(c) Parameters can be used like variables within a function. But are different by
##being independent to the caller.
##4.
##(a) A program provides input by passing information to the called function such as: example(info1,info2).
##(b) A function provides output by using a return statement to send information
##back to the program.
##5.
##(a) The function takes the parameter x that the caller sent, and multiplies it three times
##and then assigns that to answer. The function then returns answer to the caller.
##(b) A program could assign the variable exponent to cube(y). Then the function cube(x) multiples
##the value three times and returns the answer in the variable answer to variable exponent in the program. The program
##could then print(exponent).
##(c) This is due to the answer in the program being indepentent of the one in the function.
##So the one in the function has no effect on what is in the program.




# Reads a data file where every line is in the form:
# m/d/yyyy h:mm,response_time ,throw_away
# note: d can be d or dd (i.e. 9 or 13)
# note: h can be h or hh (i.e. 6 or 12)
# note: response_time is in milliseconds (1/1000 of a second)
# program outputs the average response time for all the samples taken
# during a given hour of the day (regardless of the day)
#
# Print to the shell the following output form:
# Hour: h avg_response_time number_of_samples
#
# There should be 15 lines of output beginning with the hour 6 and ending
# with the hour 22.
#
# You must use the following functions that you write in your program.

#INPUT_FILE = 'date_time_response_time.csv'
def read_file(file_name):
    # this function takes the name of the input file and returns
    # the complete file as a string

    infile = open(file_name,'r')
    file_string = infile.read()
    infile.close()

    return file_string


def file_to_list_of_lines(file_string):
    #This function takes the file as a string for input and returns
    #a list of the lines in the file without the new line characters
    #at the end of the line (split on new line character does that)

    list_of_lines = file_string.split('\n')

    return list_of_lines

def get_hour_from_line(line_string):
    # This function takes the line as a string for input and
    # returns the hour as an integer
    line_string_new = line_string.replace(':',' ')
    line_string_new = line_string_new.replace(',',' ')
    line_string_split = line_string_new.split()
    hour = int(line_string_split[1])
    
            
    
    
    return hour

def get_response_time_from_line(line_string):
    # This function takes the line as a string for input and
    # returns the response time IN SECONDS as a float
    line_string_new = line_string.replace(':',' ')
    line_string_new = line_string_new.replace(',',' ')
    line_string_split = line_string_new.split()
    response_time_in_milliseconds = int(line_string_split[3])
    response_time_in_seconds = response_time_in_milliseconds / 1000
    
    
    return response_time_in_seconds

def add_response_time(response_by_hour, num_of_samples_by_hour):
    #                  hour, response_time):
    # Takes as input 2 lists, both indexed by hour (0 to 22). One is the total
    # of the response time samples for that hour. The other is the number of
    # samples for that hour that have been added. This function modifies both
    # lists but returns NOTHING.
    # After the first sample is read, the lists would look like this:
    # response_by_hour: [0,0,0,0,0,0,7.267,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # num_of_samples_by_hour: [[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    num_of_samples_by_hour=[]
    for i in range(17):
        num_of_samples_by_hour.append(48)
    

    
    return None
                      

def calculate_avg_and_print(response_by_hour, num_of_samples_by_hour,):
    # Takes as input 2 lists, both indexed by hour (0 to 22). One is the total
    # of the response time samples for that hour. The other is the number of
    # samples for that hour that have been added. This function calculates
    # the average for each hour and prints the required output for each hour
    # on a one line.
    # "Hour: "{0:>3}{1:>8.2f}  {2}".format (hour, avg_response_time, num_of_samples)
    plain_hours = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    num_samples_per_hour = 12*4
    each_hour_average = [x/num_of_samples_by_hour for x in response_by_hour]
    for i in range(0, len(plain_hours)):
        print("Hour: {0:>3}{1:>8.2f}  {2}".format(int(plain_hours[i]),each_hour_average[i],num_samples_per_hour))
    

def main():
    #Calls to all the functions go here
    
    my_file = read_file("date_time_response_time.csv")
    my_file_lines = file_to_list_of_lines(my_file)
    hours = []
    times = []
    #splitting the file using the function get_hour_from_line
    for line in my_file_lines:
        hour = get_hour_from_line(line)
        hours.append(hour)

    #splitting the file using the function get_response_time_from_line
    for line1 in my_file_lines:
        time = get_response_time_from_line(line1)
        times.append(time)
    
    
    #creating a list for each day
    day_8_list = times[0:204]
    day_9_list = times[204:408]
    day_10_list = times[408:612]
    day_11_list = times[612:813]
    day_12_list = times[813:1017]

    #summing up all the responses for each hour per day
    day_8_time_list = []
    for x in range(0, len(day_8_list), 12):
        day_8_time_list.append( sum(day_8_list[x:x+12]) )
    
    for x in range(0, len(day_9_list), 12):
        day_8_time_list.append( sum(day_9_list[x:x+12]) )
    

    for x in range(0, len(day_10_list), 12):
        day_8_time_list.append( sum(day_10_list[x:x+12]) )
    

    for x in range(0, len(day_11_list), 12):
        day_8_time_list.append( sum(day_11_list[x:x+12]) )
    
    for x in range(0, len(day_12_list), 12):
        day_8_time_list.append( sum(day_12_list[x:x+12]) )


    #now adding up total response time per hour from each day into 1 list
    added_time = []
    
    for i in range(0 , 17):
        added_time.append(day_8_time_list[i]+day_8_time_list[i+17])
        
    
    #each hour has a set amout of samples: 48
    #this is for the whole document
    samples_per_hour_total = 12 * 4
    
    #using function add_response_time
    add_response_time(added_time,samples_per_hour_total)
    
    #sending lists to calculate_avg_and_print
    calculate_avg_and_print(added_time,samples_per_hour_total)
    


main()

