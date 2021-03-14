"""
COMP30024 Artificial Intelligence, Semester 1, 2021
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

import sys
import json

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from search.util import print_board, print_slide, print_swing
from search.board import Board

def main():

    try:
        with open(sys.argv[1]) as file:
            token_data = json.load(file)
            board = Board(token_data)
            board_dict = board.create_dict()
            print_board(board_dict, compact=True)
            while not board.win(): # WIP
                board.battle(board_dict)
                board = board.upper.play(board)
                break

    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)

    # TODO:
    # Find and print a solution to the board configuration described
    # by `data`.
    # Why not start by trying to print this configuration out using the
    # `print_board` helper function? (See the `util.py` source code for
    # usage information).
