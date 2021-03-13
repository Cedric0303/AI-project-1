import search.board

class Token():

    def __init__(self, name, x, y):
        self.name = name
        self.coord = x, y

    # generate list of adjacent hex tiles of current_hex hex tile
    #  including swings and blocks
    def get_adjacent_hex(self, board_dict):
        adjacent_hex_list = []
        (x, y) = self.coord
        temp_list = [(x, y-1), (x-1, y), 
                    (x+1, y), (x, y+1), 
                    (x-1, y+1), (x+1, y-1)]
        for (each_x, each_y) in temp_list:
            if each_x in search.board.Board.size and \
            each_y in search.board.Board.size:
                adjacent_hex_list.append((each_x, each_y))
        
        # add swing tiles to adjacent hex tiles list if swing is possible
        valid_swing_tiles=[]
        for each_adj in adjacent_hex_list:
            if each_adj in board_dict and \
                board_dict[each_adj].get_name().isalpha() and \
                board_dict[each_adj].get_name().isupper():
                valid_swing_tiles.append(each_adj)
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
    
    def get_name(self):
        return self.name

class Upper(Token):

    def __init__(self, name, x, y):
        super().__init__(name.upper(), x, y)

    pass

class Lower(Token):

    def __init__(self, name, x, y):
        super().__init__(name.lower(), x, y)

    pass

class Block(Token):

    def __init__(self, x, y):
        super().__init__("\"\"", x, y)

    pass