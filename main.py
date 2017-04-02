# Pygame template
import pygame
import random

def main():
    # Defines the screen size and times per second the game updates
    WIDTH = 360
    HEIGHT = 480
    FPS = 30

    # define basic debug colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # Creates a group that all sprites in the game must be added to
    # Used for updates
    all_sprites = pygame.sprite.Group()

    # Initialize pygame as well as sound capabilities and create window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    # Game Loop
    running = True
    while running:
        # Keeps loop running at the right speed
        clock.tick(FPS)
        # Process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                running = False

        # Update
        all_sprites.update()

        # Render
        screen.fill(BLACK)
        all_sprites.draw(screen)
        # *after* drawing everything, flip the display
        # This makes the game run faster as its not updating each pixel
        # Instead it updates everything "behind" the screen and then shows it
        pygame.display.flip()

    pygame.quit()

main()
