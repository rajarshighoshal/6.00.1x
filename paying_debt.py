# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:02:33 2017

@author: RAJARSHI GHOSHAL
"""
def remainingBalance(balance, interestRate, paymentRate):
    """ 
    function that takes balance at the start of the month;
    takes monthly interest rate and takes monthly payment rate;
    and returns remaining balance at the end of the month
    """
    # monthly interest rate
    mirate = interestRate/12.0
    # minimum monthly payment
    mmpay = paymentRate*balance
    # monthly unpaid balance
    upbalance = balance - mmpay
    # updated balance for this month
    newBalance = upbalance + mirate*upbalance
    
    # return updated balance
    return newBalance

def main():
    """ main function to get input and calculate result """
    # getting inputs
    balance = float(input())
    annualInterestRate = float(input())
    monthlyPaymentRate = float(input())
    
    # passing inputs to remainingBalance function for 12 consecutive months
    for i in range(0, 12):
        balance = remainingBalance(balance, annualInterestRate, monthlyPaymentRate)
    
    # print remaining balance upto 2 decimal places at the end of the year
    print("Remaining balance: ", round(balance, 2))
       
    
if __name__ == "__main__": main()
