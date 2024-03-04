from mimetypes import init
import numpy as np
import os
import random
import time


WHITE_PIECES        = 11
BLACK_PIECES        = 11
SPECIAL_BLACK_PIECE = 1
LEVELS              = 11
MAX_NODES           = 11
POSITIONS           = 84
WHITE_GOALS         = 5
BLACK_GOALS         = 6

COLOUR = ['Black', 'White'] # [0, 1]
SPECIAL = ['No', 'Yes']     # [0, 1]

class Board:
    def __init__(self):
        self.whites         = []
        self.blacks         = []
        self.special_balck  = []
        self.white_goals    = []
        self.black_goals    = []

        self.grid = self.create_grid()

        for i in range(WHITE_GOALS):
            self.white_goals.append(Goal(1, i+1))
        for i in range(BLACK_GOALS):
            self.black_goals.append(Goal(0, i+1))

        for i in range(WHITE_PIECES):
            self.whites.append(self.add_piece(1, i+1))
        for i in range(BLACK_PIECES):
            self.blacks.append(self.add_piece(0, i+1))
        for i in range(SPECIAL_BLACK_PIECE):
            self.special_balck.append(self.add_piece(0, i+1, 1))

    def create_grid(self):
        grid = []
        
        # 1st Level
        tmp = Position()
        tmp.set_position(1,1)
        grid.append([tmp])
        
        # 2nd Level
        tmp = []
        for i in range(6):
            tmp_pos = Position()
            tmp_pos.set_position(2,i+1)
            tmp.append(tmp_pos)
        grid.append(tmp)
        
        # 3rd to 11th Levels
        level = 3
        nodes = 11
        for i in range(LEVELS):
            if nodes>MAX_NODES: break
            tmp = []
            for k in range(nodes):
                tmp_pos = Position()
                tmp_pos.set_position(level,k+1)
                tmp.append(tmp_pos)
            level += 1
            if level<=7:
                nodes -= 1 
            else:
                nodes += 1
            grid.append(tmp)

        return grid
    
    def add_piece(self, colour, number, special=0):
        return Piece(colour, number, special)
    
    def print_board(self):
        print('\n\n###### WHITE PIECES ######')
        for i in range(len(self.whites)):
            self.whites[i].print_piece()
        print('\n\n###### BLACK PIECES ######')
        for i in range(len(self.special_balck)):
            self.special_balck[i].print_piece()
        for i in range(len(self.blacks)):
            self.blacks[i].print_piece()
        print('\n\n#######################\n#######################')
        print('\n\n###### WHITE GOALS ######')
        for i in range(len(self.white_goals)):
            self.white_goals[i].print_goal()
        print('\n\n###### BLACK GOALS ######')
        for i in range(len(self.black_goals)):
            self.black_goals[i].print_goal()
    
    def print_grid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j].print_position()

class Piece:
    def __init__(self, colour, number, special=0):
        if colour:
            assert number <= WHITE_PIECES
            self.new_piece(colour, number, special)
        else:
            if special:
                assert number <= SPECIAL_BLACK_PIECE
                self.new_piece(colour, number, special)
            else:
                assert number <= BLACK_PIECES
                self.new_piece(colour, number+1, special)
    
    def new_piece(self, colour, number, special=0):
        self.colour = colour
        self.piece_id = number
        self.special = special
        self.position = Position(colour, number, special)
    
    def movement(self):
        pass
    
    def effect(self):
        pass
    
    def print_piece(self):
        print('\nColour: {}'.format(COLOUR[self.colour]))
        print('Piece ID: {}'.format(self.piece_id))
        print('Special: {}'.format(SPECIAL[self.special]))
        print('Position:')
        self.position.print_position()

class Position:
    def __init__(self, colour=0, number=0, special=False, goal=False):
        self.level = 0
        self.node = 0
        if colour==0 | number==0:
            return

        if goal:
            self.set_goal_node(colour, number)
            return
        self.set_piece_node(colour, number, special)
    
    def set_position(self, level, node):
        self.level = level
        self.node = node
    
    def set_piece_node(self, colour, number, special):
        if colour:
            if number==1:
                self.level = 1
                self.node = number
            elif number<=5:
                self.level = 2
                self.node = number
            else:
                self.level = 3
                self.node = 2*number - 11
        else:
            if number<=3:
                self.level = 7
                if special:
                    self.node = 4
                    return
                self.node = 2*number - 1
            elif number<=7:
                self.level = 8
                self.node = number - 1
            else:
                self.level = 9
                self.node = number - 5
    
    def update_piece_node(self):
        pass
    
    def set_goal_node(self, colour, number):
        self.level = 11
        if colour:
            self.node = 2*number
        else:
            self.node = 2*number - 1
    
    def print_position(self):
        print('\tLevel: {}'.format(self.level))
        print('\tNode: {}'.format(self.node))

class Goal:
    def __init__(self, colour, number):
        self.full = False
        self.goal_id = number
        self.position = Position(colour, number, goal=True)
    
    def print_goal(self):
        print('\nGoal ID: {}'.format(self.goal_id))
        print('Position:')
        self.position.print_position()
        print('Status: FULL') if self.full else print('Status: EMPTY')

class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
    
    def play(self):
        pass

if __name__=='__main__':
    board = Board()
    board.print_board()
    board.print_grid()
    game = Game(board, 'Gianmarco', 'Aya')
    game.play()
