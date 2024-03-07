import pygame
import Assets

class Stone(pygame.sprite.Sprite):
    def __init__(self, game, x, y, id, img):
        super().__init__()
        self.image  = img
        self.rect   = self.image.get_rect()
        self.img_offset = - int(Assets.IMAGE_DIM/2) + 2
        self.true_x = x
        self.true_y = y
        self.rect.x = self.true_x + self.img_offset
        self.rect.y = self.true_y + self.img_offset

        self.game = game
        self.id   = id

        self.curr_node = Assets.node_label(x,y)

        self.selected = False

        self.hist_x = []
        self.hist_y = []
    
    def update(self, events, rings, nodes):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.rect.collidepoint(event.pos):
                    self.selected = False
                    rings.update(events, self.id)
                    nodes.update(events, self.id)
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.selected = False if self.selected else True
                    rings.update(events, self.id)
                    nodes.update(events, self.id)

    def update_pos(self, x_new, y_new):
        self.true_x = x_new
        self.true_y = y_new
        self.rect.x = x_new + self.img_offset
        self.rect.y = y_new + self.img_offset

    def move(self, dest_x, dest_y):
        self.hist_x.append(self.true_x)
        self.hist_y.append(self.true_y)

        #self.log_move()

        self.update_pos(dest_x, dest_y)
        self.animate_move()
    
    def animate_move(self):
        # NOT WORKING! USE Group.clear()
        delta_x = self.hist_x[-1] - self.true_x
        delta_y = self.hist_y[-1] - self.true_y
        
        for t in range(0,101):
            self.game.display.blit(self.image, (int(self.rect.x + delta_x*t/100 + self.img_offset),
                                                int(self.rect.y + delta_y*t/100 + self.img_offset)))
            self.game.blit_screen()

        
