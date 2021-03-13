from search.player import Upper, Lower, Block
from search.token import Token, rock, paper, scissors, block

class Board():

    # generate token classes of players 
    # with their coordinates and block tokens
    # does not allow for overlaps!!
    def __init__(self, token_data):
        
        self.upper = Upper(token_data['upper'])
        self.lower = Lower(token_data['lower'])
        self.block = Block(token_data['block'])
        
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
    def battle(self, cord_dict):
        
        p_count = r_count = s_count = 0
        paper_die = scissor_die = rock_die = False
        
        # count frequency of tokens
        for coord, token in cord_dict:
            if isinstance(token, paper):
                p_count += 1
            elif isinstance(token, rock):
                r_count += 1
            elif isinstance(token, scissors):
                s_count += 1

        # check battling types
        paper_die = bool(s_count)
        scissor_die = bool(r_count)
        rock_die = bool(p_count)

        # check battling types
        #if s_count >= 1:
        #    paper_die = True
        #if r_count >= 1:
        #    scissor_die = True
        #if p_count >= 1:
        #    rock_die = True
        
        #self.upper.clear_token_list()
        #self.lower.clear_token_list()
        alive_tokens = dict()
        for coord, token in cord_dict:
            if (isinstance(token, paper) and paper_die == False) or \
                (isinstance(token, rock) and rock_die == False) or \
                (isinstance(token, scissors) and scissor_die == False):
                if coord not in alive_tokens:
                    alive_tokens[coord] = token.name
                else:
                    alive_tokens[coord] += token.name

        return alive_tokens 