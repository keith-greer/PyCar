import pygame
from pygame.locals import *
size = width, height = (400, 800)
road_w = int (width/1.6)
roadmark_w = int (width/80)

#initialising game
pygame.init()
running = True,

# Sets screen dimensions based off of "size" variable above
screen = pygame.display.set_mode((size))
#sets screen title caption
pygame.display.set_caption("PyCar")
#sets background colour of screen
screen.fill((234, 182, 118))
#draw game graphics
#Road
pygame.draw.rect(
    screen,
    (50,50,50),
    (width/2-road_w/2, 0, road_w, height))
#Road markings centre
pygame.draw.rect(
    screen,
    (255, 240, 60),
    (width/2 - roadmark_w/2, 0, roadmark_w, height))
#Road markings left
pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))

#Road markings right
pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))


#apply changes
pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()