import os
import json

from main import hangman
from user import User
# TODO User menu (do not run with second and another game)
def choose_user():
    print("Hi! \n --> If you allready have an account enter 'a' \n --> If you want to create an account enter 'c' \n --> If you just want to play enter 'p' \n --> Press ENTER to quit. \n --: ", sep = '')
    user_input = input()

    if user_input == 'a':
        username = input("Please enter your username: ")
    # load user
        if user_exists(username):
            filename = "{}.txt".format(username) # to user.py
            with open(filename, 'r') as f: 
                json_data = json.load(f)
        else:
            print("User does not exist.")
            return choose_user()

        user = User.from_json(json_data)

        while user_input != 'q':
            play_game(user)
            user_input = input()
        user.save_user()
        
        return choose_user()            
        # TODO ask about statistic

    elif user_input == 'c':
        username = input("Please enter your username: ") #TODO name validation
        while user_exists(username):
            print("Username is allready used, please try another name")
            username = input("Please enter your username: ")  #TODO name validation
        user = User(username)

        while user_input != 'q':
            play_game(user)
            user_input = input()
        user.save_user()

        return choose_user()

    elif user_input == 'p':
        hangman()

        # TODO Ask user if he want to play default difficulty or change something
  
def user_exists(name):
    filename = "{}.txt".format(name)
    return os.path.isfile(filename)

def play_game(user):
    user.add_played_game()
    if hangman():
        user.add_won_game()
    print('If you want to play again press ENTER, if you want to quit press "q"')

