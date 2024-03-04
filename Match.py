import pygame
import Assets

class Match():
    def __init__(self, game):
        self.game = game

        self.green_piece = pygame.image.load(Assets.Images['GREEN_STONE'].value)
        self.green_piece = pygame.transform.scale(self.green_piece, (100,100))
        self.blue_piece = pygame.image.load(Assets.Images['BLUE_STONE'].value)
        self.blue_piece = pygame.transform.scale(self.blue_piece, (100,100))
        self.hblue_piece = pygame.image.load(Assets.Images['H_BLUE_STONE'].value)
        self.hblue_piece = pygame.transform.scale(self.hblue_piece, (100,100))

        self.game.to_maximised()

        self.run_display = True
        while self.run_display:
            self.display_board()

    def display_board(self):
        # Check for inputs
        self.game.check_events()
        #####
        #   CODE FOR HANDLING INPUTS
        #####

        # Set background
        self.game.display.blit(self.game.curr_menu.board, (0,0))

        self.draw_pieces(self.green_piece, Assets.greens_x, Assets.greens_y)
        self.draw_pieces(self.blue_piece, Assets.blues_x, Assets.blues_y)
        self.draw_pieces(self.hblue_piece, Assets.h_blue_x, Assets.h_blue_y)

        self.game.blit_screen()

    def draw_pieces(self, img, x, y):
        for i in range(len(x)):
            self.game.display.blit(img, (x[i]-50,y[i]-50))
