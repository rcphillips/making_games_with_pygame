#fonttext.py

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('write write')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)


fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world!', True, WHITE, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)


pygame.mixer.music.load(filename='00 - This Much is True (the Truths).wav')
pygame.mixer.music.play(-1, 0.0)


#soundObj = pygame.mixer.Sound('match1.wav')
#soundObj.play()
#import time
#time.sleep(.5)
#soundObj.stop()

while True: #main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj) #from our text object to our rectangle object DERIVED FROM THE TEXT OBJECT? hmmph. anyway and all on display surface? Or is it that two objects are going onto the surface?
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()