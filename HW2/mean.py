import math

#Jan-Michael Carrington
#Computer Science 220
#8:30 AM MWF Class

##1. This program will calculate the RMS Average and the Harmonic Mean
##of a set of numbers.
##2. The inputs will be the amount of numbers used and the actual numbers.
##The outputs will be the RMS average and Harmonic Mean.
##3. First the program  states what will be done. Then it will get the input
##of the amount of numbers the user will input. It will then ask for the numbers.
##The program will then calculate the RMS and Harmonic from these numbers.
##Then the program outputs the answers.


print("This program calculates the RMS Average and the Harmonic Mean of a set of numbers. (*Note 0 cannot be one of the numbers)")
#Here I get the number of loops need.
loops = eval(input("Enter the amount of numbers that will be used: "))

first_num = eval(input("Enter the first number: "))

#Algorithms
squared_first = first_num**2
first_harm = 1 / first_num

total = 0
total_harm = 0
for i in range(loops - 1):
    num_input = eval(input("Enter the next number: "))
    total = total + num_input**2
    total_harm = total_harm + (1 / num_input)
    
#Calculations of RMS sum and Harmonic sum.
rms_total = total + squared_first
harm_total = first_harm + total_harm

#Calculations of RMS and Harmonic average.
rms_average = math.sqrt(rms_total / loops)
harmonic_mean = loops /  harm_total




print("The RMS Average is",rms_average, end=".")
print("\n")
print("The Harmonic Mean is",harmonic_mean, end=".")
