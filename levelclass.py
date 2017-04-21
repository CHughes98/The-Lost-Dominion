import pygame
import pytmx
import random
import settings
from os import path

class Level:
    def __init__(self, mapfile):
        tm = pytmx.load_pygame(mapfile, pixelaplha = True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render_base(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        num = 0
        for layer in self.tmxdata.visible_layers:
            num += 1
            if num < 9:
                if isinstance(layer, pytmx.TiledTileLayer):
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile, (x * self.tmxdata.tilewidth,
                                                y * self.tmxdata.tileheight))

    def render_top(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        num = 0
        for layer in self.tmxdata.visible_layers:
            num += 1
            if num >= 9:
                if isinstance(layer, pytmx.TiledTileLayer):
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            surface.blit(tile, (x * self.tmxdata.tilewidth,
                                                y * self.tmxdata.tileheight))

    def make_map_base(self):
        map_base = pygame.Surface((self.width, self.height))
        self.render_base(map_base)
        return map_base

    def make_map_top(self):
        map_top = pygame.Surface((self.width, self.height))
        self.render_top(map_top)
        return map_top
    
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
