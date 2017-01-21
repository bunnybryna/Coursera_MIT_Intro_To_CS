# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter in lettersGuessed:
            continue
        else: 
            return False
    if not False:
        return True
        



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
        print 'Available letters: '
        print getAvailableLetters(lettersGuessed)
        letterGuess = raw_input('Please guess a letter: ')
        letterGuess = letterGuess.lower()
        if letterGuess in lettersGuessed:
            print "Oops! You've already guessed that letter: "
            print getGuessedWord(secretWord, lettersGuessed)
            continue
        lettersGuessed.append(letterGuess)
        if letterGuess in secretWord:
            print 'Good guess: '
            print getGuessedWord(secretWord, lettersGuessed)
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





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
