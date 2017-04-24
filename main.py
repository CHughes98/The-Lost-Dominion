#Imports
import pygame
import random
#import settings
from settings import *
from playerclass import *
from mobclass import *
from levelclass import *
from os import *
import os

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
		self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN)

		pygame.display.set_caption("The Lost Dominion")
		self.clock = pygame.time.Clock()
		self.running = True
		self.load_data()

	def load_data(self):
		game_folder = os.path.dirname(__file__)
		img_folder = os.path.join(game_folder, 'img')
		self.player_img = pygame.image.load(os.path.join(img_folder, PLAYER_IMG)).convert_alpha()

		self.icon = pygame.image.load(os.path.join(img_folder, ICON)).convert_alpha()
		self.icon = pygame.transform.scale(self.icon, (64, 64))

		self.mob_img = pygame.image.load(os.path.join(img_folder, MOB_IMG)).convert_alpha()

		map_folder = path.join(path.dirname(__file__), "map")

		#Renders the base of the map(below player)
		self.level_base = Level(path.join(map_folder, 'arena1.tmx'))
		self.level_base_img = self.level_base.make_map_base()
		self.level_base_rect = self.level_base_img.get_rect()

		#Renders the top of the map(above player)
		self.level_top = Level(path.join(map_folder, 'arena1.tmx'))
		self.level_top_img = self.level_top.make_map_top()
		self.level_top_img.set_colorkey(settings.BLACK)
		self.level_top_rect = self.level_top_img.get_rect()

	def movement(self):
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_d] or keystate[pygame.K_RIGHT]:
			self.player.moveRight()
			self.player.pos = self.player.moveRightPos()
		if keystate[pygame.K_a] or keystate[pygame.K_LEFT]:
			self.player.moveLeft()
			self.player.pos = self.player.moveLeftPos()
		if keystate[pygame.K_s] or keystate[pygame.K_DOWN]:
			self.player.moveDown()
			self.player.pos = self.player.moveDownPos()
		if keystate[pygame.K_w] or keystate[pygame.K_UP]:
			self.player.moveUp()
			self.player.pos = self.player.moveUpPos()

	def draw_bar(self, surf, x, y, pct, bar_color):
	    if pct < 0:
	        pct = 0
	    fill = (pct / 100) * settings.BAR_LENGTH
	    outline_rect = pygame.Rect(x, y, settings.BAR_LENGTH, settings.BAR_HEIGHT)
	    fill_rect = pygame.Rect(x, y, fill, settings.BAR_HEIGHT)
	    pygame.draw.rect(surf, bar_color, fill_rect)
	    pygame.draw.rect(surf, settings.BLACK, outline_rect, 2)

	def attack(self):
		#pygame.drawCircle(32)
		hits = pygame.sprite.spritecollide(self.player, self.mobs, False)
		if hits:
			for hit in hits:
				self.player.strike()
				self.mob.hp -= self.player.dmg
				print(self.mob.hp)
		if self.mob.hp < 0:
			self.mob.kill()

	def get_hit(self):
		hits = pygame.sprite.spritecollide(self.player, self.mobs, False)
		if hits:
			for hit in hits:
				self.player.hp -= 5

	def set_boundaries(self):
		if self.player.rect.right >= 43 * TILESIZE:
			self.player.rect.right = 43 * TILESIZE
		if self.player.rect.left <= 8 * TILESIZE:
			self.player.rect.left = 8 * TILESIZE
		if self.player.rect.bottom >= 23 * TILESIZE:
			self.player.rect.bottom = 23 * TILESIZE
		if self.player.rect.top <= 4 * TILESIZE:
			self.player.rect.top = 4 * TILESIZE

	def new(self):
        # Start a New Game
		self.all_sprites = pygame.sprite.Group()
		self.player = Player(self, 9, 17)
		self.all_sprites.add(self.player)

		self.mobs = pygame.sprite.Group()
		self.mob = Mob(self, 43, 14, 10, 1)
		self.all_sprites.add(self.mob)
		self.mobs.add(self.mob)

		self.run()

	def run(self):
		# Game loop
		self.playing = True
		while self.playing:
			self.dt = self.clock.tick(settings.FPS)/1000#For seconds
			self.events()
			self.update()
			self.draw()


	def events(self):
		# Game loop - Events
		for event in pygame.event.get():
			# Check for closing the window
			if event.type == pygame.QUIT:
				self.playing = False
				self.running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.attack()
				if event.key == pygame.K_ESCAPE:
					self.playing = False
					self.running = False

		self.movement()
		self.set_boundaries()
		self.get_hit()

	def update(self):
		# Game loop - Update
		self.all_sprites.update()

	def draw(self):
		# Game loop - Draw
		self.screen.blit(self.level_base_img, self.level_base_rect)
		self.all_sprites.draw(self.screen)
		self.screen.blit(self.level_top_img, self.level_top_rect)

		self.screen.blit(self.icon, (8, settings.HEIGHT - 70))
		self.draw_bar(self.screen, 73, settings.HEIGHT - 42, self.player.hp, settings.RED)
		self.draw_bar(self.screen, 73, settings.HEIGHT - 24, self.player.amr, settings.GREY)
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
