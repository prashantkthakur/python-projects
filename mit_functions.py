def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    sum =0
    for i in hand.values():
        sum += i
    return sum    
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)
    localHand = hand.copy()
    #print type(localHand)
    gameover = False
    totalScore = 0
    while gameover != True:
        print 'Current Hand:  ', 
        displayHand(localHand)
        userinput = str(raw_input('Enter word, or a "." to indicate that you are finished: '))
        if userinput == '.':
            gameover = True

        else:
            if  isValidWord(userinput, localHand, wordList):

                localHand = updateHand(localHand,userinput)
                totalScore += getWordScore(userinput, calculateHandlen(hand))
                if all(val ==0 for val in localHand.values()):
                    print '"%s" earned %d points. Total: %d points' %(userinput, getWordScore(userinput,calculateHandlen(hand)),totalScore)
                    print '\nRun out of letters. Total score: %d points.'%totalScore
                    break
                else:
                    print '"%s" earned %d points. Total: %d points' %(userinput, getWordScore(userinput,calculateHandlen(hand)),totalScore)

            else:
                print 'Invalid word, please try again.'
        if gameover:
            print 'Goodbye! Total score: %d points.'%totalScore 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    # TO DO ... <-- Remove this comment when you code this function
    hand = False
    gamecontrol =''
    while gamecontrol != 'e':
        gamecontrol = str(raw_input ('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if gamecontrol not in 'rne':
            print 'Invalid command.'
        elif gamecontrol == 'r' and not hand:
            print 'You have not played a hand yet. Please play a new hand first!'
        elif gamecontrol == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand,wordList,HAND_SIZE)
        elif gamecontrol == 'r' and hand:
            playHand(hand,wordList,HAND_SIZE)
        else:
            break
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE (available within ps4b.py)
    maxScore = 0
    bestWord =None
    for word in wordList:
        if isValidWord(word,hand,wordList):
            #print hand
            if maxScore < getWordScore(word,len(word)):
                bestWord = word
                #print bestWord
                maxScore = getWordScore(word,len(word))
                #print maxScore

    return bestWord
def compChooseWord(hand, wordList, n):

    maxScore = 0
    bestWord = None
    for word in wordList:
        if isValidWord(word,hand,wordList):
            #print hand
            if maxScore < getWordScore(word,len(word)):
                bestWord = word
                #print bestWord
                maxScore = getWordScore(word,len(word))
                #print maxScore

    return bestWord



def compPlayHand(hand, wordList, n):
    totalScore = 0
    compWord = ''
    gameover = False
    myval = True
    localhand = hand.copy()
    while not gameover:
        
        #print compWord
   # try:
        if (compWord != None and calculateHandlen(localhand) != 0 ):
            print 'Current Hand:  ', 
            displayHand(localhand)
            compWord = compChooseWord(localhand, wordList,n)
            #print compWord
            if compWord != None:
                totalScore += getWordScore(compWord, n)
            #print totalScore
                localhand = updateHand(localhand,compWord)
                print '"%s" earned %d points. Total: %d points'%(compWord,getWordScore(compWord,n),totalScore)

        if (compWord == None or calculateHandlen(localhand) == 0):
            gameover = True
            print 'Total score: %d points.'%totalScore
            break
def playGame(wordList):
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
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO...
    finalval = 'temp'
    hand = False
    while finalval != 'e':
        finalval = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if finalval not in 'nre':
            print 'Invalid command.'
        elif finalval == 'r' and not hand:
            print "You have not played a hand yet. Please play a new hand first!"
        elif finalval == 'n':
            hand = dealHand(HAND_SIZE)
            myinput = 'temp'
            while (myinput != 'u' or myinput != 'c'):
                myinput = raw_input('Enter u to have yourself play, c to have the computer play: ')
                
                if myinput == 'u':
                    playHand(hand,wordList,HAND_SIZE)
                    break
                elif myinput == 'c':
                    compPlayHand(hand,wordList,HAND_SIZE)
                    break
                else:
                    print 'Invalid command.'
        elif finalval == 'r' and hand:
            
            while (myinput != 'u' or myinput != 'c'):
                myinput = raw_input('Enter u to have yourself play, c to have the computer play: ')
                if myinput == 'u':
                    playHand(hand,wordList,HAND_SIZE)
                    break
                elif myinput == 'c':
                    compPlayHand(hand,wordList,HAND_SIZE)
                    break
                else:
                    print 'Invalid command.'
        else:
            break
