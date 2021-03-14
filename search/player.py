import search.board
from search.token import Token, Rock, Paper, Scissors, Block

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

    def play(self, board):
    
        blocks = [block.coord for block in board.block.token_list]

        # play each token
        for token in self.token_list:
            if not token.target:
                # get new target (to be improved)
                for enemy in board.lower.token_list:
                    if isinstance(enemy, token.enemy):
                        token.target = enemy
            else:
                # move to target (WIP)
                print()
            moves = (token.get_adj_hex(board.upper.token_list, blocks, board))

        return board
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


