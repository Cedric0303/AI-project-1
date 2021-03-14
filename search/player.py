import search.board

from search.token import Rock, Paper, Scissors, Block

class Player():

    token_list = list()

    def clear_token_list(self):
        
        self.token_list.clear()

class Upper(Player):

    token_list = list()

    def __init__(self, token_data):
        self.name = 'upper'
        for token, x, y in token_data:
            if token == 'r':
                self.token_list.append(Rock(token.upper(), x, y))
            elif token == 'p':
                self.token_list.append(Paper(token.upper(), x, y))
            elif token == 's':
                self.token_list.append(Scissors(token.upper(), x, y))


class Lower(Player):
    
    token_list = list()

    def __init__(self, token_data):
        
        self.name = 'lower'
        for token, x, y in token_data:
            if token == 'r':
                self.token_list.append(Rock(token.lower(), x, y))
            elif token == 'p':
                self.token_list.append(Paper(token.lower(), x, y))
            elif token == 's':
                self.token_list.append(Scissors(token.lower(), x, y))

class Non_player(Player):
    
    token_list = list()

    def __init__(self, token_data):
        
        self.name = 'Block'
        for token, x, y in token_data:
            self.token_list.append(Block("\"\"", x, y))

