
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # for l in secretWord, if l in lettersGuessed
    # instead of lettersGuessed,if l in secretWord
    # because if there is one letter in secret not guessed, lose
    # use continue
    for letter in secretWord:
        if letter in lettersGuessed:
            continue
        else: 
            return False
    if not False:
        return True
        

print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])        
    if isWordGuessed('apple', ['a']):
        print 'a'
    
check()