import pygame
from pygame.locals import *
import random

size = width, height = (400, 800)
road_w = int (width/1.6)
roadmark_w = int (width/80)

#initialising game
pygame.init()
running = True,

# Sets screen dimensions based off of "size" variable above
screen = pygame.display.set_mode((size))
#sets screen title caption
pygame.display.set_caption("PyCar by KEEFUSOFT ™")
#sets background colour of screen
screen.fill((234, 182, 118))
    
    
    
#Draw game graphics
#
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


#image load
car = pygame.image.load("car.png")
enemy_car = pygame.image.load("enemy.png")


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
#Dynamic car resizing within the loop
        car_width_fraction = 0.2
        car_height_fraction = 0.2
        car_width = int(width * car_width_fraction)
        car_height = int(height * car_height_fraction)
        car_resizer = pygame.transform.scale(car, (car_width, car_height))
        car_loc = car_resizer.get_rect()
        car_loc.center = int(width/2 + road_w/4), int(height*0.8)

#Dynamic Enemy car resizing within the loop
        enemy_car_width_fraction = 0.2
        enemy_car_height_fraction = 0.2
        enemy_car_width = int(width * enemy_car_width_fraction)
        enemy_car_height = int(height * enemy_car_height_fraction)
        enemy_car_resizer = pygame.transform.scale(enemy_car, (enemy_car_width, enemy_car_height))
        enemy_car_loc = enemy_car_resizer.get_rect()
        enemy_car_loc.center = int(width/2 - road_w/4), int(height*0.2)

        screen.blit(car_resizer, car_loc)
        screen.blit(enemy_car_resizer, enemy_car_loc)

    #apply changes
    pygame.display.update()

pygame.quit()