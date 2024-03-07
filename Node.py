import pygame
import Assets

class Node(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img, id):
        super().__init__()
        self.image  = img
        self.rect   = self.image.get_rect()
        self.img_offset = - int(Assets.IMAGE_DIM/2) + 2
        self.rect.x = x + self.img_offset
        self.rect.y = y + self.img_offset

        self.game  = game
        self.id    = id

        self.visible  = False
        self.occupied = False

    def update(self, events, id):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.visible = False
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos) and not self.occupied:
                    self.visible = False if self.visible else True