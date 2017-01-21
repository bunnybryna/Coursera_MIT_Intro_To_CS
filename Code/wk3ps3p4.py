def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = ''
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in lettersGuessed:
            alpha += letter
    return alpha
            
print 'Available letters: ',getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])
#print getAvailableLetters([])
#print getAvailableLetters(['r', 'u', 'h', 't', 'w', 'm', 'o', 'y', 'z', 'a', 'v', 'i','r'])