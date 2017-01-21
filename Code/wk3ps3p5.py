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
    print 'Welcome to the game, Hangman!'
    ls = len(secretWord)
    print 'I am thinking of a word that is ',ls,' letters long.'
    count = 8
    lettersGuessed = []
    while count > 0:
        print '-' * 10
        print 'You have ',count,' guesses left.'
        print 'Available letters: ', getAvailableLetters(lettersGuessed)
        letterGuess = raw_input('Please guess a letter: ')
        letterGuess = letterGuess.lower()
        if letterGuess in lettersGuessed:
            print "Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed)
            continue
        lettersGuessed.append(letterGuess)
        if letterGuess in secretWord:
            print 'Good guess: ', getGuessedWord(secretWord, lettersGuessed)
            if isWordGuessed(secretWord, lettersGuessed) is True:
                print '-' * 10
                print 'Congratulations, you won!'
                break               
            
        else:
            print 'Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed)
            count -= 1
            if count == 0:
                print '-' * 10
                print 'Sorry, you ran out of guesses. The word was ',secretWord,'.'
                break