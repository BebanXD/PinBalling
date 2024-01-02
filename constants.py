import pygame
from classes import *
import numpy as np


WINDOW_X = 800
WINDOW_Y = 900


#fonts
font2    = pygame.font.Font("Misc\MetalThorn.ttf",50)
font1    = pygame.font.Font("Misc\WhoAsksSatan.ttf",50)
font3    = pygame.font.Font("Misc\RythmOfDeath.ttf",60)
font4    = pygame.font.Font("Misc\RythmOfDeath.ttf",30)


#Start CONSTANTS
start_background = pygame.image.load("Image\START_SCREEN.jpg").convert()
stagetext = font3.render("CHOOSE YOUR STAGE",False,"Red")
stage1_background = pygame.image.load("Image\STAGE_1.webp").convert()
stage2_background = pygame.image.load("Image\STAGE_2.webp").convert()
ballstext = font3.render("CHOOSE YOUR BALLS",False,"Red")
BALL1 = pygame.transform.scale(pygame.image.load("Image\BALL_1.png"), (200, 200))
BALL2 = pygame.transform.scale(pygame.image.load("Image\BALL_2.png"), (250, 250))
BALL3 = pygame.transform.scale(pygame.image.load("Image\BALL_3.png"), (200, 200))
BALL4 = pygame.transform.scale(pygame.image.load("Image\BALL_4.png"), (200, 200))
radnesstext = font3.render("CHOOSE RADNESS LEVEL",False,"Red")
radnesswarning= font3.render("WARNING! OVERLOAD DETECTED",False,"Red")


#Play CONSTANTS
#radness
text = font1.render("HELL YEAH",False,"Red")
riff = pygame.mixer.Sound("Audio\SICK_ASS_RIFF.mp3").play

#rest
GRAVITY = 1

ball = Ball(radius=10, skin="Image\BALL_1.png", position=[0,0], velocity=[np.random.rand(), 5],gravity = GRAVITY)

#Shop CONSTANTS


#End CONSTANTS
gameoverscreen = pygame.image.load("Image\END_SCREEN.webp").convert()
gameoverscreen = pygame.transform.scale(gameoverscreen, (WINDOW_X, WINDOW_Y))

record_txt       = font2.render("Record your legacy:",False,"Red")
highscore_txt    = font2.render("HIGHSCORES:",False,"Red")
record_error_txt = font2.render("Score already submitted:",False,"Red")
submitted_txt    = font2.render("Score submitted:",False,"Red")
input_string        = ""
error_event_counter = 0
record_counter      = 1
submitted_counter   = 0