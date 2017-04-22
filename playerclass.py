import pygame
import random
import settings
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
	def __init__(self, game, x_start, y_start, health = 100, armor = 0, multiplier = 1):
		self.groups = game.all_sprites
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.image = game.player_img
		self.rect = self.image.get_rect()
		self.rect.centerx = x_start
		self.rect.bottom = y_start
		self.vel = vec(0,0)
		self.pos = vec(self.rect.centerx, self.rect.bottom)
		self.hp = health
		self.amr = armor
		self.multiplier = multiplier
		self.dmg = 0

	def moveDown(self):
		self.rect.bottom += 5
		#self.pos = vec(self.rect.centerx, 5 + self.rect.bottom)
	def moveUp(self):
		self.rect.bottom -= 5
		#self.pos = vec(self.rect.centerx, self.rect.bottom - 5)
	def moveRight(self):
		self.rect.centerx += 5
		#self.pos = vec(self.rect.centerx + 5, self.rect.bottom)
	def moveLeft(self):
		self.rect.centerx -= 5
		#self.pos = vec(self.rect.centerx -5, self.rect.bottom)
	def moveDownPos(self):
		#self.rect.bottom += 5
		return vec(self.rect.centerx, 5 + self.rect.bottom)
	def moveUpPos(self):
		#self.rect.bottom -= 5
		return vec(self.rect.centerx, self.rect.bottom - 5)
	def moveRightPos(self):
		#self.rect.centerx += 5
		return vec(self.rect.centerx + 5, self.rect.bottom)
	def moveLeftPos(self):
		#self.rect.centerx -= 5
		return vec(self.rect.centerx -5, self.rect.bottom)
