from game import Game
from UI import UI
import menu

def hangman():
    game = Game()
    ui = UI()
    ui.start_game()
    result = False
    while game.is_active():
        ps = game.get_present_state() # tuple representation of game present state in order: guesses, warnings, available letters
        ui.present_state(ps[0], ps[1], ps[2])
        ui.guess()
        user_guess = game.input_letter()
        if game.is_letter(user_guess): # checking if user input is letter value
            if game.is_reapeted_letter(user_guess, game.letters_guessed): # checking if user do not enter this letter before
                game.subtract_warning()
                ui.repeated_letter(game.warnings)
                continue # ask again for letter if it is reapeted letter
            else:
                game.add_letter_to_guessed(user_guess) # add a letter to letters guessed in object
            if game.is_correct_letter(user_guess, game.secret_word): 
                ui.good_guess()
            else: 
                game.subtract_guess()
                ui.bad_guess()
        else: 
            game.subtract_warning()
            ui.not_letter()
        print(ui.get_guessed_word(game.secret_word, game.letters_guessed))
    if game.is_word_guessed(game.secret_word, game.letters_guessed):
        ui.won_game()
        result = True
    else:
        ui.lost_game(game.secret_word)
    return result

#if __name__ == '__main__':
#    hangman()

if __name__ == '__main__':
    menu.choose_user()