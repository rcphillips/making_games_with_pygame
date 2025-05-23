#animation.py
#animation!!!

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 165
fpsClock = pygame.time.Clock() 

# set up the ol window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png') #hell ya
catx = 10
caty = 10
direction = 'right'

while True: #the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx+= 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty +=5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -=5
        if catx == 10:
            direction = 'up' 
    elif direction == 'up':
        caty -= 5
        if caty ==10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty)) #actually putting an image into the display
    # x y indicate the upper left corner of the image.
    # and note that you're doing this over and over to create 'motion'

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    fpsClock.tick(FPS) #this puts a pause in between loops of the main game loop, dependent on the FPS. but if there's too much to do on each loop, you'll get lag.

