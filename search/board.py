# default size of board
size = range(-4, +4+1)

# generate dictionary of tokens and blocks with their coordinates
def create_token_dict(data):
    token_dict = dict()
    for s, r, q in data['upper']:
        token_dict[r, q] = s.upper()
    for s, r, q in data['lower']:
        token_dict[r, q] = s.lower()
    for s, r, q in data['block']:
        token_dict[r, q] = "\"\""
    return token_dict

# generate dictionary of all hex coordinates along with entries and blocks
def generate_board(token_dict):
    board_dict = dict()
    for rq in [(r,q) for r in size for q in size if -r-q in size]:
        if rq in token_dict:
            board_dict[rq] = token_dict[rq]
        else:
            board_dict[rq] = " "
    return board_dict

# generate list of adjacent hex including swings and blocks
def get_adjacent_hex(hex, board_dict):
    adjacent_hex_list = []
    (x, y) = hex
    temp_list = [(x, y-1), (x-1, y), 
                (x+1, y), (x, y+1), 
                (x-1, y+1), (x+1, y-1)]
    for (each_x, each_y) in temp_list:
        if each_x in size and each_y in size:
            adjacent_hex_list.append((each_x, each_y))
    # swing
    valid_swing_tiles=[]
    for each_adj in adjacent_hex_list:
        if each_adj in board_dict and \
            board_dict[each_adj].isalpha() and \
            board_dict[each_adj].isupper():
            valid_swing_tiles.append(each_adj)
    for (x, y) in valid_swing_tiles:
        temp_list = [(x, y-1), (x-1, y), 
                    (x+1, y), (x, y+1), 
                    (x-1, y+1), (x+1, y-1)]
        for (each_x, each_y) in temp_list:
            if each_x in size and each_y in size and \
            (each_x, each_y) != hex and \
            (each_x, each_y) not in adjacent_hex_list:
                adjacent_hex_list.append((each_x, each_y))

    return adjacent_hex_list

def get_distance(hex, target):
    
    return