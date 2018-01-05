# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:48:14 2018

@author: RAJARSHI GHOSHAL
"""

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i  in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

import pylab as plt

plt.figure('lin')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.xlabel('sample points')
plt.ylabel('quadratic function')
plt.plot(mySamples, myQuadratic)
plt.figure('cube')
plt.xlabel('sample points')
plt.ylabel('cubic function')
plt.plot(mySamples, myCubic)
plt.figure('expo')
plt.xlabel('sample points')
plt.ylabel('exponential function')
plt.plot(mySamples, myExponential)
plt.figure('lin')
plt.title('Linear')
plt.figure('quad')
plt.title('Quadratic')
plt.figure('cube')
plt.title('Cubic')
plt.figure('expo')
plt.title('Exponential')