import pygame
import random
import math
import settings
from playerclass import Player
vec = pygame.math.Vector2


class Mob(pygame.sprite.Sprite):
	def __init__(self, game, x_start, y_start, health, attackStrength):
		self.groups = game.all_sprites, game.mobs
		pygame.sprite.Sprite.__init__(self, self.groups)
		self.game = game
		#self.image = pygame.Surface((50, 120))
		self.image = game.mob_img
		#pygame.Surface.fill(self.image, settings.BLUE)
		# self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = x_start
		self.rect.bottom = y_start
		self.pos = vec(self.rect.centerx, self.rect.bottom)
		self.vel = vec(0,0)
		self.acc = vec(0,0)
		self.rect.center = self.pos
		self.hp = health
		#self.speedx = 0
		#self.speedy = 0
		self.speed = 10
		self.attackStrength = 0
		self.rot = 0


	'''def enemyMovesToPlayer(self, Player): #Defines enemy movement and takes Player object as parameter so player's position can be used
		differentX = self.rect.x - Player.rect.x #Obtain difference between player position and enemy position (x)
		differentY = self.rect.y - Player.rect.y #Obtain difference between player position and enemy position (y)
		magnitudeVectorLength = math.sqrt((differentX**2) + (differentY**2)) #Calculates the magnitude (length) of the distance between player and enemy
		normalizedVectorX = (differentVectorX / magnitudeVectorLength) #Detemines the normalized vector X - component
		normalizedVectorY = (differentVectorY / magnitudeVectorLength) #Determines the normalized vector Y - component
		speedVectorX = normalizedVectorX * self.speed #Mutliply self.speed as multiplier with normal vector to determine speed vector
		speedVectorY = normalizedVectorY * self.speed #Mutliply self.speed as multiplier with normal vector to determine speed vector
		self.rect.x += speedVectorX #Has the enemy position altered so it can chase after player
        	self.rect.y += speedVectorY #Has the enemy position altered so it can chase after player
		if(speedVectorX >= differentX):
			#Collision between player and enemy will occur
		if(speedVectorY >= differentY):
			#Collision between player and enemy will occur

	def enemyMovesToPlayer(self, Player):
		player = pygame.math.Vector2(Player.rect.x, Player.rect.y)
		enemy = pygame.math.Vector2(self.rect.x, self.rect.y)
		movement = player - enemy
		realMovement = pygame.math.Vector2.normalize(movement)
		realMovement *= self.speed
		realMovement += enemy'''
		
		
	def update(self):
		self.rot = (self.game.player.pos - self.pos).angle_to(vec(1,0))
		self.image = pygame.transform.rotate(self.game.mob_img, self.rot)
		self.rect = self.image.get_rect()
		self.rect.center = self.pos
		self.acc = vec(50,0).rotate(-self.rot)
		self.acc += self.vel * -1
		self.vel += self.acc * self.game.dt
		self.pos += self.vel * self.game.dt + (0.5 * self.acc * self.game.dt ** 2)
		'''self.hit_rect.centerx = self.pos.x
		collide_with_walls(self, self.game.walls, 'x')
		self.hit_rect.centery = self.pos.y
		collide_with_walls(self, self.game.walls, 'y')
		self.rect.center = self.hit_rect.center'''










