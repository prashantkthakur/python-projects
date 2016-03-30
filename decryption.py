def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    bestShift = 0
    maxRealWord = 0
    for i in range(26):
        foundCount = 0
        shifted = applyShift(text,i)
        shiftedList = [word.strip(string.punctuation) for word in shifted.split()]
        for word in shiftedList:
            if word.lower() in wordList:
                foundCount +=1
                if foundCount > maxRealWord:
                    maxRealWord =  foundCount
                    bestShift = i

    return bestShift    

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Once you decrypt the message, be sure to include as a comment
    your decryption of the story.

    returns: string - story in plain text
    """
    ### TODO
    storytxt = getStoryString()
    wordList = loadWords()
    bestShift = findBestShift(wordList,storytxt)


    return applyShift(storytxt, bestShift)
