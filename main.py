#Imports
import pygame
import random
import settings
from playerclass import Player
# from mobclass import Mob
from levelclass import Level
from os import path

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
		map_folder = path.join(path.dirname(__file__), "map")
		self.obstacles = pygame.sprite.Group()

		#Renders the base of the map(below player)
		self.level_base = Level(path.join(map_folder, 'arena1.tmx'))
		self.level_base_img = self.level_base.make_map_base()
		self.level_base_rect = self.level_base_img.get_rect()

		#Renders the top of the map(above player)
		self.level_top = Level(path.join(map_folder, 'arena1.tmx'))
		self.level_top_img = self.level_top.make_map_top()
		self.level_top_img.set_colorkey(settings.BLACK)
		self.level_top_rect = self.level_top_img.get_rect()

		#Obstacle
		self.obstacle = Level(path.join(map_folder, 'arena1.tmx'))
		self.obstacle_img = self.obstacle.make_obstacles()
		self.obstacle_img.set_colorkey(settings.BLACK)
		self.object_layer_rect = self.obstacle_img.get_rect()


		pygame.display.set_caption("The Lost Dominion")
		self.clock = pygame.time.Clock()
		self.running = True

	def new(self):
		# Start a New Game
		self.all_sprites = pygame.sprite.Group()
		self.player = Player(50, 500)
		self.all_sprites.add(self.player)
		self.run()

	def run(self):
		# Game loop
		self.playing = True
		while self.playing:
			self.clock.tick(settings.FPS)
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
			# Check for strike
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.player.strike()
		self.movement()

	def movement(self):
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
			self.player.moveRight()
		if keystate[pygame.K_a] or keystate[pygame.K_LEFT]:
			self.player.moveLeft()
		if keystate[pygame.K_s] or keystate[pygame.K_DOWN]:
			self.player.moveDown()
		if keystate[pygame.K_w] or keystate[pygame.K_UP]:
			self.player.moveUp()

	# def check_for_collisions(self):
	# 	collisions = pygame.sprite.spritecollide(self.player, self.obstacles, False)
	# 	if collisions:
	# 		if collisions[0].rect.centerx > self.player.centerx:
	# 			self.player.centerx = collisions[0].rect.left - self.player.width / 2
	# 		if collision[0].rect.centerx < self.player.centerx:
	# 			self.player.centerx = collision[0].rect.right + self.player.width / 2
	# 			self.player.velocity = 0

	def attack(self):
		pygame.drawCircle(32)
		hits = pygame.sprite.spritecollide(self.player, self.mobs, False)
		if hits:
			for hit in hits:
				dmg = player.strike()
				mob.health -= dmg

	def draw(self):
		# Game loop - Draw
		# self.screen.fill(settings.BLACK)
		self.screen.blit(self.level_base_img, self.level_base_rect)
		self.screen.blit(self.obstacle_img, self.object_layer_rect)
		self.obstacles.draw(self.screen)
		self.all_sprites.draw(self.screen)
		self.screen.blit(self.level_top_img, self.level_top_rect)
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
