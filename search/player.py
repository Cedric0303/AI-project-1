import search.board

from search.token import rock, paper, scissors, block

class Player():

    token_list = []

    def clear_token_list(self):
        
        self.token_list = []

class Upper(Player):

    token_list = []

    def __init__(self, token_data):
        
        self.name = 'upper'
        for token, x, y in token_data:
            if token == 'r':
                self.token_list.append(rock(token.upper(), x, y))
            elif token == 'p':
                self.token_list.append(paper(token.upper(), x, y))
            elif token == 's':
                self.token_list.append(scissors(token.upper(), x, y))
        #elif isinstance(token_data, list()):



class Lower(Player):
    
    token_list = []

    def __init__(self, token_data):
        
        self.name = 'lower'
        for token, x, y in token_data:
            if token == 'r':
                self.token_list.append(rock(token.lower(), x, y))
            elif token == 'p':
                self.token_list.append(paper(token.lower(), x, y))
            elif token == 's':
                self.token_list.append(scissors(token.lower(), x, y))

class Block(Player):
    
    token_list = []

    def __init__(self, token_data):
        
        self.name = 'block'
        for token, x, y in token_data:
            self.token_list.append(block("\"\"", x, y))

