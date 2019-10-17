from game import Game


class UI(Game):
    def start_game(self):
        print("I am thinking of a word that is", len(self.secret_word), "letters long.")
    def present_state(self, guesses, warnings, available_letters):
        print("-------------")
        print("You have", guesses ,"guesses left.")
        print("You have", warnings ,"warnings left.")
        print("Available letters: ", available_letters)
    def guess(self):
        print("Please guess a letter: ", end = " ")
    def get_guessed_word(self, secret_word, letters_guessed):
        space = [i if i in letters_guessed else " _" for i in secret_word]
        return "".join(space)
    def good_guess(self):
        print ("Good guess:", sep = ' ')
    def repeated_letter(self, warnings):
        print("------------- \nYou have allready guess that letter. You have", warnings, "warnings left") 
    def bad_guess(self):
        print("Oops! That letter is not in my word:", sep = ' ')
    def not_letter(self):
        print(" Oops! That is not a valid letter. You have", self.warnings, "warnings left:", sep = ' ')
    def won_game(self):
            print("You WIN!")
            print("-----------")
    def lost_game(self, secret_word):
            print("You LOST! \n The word is:" + secret_word + "\n-----------")
