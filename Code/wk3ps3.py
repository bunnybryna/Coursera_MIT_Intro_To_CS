
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
        
            
#print isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])
#print isWordGuessed('broccoli', ['z', 'x', 'q', 'b', 'r', 'o', 'c', 'c', 'o', 'l', 'i'])

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ls = len(secretWord)
    word = '_' * ls
    for letter in lettersGuessed:
        num = secretWord.count(letter)
        # if num=1,.find()will return the index
        # if num>=2,.find() will return the first one
        # and go to the while block,.find(,beg) method will give the next index
        # and when num-1=0 will get out of the loop
        if num > 0 :
            ind = secretWord.find(letter)
            rightWord = secretWord[ind]
            word = word[:ind]+rightWord+word[ind+1:]
            num = num-1
            while num >= 1:
                ind2 = secretWord.find(letter,ind+1)
                rightWord2 = secretWord[ind2]
                word = word[:ind2]+rightWord2+word[ind2+1:]
                num = num - 1
                ind = ind2
        if num == 0:
            continue
    # add a space after each underscore
    # it's clear to the user how many unguessed letters are left in the string
    holder = ''
    for i in range(len(word)):
        holder = holder + word[i] + ' '
     
    return holder

print getGuessedWord('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])
print getGuessedWord('broccoli', ['z', 'x', 'q', 'b', 'r', 'o', 'c', 'c', 'o', 'l', 'i'])    

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
            