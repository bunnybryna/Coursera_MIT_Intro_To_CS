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

            
            
        
        
            