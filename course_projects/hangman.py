def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is '+str(len(secretWord))+' letters long'
    numberOfGuess = 8
    guessedLetters=[]
    while (numberOfGuess > 0):
        print '-----------'
        if '_' not in getGuessedWord(secretWord,guessedLetters):
            print 'Congratulations, you won!'
            break
        print 'You have %s guesses left.'%numberOfGuess
        print 'Available letters: %s'%getAvailableLetters(guessedLetters)        
        guess = raw_input('Please guess a letter: ').lower()
        if guess in guessedLetters:
            #print 'Oops! guessed already SECRETWORD: %s    GUESSEDLIST:%s'%(secretWord,guessedLetters)
            print "Oops! You've already guessed that letter: %s" % getGuessedWord(secretWord,guessedLetters)
        elif (guess in secretWord and guess not in guessedLetters):
            guessedLetters.append(guess)
            #print 'Good guess SECRETWORD: %s    GUESSEDLIST:%s'%(secretWord,guessedLetters)

            print 'Good guess: %s'%getGuessedWord(secretWord,guessedLetters)
             

        elif (guess not in secretWord and guess not in guessedLetters):
            guessedLetters.append(guess) 
            #print 'Oops! no match SECRETWORD: %s    GUESSEDLIST:%s'%(secretWord,guessedLetters)
            print 'Oops! That letter is not in my word: %s'%getGuessedWord(secretWord,guessedLetters)
            numberOfGuess -=1
            
    if numberOfGuess == 0:
        print '-----------'
        print 'Sorry, you ran out of guesses. The word was else.'
