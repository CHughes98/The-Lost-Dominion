#Imports
import pygame
import random
import settings
import sprites
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
        pygame.display.set_caption("My Game")
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # Start a New Game
        self.all_sprites = pygame.sprite.Group()
        player = sprites.Player(settings.WIDTH / 2, settings.HEIGHT / 2)
        self.all_sprites.add(player)
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.strike()

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
