import json

class User:
    def __init__(self, name, played_games = 0, won_games = 0):
        self.name = name
        self.played_games = played_games
        self.won_games = won_games
    
    #TODO default difficult level

    def add_won_game(self):
        self.won_games += 1

    def add_played_game(self):
        self.played_games += 1

    #TODO player statistic

    #TODO history of words

    # json user repr
    def json(self):
        return {
            'name': self.name,
            'played_games': self.played_games,
            'won_games': self.won_games
        }
    
    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        user.played_games = json_data['played_games']
        user.won_games = json_data['won_games']
        return user

    def save_user(self):
        filename ="{}.txt".format(self.name)
        with open(filename, 'w') as f:
            json.dump(self.json(), f)
            