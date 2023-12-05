import pygame
import numpy as np
from pathlib import Path


#Game Basics
pygame.init()                   # essential
pygame.display.set_caption("PinBalling") # window name
pygame.display.set_icon(pygame.image.load("Image\PINBALLING_LOGO.jpeg")) #window icon
clock    = pygame.time.Clock()   # essential
font1    = pygame.font.Font("Misc\DEVIL_LETTERS.otf",50)
font2    = pygame.font.Font("Misc\FACELESS.ttf",50)
font3    = pygame.font.Font("Misc\TheGrindeR.ttf",100)
WINDOW_X = 690
WINDOW_Y = 950
screen   = pygame.display.set_mode([WINDOW_X, WINDOW_Y]) # essential

#game variables
running = True      # while loop var.
game_state = 1      # check postion of screen
score   = 0         # tracks score
health  = 3

#time
FPS = 60
t   = 0
dt  = 1

last_input_time = 0
cooldown_time   = 200

#Surfaces
startscreen = pygame.image.load("Image\Skelleton_Background_0.jpg").convert()
background = pygame.image.load("Image\Skelleton_Background_2.webp").convert()
gameoverscreen= pygame.image.load("Image\GAME_OVER_SCREEN.webp").convert()

starttext = font3.render("CHOOSE YOUR BALLS",False,"Red")
text = font1.render("HELL YEAH",False,"Red")
gameovertext = font2.render("Final Score: "+str(score),False,"Red")

Ball1 = pygame.image.load("Image\Skelleton_Background_0.jpg").convert_alpha()
Ball2 = pygame.image.load("Image\Skelleton_Background_0.jpg").convert_alpha()
Ball3 = pygame.image.load("Image\Skelleton_Background_0.jpg").convert_alpha()
Heart = pygame.image.load("Image\LifeSkull.png").convert_alpha()

#get imports
from inputs import *
from elements import *
from collision import *
from functions import *

#run game
while running:
    t = pygame.time.get_ticks()
    for event in pygame.event.get():  # Get's all the user action (keyboard, mouse, joysticks, ...)
                continue
    
    #input  
    keys = pygame.key.get_pressed()
    if t - last_input_time > cooldown_time:
        last_input_time = t
        if keys[pygame.K_ESCAPE]: #kill command
                running = False
        if keys[pygame.K_TAB]:
            pygame.mixer.Sound('Audio\SICK_ASS_RIFF.mp3').play()
            game_state= 2
        if keys[pygame.K_SPACE]: 
            pygame.mixer.Sound('Audio\SICK_ASS_RIFF.mp3').play()
            health -= 1

    if game_state == 1:
        startscreen = pygame.transform.scale(startscreen, (WINDOW_X, WINDOW_Y))
        screen.blit(startscreen,(0,0))
        screen.blit(starttext,(0,0))

    if game_state == 2:
        background = pygame.transform.scale(background, (WINDOW_X, WINDOW_Y))
        screen.blit(background,(0,0))
        screen.blit(text,(t/50,30*np.sin(t/600)))

        #hp api
        for x in range(health):
            Heart = pygame.transform.scale(Heart, (WINDOW_X/10, WINDOW_Y/10))
            screen.blit(Heart,(0+50*x,WINDOW_Y-WINDOW_Y/5))

        if health <= 0: #checks hp
            game_state = 3 

    if game_state == 3:
        gameoverscreen = pygame.transform.scale(gameoverscreen, (WINDOW_X, WINDOW_Y))
        screen.blit(gameoverscreen,(0,0))
        screen.blit(gameovertext,(0,0))
    
    #Clocktick
    pygame.display.update()
    clock.tick(FPS) # 60 frames per second 

