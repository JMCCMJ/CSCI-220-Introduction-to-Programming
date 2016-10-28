##
## Name: <Jan-Michael Carrington>
## <usury>.py
##
## Purpose: <This program calculates the priniple payments on a car or home
## purchase. It will tell exactly how much interest will be paid
## over the period of the loans. It also will tell the total payment.>
##
##
## Certification of Authenticity:  
##   
##   I certify that this lab is entirely my own work.
##   
##
## Input: <The principal amount, the length of the loan in months,
## and the interest rate.>
## Output: <The principal payment each month, amound paid over the life of the
## loan, and the total interest paid.>

"""
Program 1 Usury

Author: <Jan-Michael Carrington>

Purpose: Calculate the monthly payment, total amount paid, and total interest paid for a loan.

Inputs:
1.principal
2.months
3.interest rate

Outputs:
1.monthly payments
2.total payment
3.total interest paid

Authenticity:
  I certify that this program is entirely my work.
"""
def main():

    print('This program calculates the monthly payment, total amound paid, and total interest paid over the course of a loan.')
    # Get inputs
    principal = eval(input("Enter the loan amount: $"))
    months = eval(input("Enter the length of the loan in months: "))
    interest = eval(input('Enter the interest rate (ex. "4.3" for 4.3%) '))
    

    # Calculate outputs

    rate = interest / 1200
    monthly_payment = (principal * (rate * (1 + rate)**months)) / ((1 + rate)**months - 1)
    total_payment = monthly_payment * months
    total_interest = total_payment - principal

    # Print the outputs with text to explain what they are
    print("The monthly payment is $", monthly_payment,sep="")
    print("The total amount paid is $",total_payment,sep="")
    print("The total interest paid is $",total_interest,sep="")
    
main()
