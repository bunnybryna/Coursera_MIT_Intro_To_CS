def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word in wordList:
        for letter in word:
            number = word.count(letter)
            # check if all the letters are in the hand
            # dict.get(key,0) method won't raise an error
            # if the key is not in the dictionary
            if number <= hand.get(letter,0):
                continue
            else:
                return False
        return True
    else:
        return False
