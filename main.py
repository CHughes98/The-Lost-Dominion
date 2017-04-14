#Imports
import pygame
import random
import math
#import settings
#from playerclass import Player
from playerclass import *
from settings import *
#from mobclass import Mob
# from levelclass import Level
#from os import path
import os
from mobclass import *

def draw_text(surf, text, size, x, y):
	font = pygame.font.Font(font_name, size)
	text_surface = font.render(text, True, WHITE)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surf.blit(text_surface, text_rect)

class Game:
	def __init__(self):
        # Initialize game window
		pygame.init()
		pygame.mixer.init()
		self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
		pygame.display.set_caption("The Lost Dominion")
		self.clock = pygame.time.Clock()
		self.running = True
		self.load_data()


	def load_data(self):
		game_folder = os.path.dirname(__file__)
		img_folder = os.path.join(game_folder, 'img')
		#self.map = Map(os.path.join(game_folder, 'map.txt'))
		#self.player_img = pg.image.load(os.path.join(img_folder, PLAYER_IMG)).convert_alpha()
		self.mob_img = pygame.image.load(os.path.join(img_folder, MOB_IMG)).convert_alpha()


	def new(self):
        # Start a New Game
		self.all_sprites = pygame.sprite.Group()
		self.player = Player(self, settings.WIDTH / 2, settings.HEIGHT / 2) 
		self.all_sprites.add(self.player)
		self.mobs = pygame.sprite.Group()
		self.mob = Mob(self, settings.WIDTH / 4, settings.HEIGHT / 4, 10, 1)
		self.all_sprites.add(self.mob)
		self.run()

	def run(self):
        # Game loop
		self.playing = True
		while self.playing:
			self.dt = self.clock.tick(settings.FPS)/1000#For seconds
			self.events()
			self.update()
			self.draw()

	def update(self):
	# Game loop - Update
		self.all_sprites.update()

	def events(self):
	# Game loop - Events
		for event in pygame.event.get():
		# Check for closing the window
			if event.type == pygame.QUIT:
				self.playing = False
				self.running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.player.strike()
				keystate = pygame.key.get_pressed()
				if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
					self.player.moveLeft()
				if keystate[pygame.K_a] or keystate[pygame.K_LEFT]:
					self.player.moveRight()
				if keystate[pygame.K_s] or keystate[pygame.K_DOWN]:
					self.player.moveUp()
				if keystate[pygame.K_w] or keystate[pygame.K_UP]:
					self.player.moveDown()

	def draw(self):
		# Game loop - Draw
		self.screen.fill(settings.BLACK)
		self.all_sprites.draw(self.screen)
		# *after* drawing everything, flip the display
		pygame.display.flip()

	def show_start_screen(self):
	# Game splash/start screen
		pass

	def show_go_screen(self):
	# Game over/continue
		pass

def main():
	g = Game()
	g.show_start_screen()
	while g.running:
		g.new()
		g.show_go_screen()

main()
