import pygame
import pytmx
import random
import settings
from os import path

class Level:
    def __init__(self, mapfile):
        tm = pytmx.load_pygame(mapfile, pixelaplha = True)
        pygame.sprite.Sprite.__init__(self)
        self.obstacle_group = pygame.sprite.Group()
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render_map(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
                if isinstance(layer, pytmx.TiledTileLayer):
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile, (x * self.tmxdata.tilewidth,
                                                y * self.tmxdata.tileheight))

    def make_map(self):
        self.map = pygame.Surface((self.width, self.height))
        self.render_map(self.map)
        return self.map

    def roll_stats(self, player):
        end_of_wave_roll = random.choice(1, 3)
        if(end_of_wave_roll == 1):
            player.health += health.points(25)
            print(player.health)
        if(end_of_wave_roll == 2):
            player.health -= health.points(15)
            print(player.health)
        else:
            player.strength += strength(5)
            print(player.strength)

        return
