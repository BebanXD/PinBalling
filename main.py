import pygame
import numpy as np
from pathlib import Path
from inputs import *
from elements import *
from collision import *
from functions import *


#Game Basics
pygame.init()                   # essential
pygame.display.set_caption("PinBalling") # window name
pygame.display.set_icon(pygame.image.load("Image\PINBALLING_LOGO.jpeg")) #window icon
clock    = pygame.time.Clock()   # essential
font1    = pygame.font.Font("Misc\DEVIL_LETTERS.otf",50)
font2    = pygame.font.Font("Misc\FACELESS.ttf",50)
font3    = pygame.font.Font("Misc\TheGrindeR.ttf",50)
WINDOW_X = 720
WINDOW_Y = 1000
screen   = pygame.display.set_mode([WINDOW_X, WINDOW_Y]) # essential

#general variables
running = True      # while loop var.
game_over = False   # check if game over
Score   = 0         # tracks score

#time
FPS = 60
t   = 0
dt  = 1

#Surfaces
background = pygame.image.load("Image\Skelleton_Background_0.jpg").convert()
gameoverscreen= pygame.image.load("Image\GAME_OVER_SCREEN.webp").convert()
text = font1.render("HELL YEAH",False,"Red")
gameovertext = font2.render("Final Score: "+str(Score),False,"Red")
Ball  = pygame.image.load("Image\Skelleton_Background_0.jpg").convert()

while running:
    t+=dt
    for event in pygame.event.get():  # Get's all the user action (keyboard, mouse, joysticks, ...)
                continue
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: #kill command
            running = False
    if keys[pygame.K_SPACE]: #sick audio
        pygame.mixer.Sound('Audio\SICK_ASS_RIFF.mp3').play()
        game_over=True

    if not game_over:
        # Background
        screen.blit(background,(0,0))
        screen.blit(text,(t,30*np.sin(t/60)))
    

    if game_over:
        screen.blit(gameoverscreen,(0,0))
        screen.blit(gameovertext,(0,0))
    
    #Clocktick
    pygame.display.update()
    clock.tick(FPS) # 60 frames per second 

