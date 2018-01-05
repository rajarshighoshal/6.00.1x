# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 21:52:05 2017

@author: RAJARSHI GHOSHAL
"""

def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    # getting a index and letter score pair
    letterScoreList = {}
    
    wordLower = word.lower()
    
    for i in range(len(word)):
        letterScoreList.update({str(i) : (ord(wordLower[i]) - ord('a') + 1)})
    
    # calculating positioned score based on index and letter score pair
    scoreList = []
    for k, v in letterScoreList.items():
        scoreList.append(int(k) * int(v))
    
    max1 = max(scoreList)
    scoreList.remove(max1)
    max2 = max(scoreList)
    
    return f(max1, max2)
    