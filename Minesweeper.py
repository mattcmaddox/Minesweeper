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
    def __init__(self):
        self.number = 0
        self.revealed = False
        self.mine = False
        self.flagged = False
    
    def __repr__(self):
        """Returns a string representation of the block object"""
        #return '%s %s %s %s' % (self.number, self.revealed, self.mine, self.flagged)
        #return '%s' % (self.number)
        return '%s' % (self.mine)

    def show(self):
        print self.number, self.revealed, self.mine, self.flagged
    def mine_maker(self):
        self.mine = True
        return self.mine


# Builds Minefield Grid
grid = [[block() for y in range(columns)] for x in range(rows)]

# Sets number of mines appropriate for grid size
def gather_mines(rows, columns, mines):
    if mines == None:
        mines = int(rows * columns / 6.4)
        return mines
    else:
        return mines

def mine_layer(rows, columns, mines):
    while mines != 0:
        random_block = grid[randint(0, (rows - 1))][randint(0, (columns - 1))]
        if random_block.mine == False:
            random_block.mine_maker()
            mines -= 1
        elif random_block.mine == True:
            print "tried to lay mine in same place"
        else:
            print "Something went wrong!", random_block
            return
    return


mines = gather_mines(rows, columns, mines)
print mines
mine_layer(rows, columns, mines)
print grid
#print "stuff", grid[randint(0, (rows - 1))][randint(0, (columns - 1))]


def main():
    """A CLI of Minesweeper
    $Minesweeper.py [rows] [columns]
    """

        


