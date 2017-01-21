class PlaintextMessage(Message):
    def __init__(self,text,shift):
        # use the parent class constructor 
        Message.__init__(self,text)
        self.shift = shift
        # note use self.shift instead of shift all the time
        self.encrypting_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)
        
    def get_shift(self):
        return self.shift
        
    def get_encrypting_dict(self):
        # {} is unhashable, can't use [:] to make a copy
        return self.encrypting_dict.copy()
        
    def get_message_text_encrypted(self):
        return self.message_text_encrypted 
        
    def change_shift(self,shift):
    # just update shift by doing sth. similar to the __init__ procedure
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)
        