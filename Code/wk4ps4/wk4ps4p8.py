import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList
    
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    total = 0
    ls = len(word)
    for letter in word:
        point = SCRABBLE_LETTER_VALUES[letter]
        total += point
    # PLUS 50 points if all n letters are used on the first turn    
    if ls == n:
        return (total * ls) + 50 
    else:
        return total * ls
        
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
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
    # .copy()returns a shallow copy
    handCopy = hand.copy()
    for letter in word:
        handCopy[letter]-=1
    return handCopy
        
        
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
        
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    length = 0
    for value in hand.values():
        length += value
    return length

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    totalScore = 0
    n = calculateHandlen(hand)
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) != 0:  
        # Display the hand
        print 'Current hand: ',
        displayHand(hand)
        # Ask user for input
        guessWord = raw_input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if guessWord == '.':
            # End the game (break out of the loop)
            print 'Goodbye! Total score: ',totalScore, 'points.' 
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(guessWord, hand, wordList) != True:
                # Reject invalid word (print a message followed by a blank line)
                print 'Invalid word, please try again.'
                print 
                continue
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score = getWordScore(guessWord, n) 
                totalScore += score
                print '"',guessWord,'"earned',score,'points. Total: ',totalScore ,'points.'
                print 
                # Update the hand 
                hand = updateHand(hand, guessWord)
                calculateHandlen(hand)
                continue
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand) == 0:
        print 'Run out of letters. Total score: ',totalScore,'points.'          
        
        
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for words in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(words, hand, wordList) == True: 
            # Find out how much making that word is worth
            point = getWordScore(words, n)    
            # If the score for that word is higher than your best score
            if point > maxScore:
                # Update your best score, and best word accordingly
                maxScore = point
                bestWord = words
    # return the best word you found.
    return bestWord

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # keep track of total score
    totalScore = 0
    while calculateHandlen(hand) != 0:
        print 'Current hand: ',
        displayHand(hand)
        chooseWord = compChooseWord(hand, wordList, n)
        # if there is more words can be formed using letters in hand
        if chooseWord != None:
            scoreNow = getWordScore(chooseWord, n)
            totalScore += scoreNow
            print "'",chooseWord,"' earned ",scoreNow,'points. Total: ',totalScore ,'points.'
            print 
            # Update the hand 
            hand = updateHand(hand, chooseWord)
            calculateHandlen(hand)
            continue
        else:
            break
    print 'Total score: ',totalScore,'points.'        

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    count = 0
    while True:
        usInput = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')    
        if usInput == 'e':
            break
        elif usInput == 'r' :
            if count == 0:
                print 'You have not played a hand yet. Please play a new hand first!'
                print 
                # continue is to start over again from very beginning-
                # move to first tier question, choose n, r or e
                continue
            elif count > 0:
                usChoose = raw_input('Enter u to have yourself play, c to have the computer play: ')
                print 
                if usChoose == 'u':
                    playHand(hand, wordList, n)
                    continue
                elif usChoose == 'c':
                    compPlayHand(hand, wordList, n)
                    continue
                else:
                    print 'Invalid command.'
                    continue

        elif usInput == 'n':
            # need two while loops here, because when invalid command is given, need to move to the second tier question, choose u or c
            # and when one hand is done, then move to the first tier question, choose n, r or e
            while True:
                usChoose = raw_input('Enter u to have yourself play, c to have the computer play: ')
                print 
                if usChoose == 'u':
                    n = HAND_SIZE
                    hand = dealHand(n)
                    playHand(hand, wordList, n)
                    count += 1
                    break
                elif usChoose == 'c':
                    n = HAND_SIZE
                    hand = dealHand(n)
                    compPlayHand(hand, wordList, n)
                    count += 1
                    break
                else:
                    print 'Invalid command.'
                    continue    
            continue
        else:
            print 'Invalid command.'
            continue

wordList = loadWords()    
playGame(wordList) 