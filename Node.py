import pygame
import Assets

class Node(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img, id):
        super().__init__()
        self.image  = img
        self.rect   = self.image.get_rect()
        self.true_x = x
        self.true_y = y
        self.rect.x = x + Assets.IMG_OFFSET
        self.rect.y = y + Assets.IMG_OFFSET

        self.game  = game
        self.id    = id

        self.visible  = False
        self.occupied = Assets.is_occupied(x, y)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.visible = False
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos) and not self.occupied:
                self.visible = False if self.visible else True

    def draw(self, surface):
        if self.visible:
            surface.blit(self.image, self.rect)