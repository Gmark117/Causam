import numpy as np
import os
import time
import random

WHITE_PIECES        = 11
BLACK_PIECES        = 12

class Game:
    def __init__(self, player1, player2):
        ''' Initializes the game with the players, and the board'''
        self.p1 = player1
        self.p2 = player2
    
    def play(self):
        '''Starts the game'''
        pass

class Board:
    def __init__(self):
        ''' Initializes the board through nodes, edges and pieces'''
        self.nodes = self.populate_nodes()
        self.edges = self.populate_edges()
        self.w_setup, self.b_setup = self.board_setup()
        self.pieces = Pieces()
    
    def populate_nodes(self):
        ''' Populates the board with nodes taken from the Nodes.txt datafile'''
        nodes_list = []
        with open("Nodes.txt") as fnodes:
            # Reads header
            fnodes.readline()
            # Reads and Adds nodes to the list
            node = fnodes.read(3)
            nodes_list.append(node)
            while fnodes.read(1) != '#':
                node = fnodes.read(3)
                nodes_list.append(node)
        print('# {} Nodes Initialized...'.format(len(nodes_list)))
        print(nodes_list)
        return nodes_list

    def populate_edges(self):
        ''' Populates the board with edges taken from the Edges.txt datafile'''
        edges_list = []
        with open("Edges.txt") as fedges:
            # Reads header
            fedges.readline()
            # Reads and Adds edges to the list
            node1 = fedges.read(3)
            while node1 != '--#':
                if node1 == '---':
                    # If they are a breakline, it goes to the next line and
                    # reads another 3 characters (They WILL be a node)
                    fedges.read(1)
                    node1 = fedges.read(3)
                fedges.read(3)          # Reads the arrow
                while fedges.read(1) == ' ':
                    # Reads the second edge component and adds the pair
                    node2 = fedges.read(3)
                    edges_list.append([node1,node2])
                node1 = fedges.read(3)  # First 3 characters of the next line
        print('# {} Edges Initialized...'.format(len(edges_list)))
        print(edges_list)
        return edges_list
    
    def board_setup(self):
        ''' Reads the board setup of the pieces from the BoardSetup.txt datafile'''
        w_setup = []
        b_setup = []
        with open("BoardSetup.txt") as fsetup:
            # Reads header
            fsetup.readline()
            w_node = fsetup.read(3)
            w_setup.append(w_node)
            while fsetup.read(1) != '\n':
                w_node = fsetup.read(3)
                w_setup.append(w_node)
            b_node = fsetup.read(3)
            b_setup.append(b_node)
            while fsetup.read(1) != '#':
                b_node = fsetup.read(3)
                b_setup.append(b_node)
        print('# {} Starting Positions Initialized...'.format(len(w_setup)+len(b_setup)))
        print('White Positions:\n{}'.format(w_setup))
        print('Black Positions:\n{}'.format(b_setup))
        return w_setup, b_setup

class Piece:
    def __init__(self, id='', goal=None):
        ''' Creates a piece'''
        self.id = id
        self.goal = goal
    
    def set_id(self, id):
        ''' Sets piece ID'''
        self.id = id
    
    def set_goal(self, goal):
        ''' Sets which, if any, goal is reached'''
        self.goal = goal

class Pieces:
    def __init__(self):
        ''' Initializes a set of pieces'''
        self.w_pieces, self.b_pieces = self.populate_pieces()
    
    def populate_pieces(self):
        ''' Initializes a set of pieces for each player'''
        w_pieces = []
        b_pieces = []
        for i in range(WHITE_PIECES):
            # Creates white pieces
            if i+1 <= 9:
                w_pieces.append(Piece('W0{}'.format(i+1)))
            else:
                w_pieces.append(Piece('W{}'.format(i+1)))
        for i in range(BLACK_PIECES):
            # Creates black pieces
            if i+1 <= 9:
                b_pieces.append(Piece('B0{}'.format(i+1)))
            else:
                b_pieces.append(Piece('B{}'.format(i+1)))
        print('# {} Pieces Initialized'.format(len(w_pieces)+len(b_pieces)))
        print('White Pieces:')
        for i in range(WHITE_PIECES):
            print(w_pieces[i].id)
        print('Black Pieces:')
        for i in range(BLACK_PIECES):
            print(b_pieces[i].id)

        return w_pieces, b_pieces

if __name__=='__main__':
    board = Board()