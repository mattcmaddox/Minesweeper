#! /usr/bin/python

import random
import argparse
from random import randint

def build_parser():
    parser = argparse.ArgumentParser(description='Command Line Implementation of Minesweeper', add_help=True)
    parser.add_argument('-r', '--rows', type=int, default=8, help='Number of Rows')
    parser.add_argument('-c', '--columns', type=int, default=9, help='Number of Columns')
    parser.add_argument('-m', '--mines', type=int, default=None, help='Number of Mines')
    parser.add_argument('rows', type=int, nargs='?', default=8, help='Positional Argument for Number of Rows')
    parser.add_argument('columns', type=int, nargs='?', default=9, help='Positional Argument for Number of Columns')
    parser.add_argument('mines', type=int, nargs='?', default=None, help='Positional Argument for Number of Mines')
    args = vars(parser.parse_args())
    return args
args = build_parser()
rows = args['rows']
columns = args['columns']
mines = args['mines']


# CLASSY!
class block(object):
    """An instance of a positional block on the grid"""
    def __init__(self, 0, False, False, False):
        #self.number = number
        #self.revealed = revealed
        #self.mine = mine
        #self.flagged = flagged

    def __repr__(self):
        """Returns a string representation of the block object"""
        #return '%s %s %s %s' % (self.number, self.revealed, self.mine, self.flagged)
        return '%s' % (self.number)

    # put block attributes here instead of __init__?
    def show_number(self):
        print self.number
    def show_revealed(self):
        print self.revealed


# Builds Minefield Grid
grid = [[block(0, False, False, False) for x in range(rows)] for y in range(columns)]

def gather_mines(rows, columns, mines):
    if mines == None:
        mines = int(rows * columns / 6.4)
        return mines
    else:
        return mines


print gather_mines(rows, columns, mines)
print mines
print grid



def main():
    """A CLI of Minesweeper
    $Minesweeper.py [rows] [columns]
    """

        


