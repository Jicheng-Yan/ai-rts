import pygame
import random
import sys

from pygame.locals import * 

import settings
import unit

pygame.init() 
 
window = pygame.display.set_mode(settings.SCREEN_RESOLUTION) 
pygame.display.set_caption('AI RTS') 
screen = pygame.display.get_surface() 

def input(events): 
   for event in events: 
      if event.type == QUIT: 
         sys.exit(0) 
      elif event.type == KEYDOWN and event.key == K_ESCAPE:
         sys.exit(0)
   
clock = pygame.time.Clock()

factions = ["Earth Defence Force", "Ba'ktul Alliance", "Tyranos Collective"]
units = [
    unit.MassExtractor(
        random.choice(factions), 1, 
        [random.randint(20, 1000), random.randint(20, 750)]
    ) for m in range(0,20)
]
units.extend([
    unit.PowerStation(
        random.choice(factions), 1, 
        [random.randint(20, 1000), random.randint(20, 750)]
    ) for m in range(0,20)
])

while True: 
    clock.tick(60)
    input(pygame.event.get())
    screen.fill(settings.TERRAIN_COLOURS[0])
    for u in units:
        u.draw_strategic_icon(screen)
    pygame.display.flip()

