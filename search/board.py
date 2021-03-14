from search.player import Upper, Lower, Non_player
from search.token import Token, Rock, Paper, Scissors, Block

class Board():

    # generate token classes of players 
    # with their coordinates and block tokens
    # does not allow for overlaps!!
    def __init__(self, token_data):
        
        self.upper = Upper(token_data['upper'])
        self.lower = Lower(token_data['lower'])
        self.block = Non_player(token_data['block'])
        
    # default size of board
    size = range(-4, +4+1)

    # create dict of tokens on occupied hex tiles
    # from tokens of player classes
    def create_dict(self):
        
        output_dict = dict()
        for each in self.upper.token_list + \
                    self.lower.token_list + \
                    self.block.token_list:
            if each.coord not in output_dict:
                output_dict[each.coord] = each.name
            else:
                output_dict[each.coord] += each.name
        return output_dict


    # set up fighting mechanic, 
    # where it takes a dict of all tokens on all coords, 
    # returns the dict of still-alive tokens after the battle
    # and update board Upper and Lower classes
    def battle(self, coord_dict):

        paper_die = False
        scissor_die = False
        Rock_die = False
        
        alive_tokens = dict()

        self.upper.clear_token_list()
        self.lower.clear_token_list()

        # count frequency of tokens
        for coord, tokens in coord_dict.items():
            if len(tokens) > 1:
                for token in list(tokens):
                    ttype = token.lower()
                    if ttype == 'p':
                        Rock_die = True
                    elif ttype == 'r':
                        scissor_die = True
                    elif ttype == 's':
                        paper_die = True

                for token in list(tokens):
                    ttype = token.lower()
                    if (ttype == 'p' and paper_die == False) or \
                        (ttype == 'r' and Rock_die == False) or \
                        (ttype == 's' and scissor_die == False):
                        if coord not in alive_tokens:
                            alive_tokens[coord] = [token]
                        else:
                            alive_tokens[coord].append(token)
            else:
                if coord not in alive_tokens:
                    alive_tokens[coord] = [tokens]
                else:
                    alive_tokens[coord].append(token)
        
        temp_upper_list = list()
        temp_lower_list = list()
        for (x, y), tokens in alive_tokens.items():
            if len(tokens) > 1:
                for token in tokens:
                    if token.isalpha() and token.isupper():
                        temp_upper_list.append([token.lower(), x ,y])
                    elif token.isalpha() and token.islower():
                        temp_lower_list.append([token, x ,y])
            else:
                if tokens[0].isalpha() and tokens[0].isupper():
                    temp_upper_list.append([tokens[0].lower(), x ,y])
                elif tokens[0].isalpha() and tokens[0].islower():
                    temp_lower_list.append([tokens[0], x ,y])
        
        self.upper = Upper(temp_upper_list)
        self.lower = Lower(temp_lower_list)
        return alive_tokens 