from ps4a import *
import time


#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordScoreDict, n):
    """
    Given a hand and a wordScoreDict, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordScoreDict.

    If no words in the wordScoreDict can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordScoreDict: dictionary (string -> int), containng score for each word
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """   
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordScoreDict.keys():
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordScoreDict.keys()):
            # find out how much making that word is worth
            score = wordScoreDict[word]
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord

#
# Computer plays a hand
#
def compPlayHand(hand, wordScoreDict, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordScoreDict: dictionary (string -> int), containing score for each word
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordScoreDict, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWord(word, hand, wordScoreDict.keys())) :
                print('This is a terrible error! I need to check my own code!')
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the updated total score
                if(getWordScore(word, n) != wordScoreDict[word]):
                    print('Something wrong happend!!! immediately check code')
                    return 'error occured'
                score = wordScoreDict[word]
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')

    
#
# Problem #6: Playing a game
#
#
def playGame(wordScoreDict):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    
    wordScoreDict: Dictionary (string -> int), containing score for each word
    """
    # creating an empty hand to mark start of the game
    hand = {}
    # making a while loop for continuous playing
    while True:
        # asking for user input 'n', 'r' or 'e'
        data = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        # if user wants to play new hand
        if data == 'n':
            # creating new hand
            hand = dealHand(HAND_SIZE)
            # looping until correct input
            flag = True
            while flag:
                # computer or yourself
                player = input("Enter u to have yourself play, c to have the computer play: ")
                # calling playhand function for playing the hand by user
                if player == 'u':
                    playHand(hand.copy(), wordScoreDict.keys(), HAND_SIZE)
                    flag = False
                # calling compPlayHand function for playing the hand by computer
                elif player == 'c':
                    compPlayHand(hand.copy(), wordScoreDict, HAND_SIZE)
                    flag = False
                # for all other inputs show invalid
                else:
                    print("Invalid command.")
        # if user wants to repeat the previous hand
        elif data == 'r':
            # if hand is empty ask for different input
            if hand == {}:
                print('You have not played a hand yet. Please play a new hand first!')
            # else proceed
            else:
                # looping until proper input
                flag = True
                while flag:
                    # computer or yourself
                    player = input("Enter u to have yourself play, c to have the computer play: ")
                    # calling playhand function for playing the hand by user
                    if player == 'u':
                        playHand(hand.copy(), wordScoreDict.keys(), HAND_SIZE)
                        flag = False
                    # calling compPlayHand function for playing the hand by computer
                    elif player == 'c':
                        compPlayHand(hand.copy(), wordScoreDict, HAND_SIZE)
                        flag = False
                    # for all other inputs show invalid
                    else:
                        print("Invalid command.")
        # if user wants to end the game
        elif data == 'e':
            break
        # for all other inputs show invalid input
        else:
            print('Invalid command.')
    # print a blank line
    print()
    

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    # creating wordscoredictionary for fast computing
    wordScoreDict = {}
    for word in wordList:
        wordScoreDict[word] = getWordScore(word, n)
    
    playGame(wordScoreDict)


