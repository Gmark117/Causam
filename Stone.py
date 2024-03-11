import pygame
import Assets

class Stone(pygame.sprite.Sprite):
    def __init__(self, game, x, y, id, img):
        super().__init__()
        self.image  = img
        self.rect   = self.image.get_rect()
        self.true_x = x
        self.true_y = y
        self.rect.x = x + Assets.IMG_OFFSET
        self.rect.y = y + Assets.IMG_OFFSET

        self.game = game
        self.id   = id

        self.curr_node = Assets.node_label(x,y)

        self.selected = False

        self.hist_x = []
        self.hist_y = []
    
    def update(self, events, selection):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.rect.collidepoint(event.pos):
                self.selected = False
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
                self.selected = False if self.selected else True
        
        if self.selected:
            Assets.update_selection(selection, self)

    def update_pos(self, x_new, y_new):
        self.true_x = x_new
        self.true_y = y_new
        self.rect.x = x_new + Assets.IMG_OFFSET
        self.rect.y = y_new + Assets.IMG_OFFSET

        self.curr_node = Assets.node_label(self.true_x, self.true_y)

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
        
        for t in range(1,101):
            self.game.display.blit(self.image, (int(self.rect.x + delta_x*t/100),
                                                int(self.rect.y + delta_y*t/100)))
            self.game.blit_screen()

        
