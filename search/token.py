import search.board
import search.player

class Token():

    def __init__(self, name, x, y):
        
        self.name = name
        self.coord = x, y
        self.target = False

    # generate list of adjacent hex tiles of current hex tile
    # including swings and blocks
    def get_adj_hex(self, token_list, block_list, board):
        
        token_dict = {token.coord: token.name for token in token_list}
        temp_adj_list = list()
        (x, y) = self.coord
        temp_list = [(x, y-1), (x-1, y), 
                    (x+1, y), (x, y+1), 
                    (x-1, y+1), (x+1, y-1)]
        for (each_x, each_y) in temp_list:
            if each_x in board.size and each_y in board.size:
                temp_adj_list.append((each_x, each_y))
        
        # find adjacent swing tiles
        valid_swing_tiles = list()
        for each_adj in temp_adj_list:
            if each_adj in token_dict and \
            token_dict[each_adj].isalpha() and \
            token_dict[each_adj].isupper():
                valid_swing_tiles.append(each_adj)

        # add swing tiles to adjacent hex tiles list if swing move is legal
        for (x, y) in valid_swing_tiles:
            temp_list = [(x, y-1), (x-1, y), 
                        (x+1, y), (x, y+1), 
                        (x-1, y+1), (x+1, y-1)]
            for (each_x, each_y) in temp_list:
                if each_x in board.size and each_y in board.size and \
                (each_x, each_y) != self.coord and \
                (each_x, each_y) not in temp_adj_list:
                    temp_adj_list.append((each_x, each_y))        
        
        # remove block tiles from adjacency list
        final_adj_list = list(set(temp_adj_list) ^ set(block_list))
        
        return final_adj_list

    def move(self, coord):
        
        self.coord = coord

    def set_target(self, target):
        self.target = target

class Rock(Token):

    def __init__(self, name, x, y):

        self.enemy = Scissors
        super().__init__(name, x, y)

class Paper(Token):

    def __init__(self, name, x, y):

        self.enemy = Rock
        super().__init__(name, x, y)

class Scissors(Token):

    def __init__(self, name, x, y):

        self.enemy = Paper
        super().__init__(name, x, y)

class Block(Token):
    
    pass