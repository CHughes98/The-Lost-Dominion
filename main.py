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
import makestats

class Game:
	def __init__(self):
		# Initialize game window
		pygame.init()
		pygame.mixer.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

		pygame.display.set_caption("The Lost Dominion")
		self.clock = pygame.time.Clock()
		self.load_data()

	def load_data(self):
		game_folder = os.path.dirname(__file__)
		img_folder = os.path.join(game_folder, 'img')

		self.font_name = pygame.font.match_font("algerian")

		self.logo = pygame.image.load(os.path.join(img_folder, LOGO_IMG)).convert_alpha()
		self.logo = pygame.transform.scale2x(self.logo)

		self.player_img = pygame.image.load(os.path.join(img_folder, PLAYER_IMG)).convert_alpha()

		self.icon = pygame.image.load(os.path.join(img_folder, ICON)).convert_alpha()
		self.icon = pygame.transform.scale(self.icon, (128, 128))

		self.mob_img = pygame.image.load(os.path.join(img_folder, MOB_IMG)).convert_alpha()

		self.mob_icon = pygame.image.load(os.path.join(img_folder, MOB_ICON)).convert_alpha()
		self.mob_icon = pygame.transform.scale(self.mob_icon, (32, 32))

		map_folder = path.join(path.dirname(__file__), "map")

		#Renders the map
		self.map = Level(path.join(map_folder, 'arena1.tmx'))
		self.map_img = self.map.make_map()
		self.map_img = pygame.transform.scale(self.map_img, (WIDTH, HEIGHT))
		self.map_rect = self.map_img.get_rect()

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
	    fill = (pct / 100) * BAR_LENGTH
	    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
	    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
	    pygame.draw.rect(surf, bar_color, fill_rect)
	    pygame.draw.rect(surf, BLACK, outline_rect, 2)

	def draw_text(self, surf, text, size, x, y, color):
		font = pygame.font.Font(self.font_name, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)
		surf.blit(text_surface, text_rect)

	def attack(self):
		#pygame.drawCircle(32)
		hits = pygame.sprite.spritecollide(self.player, self.mobs, False)
		if hits:
			for hit in hits:
				self.player.strike()
				hit.hp -= self.player.dmg
				print(hit.hp)
				if hit.hp <= 0:
					hit.kill()
					self.mob_amt -= 1

	def get_hit(self):
		hits = pygame.sprite.spritecollide(self.player, self.mobs, False)
		if hits:
			for hit in hits:
				self.player.hp -= self.mob.attackStrength
				if self.player.hp <= 0:
					self.player.kill()

	def set_boundaries(self):
		if self.player.rect.right >= 46 * TILESIZE:
			self.player.rect.right = 46 * TILESIZE
		if self.player.rect.left <= 8 * TILESIZE:
			self.player.rect.left = 8 * TILESIZE
		if self.player.rect.bottom >= 24 * TILESIZE:
			self.player.rect.bottom = 24 * TILESIZE
		if self.player.rect.top <= 6 * TILESIZE:
			self.player.rect.top = 6 * TILESIZE

	def draw_enemies(self, surf, x, y, img):
	    for i in range(self.mob_amt):
	        img_rect = img.get_rect()
	        img_rect.x = x + (48 * i)
	        img_rect.y = y
	        surf.blit(img, img_rect)

	def create_enemies(self, x, y):
		self.mob = Mob(self, x, y, makestats.makeHealth(1), makestats.makeStrength(1))
		self.all_sprites.add(self.mob)
		self.mobs.add(self.mob)

	def new(self):
        # Start a New Game
		self.all_sprites = pygame.sprite.Group()
		self.player = Player(self, 9, 17, 100, 0)
		self.all_sprites.add(self.player)
		self.mobs = pygame.sprite.Group()
		self.mob_amt = 13

		for i in range(self.mob_amt):
			self.create_enemies(44, 6 + (i * 1.5))

	def run(self):
		# Game loop
		self.playing = True
		self.new()
		while self.playing:
			self.dt = self.clock.tick(FPS)/1000 #For seconds
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
		self.screen.blit(self.map_img, self.map_rect)
		self.all_sprites.draw(self.screen)

		self.screen.blit(self.icon, (8, HEIGHT - 132))
		self.draw_enemies(self.screen, 152, HEIGHT - 106, self.mob_icon)
		self.draw_bar(self.screen, 136, HEIGHT - 70, self.player.hp, RED)
		self.draw_bar(self.screen, 136, HEIGHT - 38, self.player.amr, GREY)
		# *after* drawing everything, flip the display
		pygame.display.flip()

	def show_start_screen(self):
		self.screen.blit(self.map_img, self.map_rect)
		self.draw_text(self.screen, "Press any key to begin!", 36, 648, 512, BLACK)
		self.screen.blit(self.logo, (240, 64))
		pygame.display.flip()
		self.waiting = True
		while self.waiting:
			self.clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_ESCAPE:
						exit()
					else:
						pygame.mixer.music.load(os.path.join(path.dirname(__file__), "snd", "song1.wav"))
						pygame.mixer.music.play(loops = -1)

						self.waiting = False
						self.running = True

	def show_go_screen(self):
		# Game over/continue
		pass

def main():
	g = Game()
	g.show_start_screen()
	while g.running:
		g.run()
		g.show_go_screen()

main()
