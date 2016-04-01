def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    caesarDict = {}
    for letter in lower:
        for i in lower:
            caesarDict[i] = lower[(lower.index(i)+shift)%26]
            caesarDict[i.upper()] = lower[(lower.index(i)+shift)%26].upper()


    return caesarDict 


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO
    cipher = []
    for letter in text:
        if (letter in string.punctuation or letter in string.whitespace or letter in string.digits):
            cipher.append(letter)
        else:
            cipher.append(coder[letter])

    return ''.join(cipher)
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift)) 
