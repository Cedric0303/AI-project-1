from search.token import Upper, Lower, Block

class Board():

    def __init__(self, token_data):
        self.board_dict = Board.create_board_dict(token_data)

    # default size of board
    size = range(-4, +4+1)

    # generate dict of tokens with their coordinates
    def create_board_dict(data):
        board_dict = dict()
        for s, r, q in data['upper']:
            board_dict[r, q] = Upper(s, r, q)
        for s, r, q in data['lower']:
            board_dict[r, q] = Lower(s, r, q)
        for s, r, q in data['block']:
            board_dict[r, q] = Block(r, q)
        return board_dict

    # create dict from token dict to work with print_board function
    def print_dict(self):
        output_dict = dict()
        for each in self.board_dict:
            output_dict[each] = self.board_dict[each].get_name()
        return output_dict