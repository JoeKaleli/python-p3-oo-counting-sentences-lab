#!/usr/bin/env python3

class MyString():
    

    def __init__ (self, string):
        self.string = string

    def is_sentence(self):
        if self.string.endswith('.'):
            return True
        else:
          return False
        
    def is_question(self):
        if self.string.endswith('?'):
            return True
        else:
            return False
        
    def count_sentences(self):
        # Split the string into sentences based on periods
        sentences = self.value.split('.')
        # Filter out any empty strings (e.g., caused by consecutive periods)
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        # Return the count of sentences
        return len(sentences)
