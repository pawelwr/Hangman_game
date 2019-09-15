import random
import string

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

def hangman():
  game = Game(3, 6, "", "")
  ui = UI()
  ui.show_welcome()
  while Game.is_active(Game):
    ui.present_state()
    ui.guess()
    user_guess = game.input_letter()
    if game.is_letter(user_guess):
      if game.is_reapeted_letter(user_guess, game.letters_guessed):
        game.warning()
        ui.repeated_letter(game.warnings)
      else:
        game.add_letter_to_guessed(user_guess)  
        if game.is_correct_letter(user_guess, game.secret_word):
          ui.good_guess()
        else: 
          game.bad_guess()
          ui.bad_guess()
    else: 
      game.warning()
      ui.not_letter()
  ui.end_of_game(Game.is_word_guessed)
  if input("If you want to play again press A and enter, otherwise press enter: ") == "a" or "A":
    return hangman()
    
class Game(object):
  def __init__(self, 
              warning, guesses, letters_guessed, secret_word):
    Game.warnings = 3
    Game.guesses = 6
    Game.letters_guessed = []
    Game.secret_word = choose_word(wordlist)
    
  def input_letter(self):
    letter = (input()).lower()
    return letter
  
  def is_letter(self, letter):
    if letter in string.ascii_lowercase:
      return True
    else: return False
    
  def add_letter_to_guessed(self, letter):
    if Game.is_letter(self, letter):
      self.letters_guessed.append(letter)
      
  def is_correct_letter(self, 
                      letter, secret_word):
    if letter in secret_word:
      return True
    else: return False
    
  def get_available_letters(self, letters_guessed):
    return ("".join(sorted(set(string.ascii_lowercase) ^ set(Game.letters_guessed))))
  
  def is_word_guessed(secret_word, letters_guessed):
    for char in secret_word:
      if (char in letters_guessed):
        guessed = True
      else:
        guessed = False
        return guessed
    return guessed
  
  def is_reapeted_letter(self, 
                         letter, letters_guessed):
    if letter in letters_guessed:
      return True
    else: return False
  def is_active(self):  
    if self.is_word_guessed(self.secret_word, self.letters_guessed) or self.guesses == 0: 
      return False
    else: 
      return True
    
  def warning(self):
    if Game.warnings > 0: Game.warnings -= 1
    else: Game.guesses -= 1
  def bad_guess(self):
    Game.guesses -= 1

class UI():
  def show_welcome(self):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(Game.secret_word), "letters long.")
    
  def present_state(self):
    print("-------------")
    print("You have", Game.guesses ,"guesses left.")
    print("You have", Game.warnings ,"warnings left.")
    print("Available letters: ", Game.get_available_letters(self, Game.letters_guessed))
    
  def guess(self):
    print("Please guess a letter: ", end = " ")
    
  def get_guessed_word(self, secret_word, letters_guessed):
    space = [i if i in letters_guessed else " _" for i in secret_word]
    return "".join(space)
  
  def get_available_letters(self, letters_guessed):
    return ("".join(sorted(set(string.ascii_lowercase) ^ set(letters_guessed))))
  
  def good_guess(self):
    print ("Good guess:", self.get_guessed_word(Game.secret_word, Game.letters_guessed))
    
  def repeated_letter(self, warnings):
    print("You have allready guess that letter. You have", warnings, "warnings left") 
    
  def bad_guess(self):
    print("Oops! That letter is not in my word:", 
          self.get_guessed_word(Game.secret_word, Game.letters_guessed))
    
  def not_letter(self):
    print(" Oops! That is not a valid letter. You have", Game.warnings,
          "warnings left:", self.get_guessed_word(Game.secret_word, Game.letters_guessed))
    
  def end_of_game(self, is_word_guessed):
    if is_word_guessed(Game.secret_word, Game.letters_guessed):
      print("You WIN!")
      print("-----------")
    else:
      print("You LOST!")
      print("The word is:", Game.secret_word)
      print("-----------")

hangman()
