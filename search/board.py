import math
from search.player import Upper, Lower, Non_player

class Board():

    # generate token classes of players 
    # with their coordinates and block tokens
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
    # updates surviving tokens of Upper & Lower class after battle
    # and update board Upper and Lower classes
    def battle(self, coord_dict):

        paper_die = False
        scissor_die = False
        rock_die = False
        
        alive_tokens = dict()

        self.upper.clear_token_list()
        self.lower.clear_token_list()

        # decide what token dies
        for coord, tokens in coord_dict.items():
            if len(tokens) > 1:
                for token in list(tokens):
                    ttype = token.lower()
                    if ttype == 'p':
                        rock_die = True
                    elif ttype == 'r':
                        scissor_die = True
                    elif ttype == 's':
                        paper_die = True

                # create list of surviving tokens
                for token in list(tokens):
                    ttype = token.lower()
                    if (ttype == 'p' and paper_die == False) or \
                        (ttype == 'r' and rock_die == False) or \
                        (ttype == 's' and scissor_die == False):
                        if coord not in alive_tokens:
                            alive_tokens[coord] = [token]
                        else:
                            alive_tokens[coord].append(token)
            
            # single token or tokens of same type on a hex tile
            else:
                if coord not in alive_tokens:
                    alive_tokens[coord] = [tokens]
                else:
                    alive_tokens[coord].append(token)

        # re-insert surviving tokens into player classes
        for (x, y), tokens in alive_tokens.items():
            for token in tokens:
                if token.isalpha() and token.isupper():
                    self.upper = Upper([[token.lower(), x ,y]])
                elif token.isalpha() and token.islower():
                    self.lower = Lower([[token, x ,y]])
        
        return alive_tokens



    # sets the tokens as the keys, with the coordinates as values
    def swap_dict(self, coord_dict):
        token_first_dict = {}

        for coord in coord_dict.keys():
            for token in coord_dict[coord]:
                
                # check if it's been listed before
                if token not in token_first_dict:
                    token_first_dict[token] = [coord]
                else:
                    token_first_dict[token].append(coord) 
        
        return token_first_dict

    # select a target for each of Upper's tokens
    # do a pairwise search for each Upper token vs each Lower enemy
    # pick the shortest distance target for each
    # {(0,0): "rfs"}
    def target(self, coord_dict):

        # create token-focused dictionary so target locations can be looked up
        token_first = swap_dict(coord_dict)    

        for token in token_first:
            if token.isupper() and token == 'R': # repeat for each 'R' 'P' 'S'
                prey = token_first['s']
                target_pieces = pick_shortest(token_first[token], prey) # how to assign?


                # at this point, there are two lists, where the first is a list of coordinates where the instances of the Upper
                # token can be found, and the second is target_pieces, containing target coordinates in order of the matching Upper tokens
                # e.g. 'R' : [(0,0), (2,3)]
                #      's' : [(0,1), (1,2)] 
                # how can we "assign" the coordinates to the instances of the Upper tokens? 
                



        return 0


    # win when no lower tokens left
    def win(self):
        return not bool(self.lower)

    # calculate direct line distance between two tokens
    def calc_distance(self, token1, token2):
        (x1, y1) = token1
        (x2, y2) = token2
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return dist

    # conducts a pairwise search between lists of coordinates, and returns 
    # the shortest targeted Lower coordinates(in order)
    def pick_shortest(self, uppers, lowers):
        targets = []

        for upCoord in uppers:    
            # longest possible distance is 8 units
            shortest = 8
            best_target = 0

            for lowCoord in lowers:
                dist = calc_distance(upCoord, lowCoord) 
                if dist < shortest:
                    shortest = dist
                    best_target = lowCoord
            
            # remove targeted coord so it isn't targeted again
            targets.append(best_target)
            lowers.remove(best_target)

        return targets

        
        
            

