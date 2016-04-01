def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    updatedhand = hand.copy()
    if len(word) == 0:
        return False
    
    if word not in wordList:
        return False
    else:

        for i in word:
            if i in updatedhand:
                updatedhand[i] -= 1
            else:
                return False
    #print updatedhand.values()
    for j in updatedhand.values():
            
        if j<0:
            return False
    return True
