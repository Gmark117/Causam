import pygame

class Stone(pygame.sprite.Sprite):
    def __init__(self, game, x, y, id, img, img_dim):
        super().__init__()
        self.image  = img
        self.rect   = self.image.get_rect()
        self.img_offset = - int(img_dim/2) + 2
        self.rect.x = x + self.img_offset
        self.rect.y = y + self.img_offset

        self.game  = game
        self.id    = id

        self.selected = False

        self.hist_x = []
        self.hist_y = []
    
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selected = False
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.selected = True if self.selected==False else False

    def move(self, dest_x, dest_y):
        self.hist_x.append(self.rect.x)
        self.hist_y.append(self.rect.y)

        #self.log_move()

        self.rect.x = dest_x + self.img_offset
        self.rect.y = dest_y + self.img_offset

        self.animate_move()
    
    def animate_move(self):
        # NOT WORKING! USE SPRITES
        delta_x = self.hist_x[-1] - self.rect.x
        delta_y = self.hist_y[-1] - self.rect.y
        
        for t in range(0,101):
            self.game.display.blit(self.image, (int(self.rect.x + delta_x*t/100), int(self.rect.y + delta_y*t/100)))
            self.game.blit_screen()

        
