class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        self.shiftDict = {}
        lowerStr = 'abcdefghijklmnopqrstuvwxyz'
        for letter in lowerStr:
            newInd = lowerStr.index(letter)+shift
            if newInd < 26:
                newInd = newInd
            # make sure to it won't run out index by starting from 'a' again    
            else:
                newInd = newInd - 26
            self.shiftDict[letter]= lowerStr[newInd]
        # same thing for uppercase     
        upperStr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for letter in upperStr:
            newIND = upperStr.index(letter)+shift
            if newIND < 26:
                newIND = newIND
            else:
                newIND = newIND - 26
            self.shiftDict[letter]= upperStr[newIND]
            
        return self.shiftDict    
        

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        self.newMessage = ''
        for each in self.message_text:
            if each in string.punctuation or each == ' ':
                newOne = each
            elif each in string.digits:
                newOne = each
            else:
            # apply the shift dictionary
            # this is how to use previous attributes under the same class
            # notice that build_shift_dict takes two argument, one is self(already given), the other is shift
                newOne = self.build_shift_dict(shift)[each]
            self.newMessage = self.newMessage + newOne
        return self.newMessage
            