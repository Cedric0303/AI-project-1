import math
import search.board
from search.token import Token, Rock, Paper, Scissors, Block

class Player():

    token_list = list()

    def clear_token_list(self):
        
        self.token_list.clear()

    # return the enemy token nearest to the supplied Upper token
    def pick_nearest(self, token, lowers):
        nearest = 10 # arbitrary greater than 8
        best_target = False
        for target in lowers.token_list:
            if isinstance(target, token.enemy):
                distance = token.calc_distance(token.coord, target.coord)
                if distance < nearest:
                    nearest = distance
                    best_target = target
        return best_target

    # carry out search to find best path/ best move
    def best_valid_move(self, moves, token):
        nearest = 10
        best_move = False
        for move in moves:
            distance = token.calc_distance(move, token.target.coord)
            if distance < nearest:
                nearest = distance
                best_move = move
        return best_move

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
    
    # carry out the moves for the Upper player each turn
    def play(self, board):
        
        blocks = [block.coord for block in board.block.token_list]

        # play each token
        for token in self.token_list:
            if not token.target:
                # get new target
                token.target = self.pick_nearest(token, board.lower)
                # move to target (WIP)
            if token.target:
                moves = (token.get_adj_hex(board.upper.token_list, 
                                            blocks, board))
                check_move = self.best_valid_move(moves, token)
                if check_move != False:
                    token.move(check_move, board)

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




