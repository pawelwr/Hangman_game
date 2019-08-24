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
    space = ["_ " for i in range(len(secret_word))]
    for char in secret_word:
        if char in letters_guessed:
            space[i] = char
        i += 1
    return "".join(space)

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    list_of_letters = list(string.ascii_lowercase)
    for char in letters_guessed:
        if char in list_of_letters:
            list_of_letters.remove(char)
    return("".join(list_of_letters))

def input_letter():
  letter = (input("Please guess a letter: ")).lower()
  return letters_guessed.append(letter)

#class mess(object)
#  def __init__(self, text) 

def messages():
  """
  text messages for user
  """
  if (letters_guessed[-1] in letters_guessed[:-1]) and warnings > 0:
    print("Oops! You've already guessed that letter. You have", warnings - 1, "warnings left", get_guessed_word(secret_word, letters_guessed))
  elif (letters_guessed[-1] in letters_guessed[:-1]) and warnings <= 0:
    print("Oops! You've already guessed that letter. You have 0 warnings left", get_guessed_word(secret_word, letters_guessed))    
  elif letters_guessed[-1] in secret_word:
    print("Good guess:", get_guessed_word(secret_word, letters_guessed))
  elif (not letters_guessed[-1] in string.ascii_lowercase) and (warnings > 0):
    print(" Oops! That is not a valid letter. You have", warnings - 1, "warnings left:", get_guessed_word(secret_word, letters_guessed))
  elif ((not letters_guessed[-1] in string.ascii_lowercase) and (warnings > -1)):
    print(" Oops! That is not a valid letter. You have 0 warnings left:", get_guessed_word(secret_word, letters_guessed))
  else: 
      print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))  

def hangman(secret_word):

  print(secret_word)
  print("-------------")
  print("You have", guesses ,"guesses left.")
  print("You have", warnings ,"warnings left.")
  print("Available letters: ", get_available_letters(letters_guessed))
  input_letter()
  messages()

letters_guessed = []
guesses = 6
warnings = 3
secret_word = choose_word(wordlist)
print("Welcome to the game Hangman!")
print("I am thinking of a word that is", len(secret_word), "letters long.")
hangman(secret_word)    
while guesses > 0:
  hangman(secret_word)
  if (not (letters_guessed[-1] in string.ascii_lowercase)) or (letters_guessed[-1] in letters_guessed[:-1]):
    if warnings > 0:
      warnings -= 1
    else:
      guesses -= 1
  elif (letters_guessed[-1] in string.ascii_lowercase) and (not letters_guessed[-1] in secret_word):
        guesses -= 1
  if is_word_guessed(secret_word, letters_guessed):
    print("Congratulation! You WIN!")
    break
  elif guesses == 0:
    print ("You LOST!")
    break
