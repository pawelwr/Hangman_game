import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
  """
  Returns a list of valid words. Words are strings of lowercase letters.
  
  Depending on the size of the word list, this function may
  take a while to finish.
  """
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
  """
  wordlist (list): list of words (strings)
  
  Returns a word from wordlist at random
  """
  return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
  '''
  secret_word: string, the word the user is guessing; assumes all letters are lowercase
  letters_guessed: list (of letters), which letters have been guessed so far;
    assumes that all letters are lowercase
  returns: boolean, True if all the letters of secret_word are in letters_guessed;
    False otherwise
  '''
  for char in secret_word:
    if (char in letters_guessed):
      guessed = True
    else:
      guessed = False
      return guessed
  return guessed

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    space = [i if i in letters_guessed else " _" for i in secret_word]
    return "".join(space)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    return ("".join(sorted(set(string.ascii_lowercase) ^ set(letters_guessed))))

def input_letter():
  letter = (input("Please guess a letter: ")).lower()
  return letter
  
class Game:
  def __init__(self, warning, guesses, letters_guessed):
    self.warnings = 3
    self.guesses = 6
    self.letters_guessed = []

  def welcome(self):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

  def information(self):
    print("-------------")
    print("You have", self.guesses ,"guesses left.")
    print("You have", self.warnings ,"warnings left.")
    print("Available letters: ", get_available_letters(self.letters_guessed))

  def hangman(self, letters_guessed, secret_word):
    if len(letters_guessed) == 0: game.welcome()
    self.information()
    self.letters_guessed.append(input_letter())
    user_guess = game.letters_guessed[-1]
    if user_guess in secret_word and user_guess in letters_guessed[:-1]: 
      self.repeated_letter()
    if user_guess in secret_word: 
      self.good_guess()
    if not user_guess in string.ascii_lowercase:
      self.not_letter()
    if user_guess in string.ascii_lowercase and not user_guess in secret_word: 
      self.bad_guess()
    if is_word_guessed(secret_word, letters_guessed): 
      print("You WIN!")
    elif game.guesses == 0: 
      print("You LOST!")
      print("The word is:", secret_word)
    else: return self.hangman(game.letters_guessed, secret_word)

  def warning(self):
    del self.letters_guessed[-1]
    if self.warnings > 0: self.warnings -= 1
    else: self.guesses -= 1

  def not_letter(self):
    self.warning()
    print(" Oops! That is not a valid letter. You have", self.warnings, "warnings left:", get_guessed_word(secret_word, self.letters_guessed))

  def repeated_letter(self):
    self.warning()
    print("You have allready guess that letter. You have", self.warnings, "warnings left") 
  def good_guess(self):
    print ("Good guess:", get_guessed_word(secret_word, self.letters_guessed))

  def bad_guess(self):
    self.guesses -= 1
    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, self.letters_guessed))

secret_word = choose_word(wordlist)
game = Game(3, 6, "")
game.hangman(game.letters_guessed, secret_word)
