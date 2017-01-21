def decrypt_story():
    '''
    decrypt_story is a CiphertextMessage object 
    use a helper function get_story_string() that returns the encrypted version of the story as a string
    and decrypt_message to return the appropriate shift value and unencrypted story string
    '''
    story = get_story_string()
    text = CiphertextMessage(story)
    text.decrypt_message()
    # see below the format of how to access a class method 
    # instance = className(argument)
    # instance.method ()
    '''
    class Clock(object):
        def __init__(self, time):
            self.time = time
        def print_time(self):
            time = '6:30'
            print self.time

clock = Clock('5:30')
clock.print_time()'''
    
