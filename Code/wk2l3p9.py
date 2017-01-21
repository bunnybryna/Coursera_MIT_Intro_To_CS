low = 0.0
high = 100.0
print 'Please think of a number between 0 and 100!'
while True:
    ans = int((low + high)/2)
    question1 = 'Is your secret num ' + str(ans) + ' ? '
    print question1
    question2 = """Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.Enter 'c' to indicate I guessed correctly."""
    reply = raw_input(question2)
    if reply == 'h':
        high = ans
    elif reply == 'l':
        low = ans
    elif reply == 'c':
        break
    else:
        print 'Sorry, I did not understand your input.'
        continue
        
print 'Game over. Your secret number was:' + str(ans) 