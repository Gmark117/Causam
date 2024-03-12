import pygame
import Assets

class Stone(pygame.sprite.Sprite):
    def __init__(self, game, x, y, label, img):
        super().__init__()
        self.image  = img
        self.rect   = self.image.get_rect()
        self.true_x = x
        self.true_y = y
        self.rect.x = x + Assets.IMG_OFFSET
        self.rect.y = y + Assets.IMG_OFFSET

        self.game = game
        self.lvl  = Assets.get_lvl(label[0])
        self.node = int(label[1:])

        self.label = label

        self.selected = False

        self.hist_x = []
        self.hist_y = []
        #self.t = 0
        #self.steps = 1000
    
    def update(self, events, selection, nodes, next_nodes):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.rect.collidepoint(event.pos):
                self.selected = False
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
                self.selected = False if self.selected else True
                if self.selected:
                    Assets.update_selection(nodes, next_nodes, selection, self)

    def update_pos(self, x_new, y_new):
        self.true_x = x_new
        self.true_y = y_new
        self.rect.x = x_new + Assets.IMG_OFFSET
        self.rect.y = y_new + Assets.IMG_OFFSET

        self.label = Assets.node_label(self.true_x, self.true_y)

    def move(self, dest_x, dest_y):
        self.hist_x.append(self.true_x)
        self.hist_y.append(self.true_y)

        #self.log_move()

        self.update_pos(dest_x, dest_y)
        # return self.animate_move()
    
    def animate_move(self):
        # NOT WORKING! USE Group.clear()
        delta_x = self.hist_x[-1] - self.true_x
        delta_y = self.hist_y[-1] - self.true_y

        if self.t<self.steps:
            self.t += 1

        self.game.display.blit(self.image, (int(self.hist_x[-1] + Assets.IMG_OFFSET - delta_x*self.t/self.steps),
                                            int(self.hist_y[-1] + Assets.IMG_OFFSET - delta_y*self.t/self.steps)))
        
        if self.t==self.steps:
            self.t = 0
            return False
        
        return True