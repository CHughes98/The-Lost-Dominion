import pygame
import random
import settings

class Player(pygame.sprite.Sprite):
    def __init__(self, x_start, y_start, health = 100, armor = 0, multiplier = 1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 60))
        pygame.Surface.fill(self.image, settings.RED)
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x_start
        self.rect.bottom = y_start
        self.hp = health
        self.amr = armor
        self.multiplier = multiplier
        self.speedx = 0
        self.speedy = 0
        self.dmg = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        if keystate[pygame.K_d]:
            self.speedx = 5
        if keystate[pygame.K_w]:
            self.speedy = -5
        if keystate[pygame.K_s]:
            self.speedy = 5
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > settings.WIDTH:
            self.rect.right = settings.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def strike(self):
        self.roll = random.randrange(1,7)
        self.dmg = self.roll * self.multiplier
        print(self.dmg)
