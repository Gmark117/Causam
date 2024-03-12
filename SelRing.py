import pygame
import Assets

class SelRing(pygame.sprite.Sprite):
    def __init__(self, game, x, y, img, label):
        super().__init__()
        self.image  = img
        self.rect   = self.image.get_rect()
        self.true_x = x
        self.true_y = y
        self.rect.x = x + Assets.IMG_OFFSET
        self.rect.y = y + Assets.IMG_OFFSET

        self.game  = game
        self.lvl  = Assets.get_lvl(label[0])
        self.node = int(label[1:])

        self.visible = False
        self.occupied = Assets.is_occupied(x, y)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.rect.collidepoint(event.pos):
                self.visible = False
            if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
                self.visible = False if self.visible else True

    def draw(self, surface):
        if self.visible:
            surface.blit(self.image, self.rect)