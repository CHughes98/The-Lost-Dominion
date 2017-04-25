import pygame
from settings import *

class Hitbox(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.hitbox = pygame.Surface((24, 24))
    self.rect = self.hitbox.get_rect()
    self.rect.midleftx = x
    self.rect.bottomlefty = y
    
 
