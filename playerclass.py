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
        self.image = pygame.transform.scale(player_img, (64, 64))
        self.image.set_colorkey(settings.WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x_start
        self.rect.centery = y_start
        self.hp = health
        # self.amr = armor
        self.multiplier = multiplier
        self.velocity = 5
        self.dmg = 0

    def strike(self):
        self.roll = random.randrange(1,7)
        self.dmg = self.roll * self.multiplier
        print(self.dmg)

    def moveDown(self):
        self.rect.centery += self.velocity

    def moveUp(self):
        self.rect.centery -= self.velocity

    def moveRight(self):
	    self.rect.centerx += self.velocity

    def moveLeft(self):
<<<<<<< HEAD
	    self.rect.centerx -= self.velocity
=======
	    self.rect.centerx -= 5
		
		
		
	def attack(self):
		pygame.drawCircle(32)
		hits = pygame.sprites.spritescollide(player.sprite, mob.sprite, false)
		if hits:
			for hit in hits:
				dmg = self.strike
				mob.health -= hit
		
		return hits
>>>>>>> df42ad2cf8f90210deda46214d715ff016111b29
