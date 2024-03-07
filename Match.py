import pygame
import Assets
from Stone import Stone
from SelRing import SelRing
from Node import Node

class Match():
    def __init__(self, game):
        self.game = game

        self.n_stones = 11
        self.generate_sprites()

        self.game.to_maximised()

        self.game_on = True
        while self.game_on:
            self.display_board()
            self.check_inputs()

    def generate_sprites(self):
        img_dim = Assets.IMAGE_DIM

        self.green_img = pygame.image.load(Assets.Images['GREEN_STONE'].value)
        self.green_img = pygame.transform.scale(self.green_img, (img_dim,img_dim))
        self.blue_img  = pygame.image.load(Assets.Images['BLUE_STONE'].value)
        self.blue_img  = pygame.transform.scale(self.blue_img, (img_dim,img_dim))
        self.hblue_img = pygame.image.load(Assets.Images['H_BLUE_STONE'].value)
        self.hblue_img = pygame.transform.scale(self.hblue_img, (img_dim,img_dim))

        self.ring_img = pygame.image.load(Assets.Images['SELECT_RING'].value)
        self.ring_img = pygame.transform.scale(self.ring_img, (img_dim,img_dim))
        self.node_img = pygame.image.load(Assets.Images['NEXT_NODE'].value)
        self.node_img = pygame.transform.scale(self.node_img, (img_dim,img_dim))

        self.g_stones = pygame.sprite.RenderUpdates()
        self.b_stones = pygame.sprite.RenderUpdates()

        self.rings = pygame.sprite.RenderUpdates()
        self.nodes = pygame.sprite.RenderUpdates()

        for i in range(self.n_stones):
            self.g_stones.add(Stone(self.game, Assets.greens_x[i], Assets.greens_y[i], i, self.green_img))
            self.b_stones.add(Stone(self.game, Assets.blues_x[i], Assets.blues_y[i], i, self.blue_img))

            for j in range(len(Assets.nodes_pos_y[i])):
                self.rings.add(SelRing(self.game, Assets.nodes_pos_x[i], Assets.nodes_pos_y[i][j],
                                       self.ring_img, Assets.node_label(i,j)))
                self.nodes.add(Node(self.game, Assets.nodes_pos_x[i], Assets.nodes_pos_y[i][j],
                                    self.node_img, Assets.node_label(i,j)))
                
        self.b_stones.add(Stone(self.game, Assets.h_blue_x[0], Assets.h_blue_y[0], 12, self.hblue_img))

    def check_inputs(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.game_on = False
        
        self.g_stones.update(events, self.rings, self.nodes)
        self.b_stones.update(events, self.rings, self.nodes)
        
    def display_board(self):
        # Set background
        self.game.display.blit(self.game.curr_menu.board, (0,0))

        #self.rings.draw(self.game.display)
        #self.nodes.draw(self.game.display)
        self.g_stones.draw(self.game.display)
        self.b_stones.draw(self.game.display)

        self.game.blit_screen()
    
    def move(self, id, dest_node):
        # Find the right stone to move
        # Get the coords of the destination node
        # Call the move method of the stone
        pass