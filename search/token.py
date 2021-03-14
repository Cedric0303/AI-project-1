import search.board

class Token():

    def __init__(self, name, x, y):
        
        self.name = name
        self.coord = x, y

    # generate list of adjacent hex tiles of current hex tile
    # including swings and blocks
    def get_adjacent_hex(self, token_list):
        
        token_dict = {token.coord: token.name for token in token_list}
        adjacent_hex_list = list()
        (x, y) = self.coord
        temp_list = [(x, y-1), (x-1, y), 
                    (x+1, y), (x, y+1), 
                    (x-1, y+1), (x+1, y-1)]
        for (each_x, each_y) in temp_list:
            if each_x in search.board.Board.size and \
            each_y in search.board.Board.size:
                adjacent_hex_list.append((each_x, each_y))
        
        # find adjacent swing tiles
        valid_swing_tiles=[]
        for each_adj in adjacent_hex_list:
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
                if each_x in search.board.Board.size and \
                each_y in search.board.Board.size and \
                (each_x, each_y) != self.coord and \
                (each_x, each_y) not in adjacent_hex_list:
                    adjacent_hex_list.append((each_x, each_y))         
        return adjacent_hex_list

class Rock(Token):
    
    pass

class Paper(Token):
    
    pass

class Scissors(Token):
    
    pass

class Block(Token):
    
    pass