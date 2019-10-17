import string
import random

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

class Game(object):
    def __init__(self):
        self.warnings = 3
        self.guesses = 6
        self.letters_guessed = []
        self.secret_word = choose_word(wordlist)

    def input_letter(self):
        letter = (input()).lower()
        return letter

    def is_letter(self, letter):
        if letter in string.ascii_lowercase:
            return True
        else: return False

    def add_letter_to_guessed(self, letter):
        if self.is_letter(letter):
            self.letters_guessed.append(letter)

    def is_correct_letter(self, letter, secret_word):
        if letter in secret_word:
            return True
        else: return False

    def get_available_letters(self, letters_guessed):
        return ("".join(sorted(set(string.ascii_lowercase) ^ set(self.letters_guessed))))

    def is_word_guessed(self, secret_word, letters_guessed):
        for char in secret_word:
            if (char in letters_guessed):
                guessed = True
            else:
                guessed = False
                return guessed
        return guessed

    def is_reapeted_letter(self, letter, letters_guessed):
        if letter in letters_guessed:
            return True
        else: return False

    def is_active(self):  
        if self.is_word_guessed(self.secret_word, self.letters_guessed) or self.guesses == 0: 
            return False
        else: 
            return True

    def subtract_warning(self):
        if self.warnings > 0: self.warnings -= 1
        else: self.guesses -= 1

    def subtract_guess(self):
        self.guesses -= 1

    def get_present_state(self):
        return self.guesses, self.warnings, self.get_available_letters(self.letters_guessed)

'''
    def get_guessed_word(self, secret_word, letters_guessed):
        space = [i if i in letters_guessed else " _" for i in secret_word]
        return "".join(space)

    def get_guesses(self):
        return self.guesses
'''