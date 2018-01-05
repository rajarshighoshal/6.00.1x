# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:08:12 2017

@author: RAJARSHI GHOSHAL
"""

balance = float(input("Enter the outstanding balance on the credit card: "))
annualInterestRate = float(input("Enter annual interest rate: "))

monthlyPaymentRate = 0
init_balance = balance
monthlyInterestRate = annualInterestRate/12

while balance > 0:
    for i in range(12):
        balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * monthlyInterestRate)
    if balance > 0:
        monthlyPaymentRate += 10
        balance = init_balance
    elif balance <= 0:
        break
print('Lowest Payment:', monthlyPaymentRate)
