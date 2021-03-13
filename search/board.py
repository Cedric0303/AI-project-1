from search.token import Upper, Lower, Block

class Board():

    def __init__(self, token_data):
        self.board_dict = Board.create_board_dict(token_data)

    # default size of board
    size = range(-4, +4+1)

    # generate dict of tokens with their coordinates
    # does not allow for overlaps!!
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

    # set up fighting mechanic, where it takes a list of all tokens on this coord
    # and returns the list of still-alive tokens after the battle
    def battle(self, all_tokens):
        p_count = 0
        r_count = 0
        s_count = 0

        paper_die = False
        scissor_die = False
        rock_die = False
        
        # count frequency of tokens
        for token in all_tokens:
            ttype = token.get_name().lower()
            if ttype == 'p':
                p_count += 1
            elif ttype == 'r':
                r_count += 1
            elif ttype == 's':
                s_count += 1

        # check battling types
        if s_count >= 1:
            paper_die = True
        if r_count >= 1:
            scissor_die = True
        if p_count >= 1:
            rock_die = True

        alive_tokens = []
        for token in all_tokens:
            ttype = token.get_name().lower()
            if (ttype == 'p' and paper_die == False) or \
            (ttype == 'r' and rock_die == False) or \
            (ttype == 's' and scissor_die == False):
                alive_tokens.append(token)

        return alive_tokens 