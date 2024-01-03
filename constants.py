import pygame
import numpy as np
from classes import Rect

#double mentioned
WINDOW_X = 800
WINDOW_Y = 900
screen   = pygame.display.set_mode([WINDOW_X, WINDOW_Y]) # essential

#fonts
font2    = pygame.font.Font("Misc\MetalThorn.ttf",50)
font1    = pygame.font.Font("Misc\WhoAsksSatan.ttf",50)
font3    = pygame.font.Font("Misc\RythmOfDeath.ttf",60)
font4    = pygame.font.Font("Misc\RythmOfDeath.ttf",30)


#Start CONSTANTS
start_background = pygame.transform.scale(pygame.image.load("Image\START_SCREEN.jpg").convert(), (WINDOW_X, WINDOW_Y))

stagetext = font3.render("CHOOSE YOUR STAGE",False,"Red")
stage1_background = pygame.transform.scale(pygame.image.load("Image\STAGE_1.webp").convert(), (WINDOW_X, WINDOW_Y))
stage2_background = pygame.transform.scale(pygame.image.load("Image\STAGE_2.webp").convert(), (WINDOW_X, WINDOW_Y))

ballstext = font3.render("CHOOSE YOUR BALLS",False,"Red")
BALL1 = pygame.transform.scale(pygame.image.load("Image\BALL_1.png"), (200, 200))
BALL2 = pygame.transform.scale(pygame.image.load("Image\BALL_2.png"), (250, 250))
BALL3 = pygame.transform.scale(pygame.image.load("Image\BALL_3.png"), (200, 200))
BALL4 = pygame.transform.scale(pygame.image.load("Image\BALL_4.png"), (200, 200))

radnesstext = font3.render("CHOOSE RADNESS LEVEL",False,"Red")
FIREWALL = pygame.image.load("Image\FIREWALL.jpg")
radnesswarning= font3.render("WARNING! OVERLOAD DETECTED",False,"Red")


#Play CONSTANTS
#radness
text = font1.render("HELL YEAH",False,"Red")
riff = pygame.mixer.Sound("Audio\SICK_ASS_RIFF.mp3").play

#rest
GRAVITY = [0,1]


rec1 = Rect(screen, (0, 255, 0), (100, 50), [400, 300], [0, 0])
rec2 = Rect(screen, (0, 255, 0), (300, 100), [500, 200], [0, 0])
REC_LIST1 =[rec1,rec2]
REC_LIST2 =[rec1,rec2]



#End CONSTANTS
gameoverscreen = pygame.transform.scale(pygame.image.load("Image\END_SCREEN.webp").convert(), (WINDOW_X, WINDOW_Y))

record_txt       = font2.render("Record your legacy:",False,"Red")
highscore_txt    = font2.render("HIGHSCORES:",False,"Red")
record_error_txt = font2.render("Score already submitted:",False,"Red")
submitted_txt    = font2.render("Score submitted:",False,"Red")
input_string        = ""
error_event_counter = 0
record_counter      = 1
submitted_counter   = 0