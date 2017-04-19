import pygame
import random
import settings
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
	def __init__(self, game, x_start, y_start, health = 100, armor = 0, multiplier = 1.15):
		self.groups = game.all_sprites
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.image = pygame.Surface((30, 60))
		pygame.Surface.fill(self.image, settings.RED)
		# self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = x_start
		self.rect.bottom = y_start
		self.vel = vec(0,0)
		self.pos = vec(self.rect.centerx, self.rect.bottom)
		self.hp = health
		self.amr = armor
		self.multiplier = multiplier
		#self.speedx = 0
		#self.speedy = 0
		self.dmg = 0

	def update(self):
		

	'''def update(self):
		#self.speedx = 0
		#self.speedy = 0
		#keystate = pygame.key.get_pressed()
		pygame.key.get_pressed()
		#self.rect.x += self.speedx
		#self.rect.y += self.speedy'''

	def strike(self):
		self.roll = random.randrange(1,7)
		print(self.roll)
		self.dmg = self.roll * self.multiplier
		'''Maybe make also add a wave multiplier for damage increase, if we dont have that already'''
		print(self.dmg)
		

	def moveUp(self):
		self.rect.bottom += 5

	def moveDown(self):
		self.rect.bottom -= 5

	def moveLeft(self):
	    	self.rect.centerx += 5

	def moveRight(self):
	    	self.rect.centerx -= 5
