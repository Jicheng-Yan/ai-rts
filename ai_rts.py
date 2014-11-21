import pygame
import random
import sys

from pygame.locals import * 

import faction
import settings
import unit

from team import Team

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

teams = [
  Team("mhallsmoore", faction.factions["EDF"]),
  Team("jimbo", faction.factions["BAK"])
]

units = [
    unit.MassExtractor(
        teams[0],
        [random.randint(20, 1000), random.randint(20, 750)]
    ) for m in range(0,20)
]
units.extend([
    unit.PowerStation(
        teams[1],
        [random.randint(20, 1000), random.randint(20, 750)]
    ) for m in range(0,20)
])

t = 0.0
framerate = 60.0  # Frames per second
dt = 1000.0/framerate

while True: 
    clock.tick(framerate)
    t += dt
    input(pygame.event.get())
    screen.fill(settings.TERRAIN_COLOURS[0])
    for u in units:
        u.draw_strategic_icon(screen)
    pygame.display.flip()

