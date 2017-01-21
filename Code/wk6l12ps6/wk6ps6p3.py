class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self,text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''

        self.maxWord = None
        self.maxShift = None
        for s in range(26):
            # !!! note that count = 0 should be here, not out of the loop with maxWord and maxShift
            # because for every s, count should be reset to zero each time
            self.countWord = 0
            self.encrypting_dict = self.build_shift_dict(s)
            self.message_text_encrypted = self.apply_shift(s)
            for word in self.message_text_encrypted.split(' '):
            # self.valid_words is Message's attribute
            # it returns a copy of valid words using loaded word_list
                if (is_word(self.valid_words,word)):
                    self.countWord += 1
            if self.maxWord is None or self.countWord > self.maxWord:
                self.maxWord = self.countWord
                self.maxShift = s
        return (self.maxShift, self.apply_shift(self.maxShift))  
        