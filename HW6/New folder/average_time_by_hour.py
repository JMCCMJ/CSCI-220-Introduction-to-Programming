# average_time_by_hour.py

# answers to T/F, Multiple Choice and Discussion on p194-196 (30% of hw grade)


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

INPUT_FILE = 'date_time_response_time.csv'
def read_file(file_name):
    # this function takes the name of the input file and returns
    # the complete file as a string

    return file_string

def file_to_list_of_lines(file_string):
    # This function takes the file as a string for input and returns
    # a list of the lines in the file without the new line characters
    # at the end of the line (split on new line character does that)

    return list_of_lines

def get_hour_from_line(line_string):
    # This function takes the line as a string for input and
    # returns the hour as an integer

    return hour

def get_response_time_from_line(line_string):
    # This function takes the line as a string for input and
    # returns the response time IN SECONDS as a float

    return response_time_in_seconds

def add_response_time(response_by_hour, num_of_samples_by_hour,
                      hour, response_time):
    # Takes as input 2 lists, both indexed by hour (0 to 22). One is the total
    # of the response time samples for that hour. The other is the number of
    # samples for that hour that have been added. This function modifies both
    # lists but returns NOTHING.
    # After the first sample is read, the lists would look like this:
    # response_by_hour: [0,0,0,0,0,0,7.267,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # num_of_samples_by_hour: [[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def calculate_avg_and_print(response_by_hour, num_of_samples_by_hour):
    # Takes as input 2 lists, both indexed by hour (0 to 22). One is the total
    # of the response time samples for that hour. The other is the number of
    # samples for that hour that have been added. This function calculates
    # the average for each hour and prints the required output for each hour
    # on a one line.
    # "Hour: "{0:>3}{1:>8.2f}  {2}".format (hour, avg_response_time, num_of_samples)

def main():
    # Calls to all the functions go here


main()

