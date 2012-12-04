#! /usr/bin/python

import random
import argparse
from random import randint

def build_parser():
    parser = argparse.ArgumentParser(description='Command Line Implementation of Minesweeper', add_help=True)
    parser.add_argument('-r', '--rows', type=int, default=2, help='Number of Rows')
    parser.add_argument('-c', '--columns', type=int, default=4, help='Number of Columns')
    parser.add_argument('rows', type=int, nargs='?', default=2, help='Positional Argument for Number of Rows')
    parser.add_argument('columns', type=int, nargs='?', default=4, help='Positional Argument for Number of columns')
    args = vars(parser.parse_args())
    return args
args = build_parser()

class block(object):
    """An instance of a positional block on the grid"""
    def __init__(self, number, revealed, mine, flagged):
        self.number = number
        self.revealed = revealed
        self.mine = mine
        self.flagged = flagged
    def __repr__(self):
        """Returns a string representation of the block object"""
        return '%s %s %s %s' % (self.number, self.revealed, self.mine, self.flagged)

    def add_mine(self):
        pass
    def add_flag(self):
        pass
    def show_number(self):
        print self.number
    def show_revealed(self):
        print self.revealed


grid = [[block(0, False, False, False) for y in range(args['rows'])] for x in range(args['columns'])]
print grid
def main():
    """A CLI of Minesweeper
    $Minesweeper.py [rows] [columns]
    """

        


