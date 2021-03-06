import collections
import search.board
import sys
from search.token import Token, Rock, Paper, Scissors, Block

class Player():

    token_list = list()

    def clear_token_list(self):
        self.token_list.clear()

    # return the enemy token nearest to the supplied Upper token
    def pick_nearest(self, token, lowers):
        nearest = sys.maxsize
        best_target = False
        for target in lowers.token_list:
            if isinstance(target, token.enemy):
                distance = token.calc_distance(token.coord, target.coord)
                if distance < nearest:
                    nearest = distance
                    best_target = target
        return best_target

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

    # generate path using BFS
    # adapted & modified from Stack Overflow, authored by tobias_k
    # https://stackoverflow.com/a/47902476
    def get_path(token, blocks, enemies, token_list):
        queue = collections.deque([[token.coord]])
        seen = set([token.coord])
        other_enemies = set(enemies)
        other_enemies.remove(token.target.coord)

        while queue:
            path = queue.popleft()
            x, y = path[-1]
            if (x, y) == token.target.coord:
                path.pop(0)
                return path
            temp_list = Token.get_adj_hex((x,y))
            for coord in [each.coord for each in token_list]:
                immediate_adj = Token.get_adj_hex((token.coord))
                if coord in immediate_adj and coord in temp_list:
                    temp_list.remove(coord)
                    adjacent = Token.get_adj_hex(coord)
                    for (x3, y3) in adjacent:
                        temp_list.append((x3, y3))
            for (x2, y2) in temp_list:
                if search.board.Board.check_bounds(x2, y2) and \
                (x2, y2) not in blocks and (x2, y2) not in seen and \
                (x2, y2) not in other_enemies:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
        return False

    # carry out moves for Upper player each turn
    def play(self, board):
        blocks = [block.coord for block in board.block.token_list]
        enemies = [enemy.coord for enemy in board.lower.token_list]
        targetless = list()
        move_array = list()
        targeted = list()

        # play each token
        for token in self.token_list:
            if not token.target:
                # get new target
                target = self.pick_nearest(token, board.lower)
                if target not in targeted:
                    token.set_target(target)
                    targeted.append(target)
                # do nothing if no target available
                if not token.target:
                    targetless.append(token)
                    continue
                # generate new path to target
                if token.target and not token.path:
                    token.path = Upper.get_path(token, blocks, enemies,
                                board.upper.token_list)
                    if not token.path:
                        targetless.append(token)
                        continue
                    else:
                        move_array.append(token.initialize_move())
            else:
                move_array.append(token.initialize_move())

        # generate valid move for targetless tokens
        for token in targetless:
            unavailable = [move.next_move for move in move_array]
            moves = list()
            adjacent = Token.get_adj_hex((token.coord))
            for (x, y) in adjacent:
                if search.board.Board.check_bounds(x, y) and \
                (x, y) not in blocks and (x, y) not in enemies and \
                (x, y) not in unavailable:
                    moves.append((x, y))
            token.path = [moves[0]]
            move_array.append(token.initialize_move())
       
        # change paths for tokens moving onto same hex
        move_array.sort(key=Token.nearest_distance)
        moved_hex = list()
        moved = list()
        for token in move_array:
            if token.next_move not in moved_hex:
                moved.append(token.initialize_move())
                moved_hex.append(token.next_move)
            else:
                blocks_and_moved = set(blocks) ^ set(moved_hex)
                token.path = Upper.get_path(token, blocks_and_moved, 
                            enemies,board.upper.token_list)
                moved.append(token.initialize_move())
                moved_hex.append(token.next_move)

        # move tokens toward targets
        for token in moved:
            token.move(token.next_move, board)


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




