# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:18:13 2017

@author: RAJARSHI GHOSHAL
"""

balance = float(input("Enter outstanding balance on the credit card: "))
annualInterestRate = float(input("Enter annual interest rate as a decimal: "))
monthlyInterestRate = annualInterestRate/12.0

lowerBound = balance/12.0
upperBound = (balance*(1 + monthlyInterestRate)**12)/12.0
epsilon = 0.03

while abs(balance) > epsilon:
    monthlyPaymentRate = (upperBound + lowerBound)/2
    updatedBalance = balance
    
    for i in range(12):
        updatedBalance = updatedBalance - monthlyPaymentRate + ((updatedBalance - monthlyPaymentRate)*monthlyInterestRate)
    
    if updatedBalance > epsilon:
        lowerBound = monthlyPaymentRate
    elif updatedBalance < -epsilon:
        upperBound = monthlyPaymentRate
    else:
        break

print("Lowest payment: ", round(monthlyPaymentRate, 2))