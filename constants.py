import pygame
import numpy as np

WINDOW_X = 800
WINDOW_Y = 900
screen   = pygame.display.set_mode([WINDOW_X, WINDOW_Y]) # essential
FPS      = 60 # frames per sec

#fonts
font1    = pygame.font.Font("Misc\WhoAsksSatan.ttf",50)
font2    = pygame.font.Font("Misc\MetalThorn.ttf",50)
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
BALLSKIN_LIST = [BALL1,BALL2,BALL3,BALL4]  # List of skins

radnesstext = font3.render("CHOOSE RADNESS LEVEL",False,"Red")
FIREWALL = pygame.image.load("Image\FIREWALL.jpg")
radnesswarning= font3.render("WARNING! OVERLOAD DETECTED",False,"Red")


#Play CONSTANTS
FIRE1 = pygame.transform.scale(pygame.image.load("Image\FIRE1.png"), (300, 100))
FIRE2 = pygame.transform.scale(pygame.image.load("Image\FIRE2.png"), (300, 100))
FIRE3 = pygame.transform.scale(pygame.image.load("Image\FIRE3.png"), (300, 100))
FIRE4 = pygame.transform.scale(pygame.image.load("Image\FIRE4.png"), (300, 100))
FIRELIST = [FIRE1,FIRE2,FIRE3,FIRE4] # List of frames for fire "animation"

#radness
SOUNDLIST    = ["Audio/EAGLE_SCREACH.mp3","Audio\HELL_YEAH.mp3","Audio\RAAAAH.mp3","Audio\SICK_ASS_RIFF.mp3"]
TEXTLIST     = ["HELL YEAH!","ROCK AND ROLL!", "RAW IRON", "FIRE!!!" , "LETS GO" , " U S A "]

#dynamics
GRAVITY = [0,1] #gravity in (x,y)
FLIPPER_LENGTH = 110

#End CONSTANTS
gameoverscreen = pygame.transform.scale(pygame.image.load("Image\END_SCREEN.webp").convert(), (WINDOW_X, WINDOW_Y))

record_txt       = font2.render ("RECORD YOUR LEGACY:",False,"Red")
highscore_txt    = font2.render ("HIGHSCORES:",False,"Red")

record_error_txt = font2.render ("SCORE ALREADY SUBMITTED:",False,"Red")
short_error_txt  = font2.render ("NAME TO SHORT!",False,"Red")
long_error_txt   = font2.render ("NAME TO LONG!",False,"Red")
submitted_txt    = font2.render ("SCORE SUBMITTED:",False,"Red")