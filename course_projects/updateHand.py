def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    updatedhand =dict(hand) # To create a copy of hand and not the reference of same dictionary
    for i in word:
        #for j in hand.keys():
        if i in updatedhand:
            #print j, hand[j]
            updatedhand[i]=(updatedhand[i] - 1)
            if updatedhand[i] == 0:
                updatedhand.pop(i)

    return updatedhand
