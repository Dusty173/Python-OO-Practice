"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine that reads from a .txt file and retrieves a random word
    >>> wf = WordFinder("simple.txt")
    3 words read.

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    
    def __init__(self, path):
        """Reads through word file and reports number of words read."""

        word_file = open(path)
        self.words = self.read(word_file)
        print(f'{len(self.words)} words read.')

    def read(self, word_file):
        """Take words in given file of words and returns a list of words."""
        return [words.strip() for words in word_file]
    
    def random(self):
        """Returns a random word from words"""
        return random.choice(self.words)
    
    
    
class SpecialWordFinder(WordFinder):
    """Machine that takes a different style of word input (with spaces, comments, etc.) and attempts to output same behavior of WordFinder class
    
    >>> swf = SpecialWordFinder('otherwords.txt')
    4 words read.

    >>> swf.random() in ['apple', 'mango', 'kale', 'parsnips']
    True

    >>> swf.random() in ['apple', 'mango', 'kale', 'parsnips']
    True
    """
    def read(self, word_file):
        """Read from word_file and turn into list without any spaces/comments."""
        return [words.strip() for words in word_file if words.strip() and not words.startswith('#')]