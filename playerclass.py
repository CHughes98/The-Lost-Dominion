import pygame
import random
import settings
from os import path

class Player(pygame.sprite.Sprite):
    def __init__(self, x_start, y_start, health = 100, armor = 0, multiplier = 1):
        pygame.sprite.Sprite.__init__(self)
        img_dir = path.join(path.dirname(__file__), "img")
        player_img = pygame.image.load(path.join(img_dir, "sprite.png")).convert()
        # self.image = pygame.Surface((30, 60))
        # pygame.Surface.fill(self.image, settings.RED)
        self.image = pygame.transform.scale(player_img, (30, 60))
        self.image.set_colorkey(settings.WHITE)
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
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def strike(self):
        self.roll = random.randrange(1,7)
        self.dmg = self.roll * self.multiplier
        print(self.dmg)

    def moveDown(self):
        self.rect.bottom += 5

    def moveUp(self):
        self.rect.bottom -= 5

    def moveRight(self):
	    self.rect.centerx += 5

    def moveLeft(self):
	    self.rect.centerx -= 5
