import pygame
import sys #to quit properly
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
WINDOW_X = 800
WINDOW_Y = 950
screen   = pygame.display.set_mode([WINDOW_X, WINDOW_Y]) # essential

#game variables
running = True      # while loop var.
game_state = "end"      # check postion of screen
score   = 0         # tracks score
health  = 3

#time
FPS = 60
t   = 0
dt  = 1

last_input_time = 0
cooldown_time   = 200

#Start CONSTANTS
start_background = pygame.image.load("Image\Skelleton_Background_0.jpg").convert()

starttext = font3.render("CHOOSE YOUR BALLS",False,"Red")

#Play CONSTANTS
play_background = pygame.image.load("Image\Skelleton_Background_2.webp").convert()
text = font1.render("HELL YEAH",False,"Red")
Ball1 = pygame.image.load("Image\Skelleton_Background_0.jpg").convert_alpha()
Ball2 = pygame.image.load("Image\Skelleton_Background_0.jpg").convert_alpha()
Ball3 = pygame.image.load("Image\Skelleton_Background_0.jpg").convert_alpha()
Heart = pygame.image.load("Image\LifeSkull.png").convert_alpha()

#Shop SONSTANTS
shop_background = pygame.image.load("Image\Skelleton_Background_3.webp").convert()


#End CONSTANTS
gameoverscreen = pygame.image.load("Image\GAME_OVER_SCREEN.webp").convert()
gameoverscreen = pygame.transform.scale(gameoverscreen, (WINDOW_X, WINDOW_Y))
record_txt       = font2.render("Record your legacy:",False,"Red")
highscore_txt    = font2.render("HIGHSCORES:",False,"Red")
record_error_txt = font2.render("Score already submitted:",False,"Red")
submitted_txt    = font2.render("Score submitted:",False,"Red")
input_string        = ""
error_event_counter = 0
record_counter      = 1
submitted_counter   = 0


#get imports
from elements import *
from collision import *
from functions import *

#run game
while running:
    t = pygame.time.get_ticks()
    
    #input
    keys = pygame.key.get_pressed()  # for holding key pressed, gives input all the time
    if t - last_input_time > cooldown_time: #
        last_input_time = t
        if keys[pygame.K_ESCAPE]: #kill command
                running = False
        if keys[pygame.K_TAB]:
            game_state= 3
        if keys[pygame.K_SPACE]: 
            score += 1


    #Start
    if game_state == "start":
        start_background = pygame.transform.scale(start_background, (WINDOW_X, WINDOW_Y))
        screen.blit(start_background,(0,0))

    #Game
    if game_state == "play":
        play_background = pygame.transform.scale(play_background, (WINDOW_X, WINDOW_Y))
        screen.blit(play_background,(0,0))
        screen.blit(text,(t/50,30*np.sin(t/600)))


    #Shop
    if game_state == "shop":
        screen.blit(starttext,(0,0))


    #End
    if game_state == "end": #shows endscreen and manages highscores
        
        #End Display
        gameover_txt = font2.render("Final Score: "+ str(score),False,"Red")
        input_txt    = font2.render(input_string,False,"Red")

        #your score and input
        screen.blit(gameoverscreen, (0,0))
        screen.blit(gameover_txt,   (0,50))
        screen.blit(record_txt,     (0,100))
        screen.blit(input_txt,      (0,150))
        screen.blit(highscore_txt,      (0,400))
        if error_event_counter:
            submitted_counter = 0
            screen.blit(record_error_txt,(0,250))
        if submitted_counter:
            screen.blit(submitted_txt,(0,250))

        #input for name into highscore list
        for event in pygame.event.get(): # for pressing key once
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_string = input_string[:-1]
                elif event.key == pygame.K_SPACE:
                    print() #does nothing
                elif event.key == pygame.K_KP_ENTER:
                    if record_counter:
                        record_counter = 0
                        with open("Highscores.txt", "a") as file:
                            file.write(input_string + " " + str(score) + '\n')
                        submitted_counter = 1
                    else:
                         error_event_counter = 1   
                else:
                    input_string += event.unicode  
        
        # top ten highscores
        for x in range(len(read_highest_scores())):
            highscore_name_txt = font3.render(str(read_highest_scores()[x][0]),False,"Red")
            screen.blit(highscore_name_txt,  (0,450+x*50))
            highscore_value_txt = font3.render(str(read_highest_scores()[x][1]),False,"Red")
            screen.blit(highscore_value_txt, (400,450+x*50))
        
    
    # Clocktick
    pygame.display.update()
    clock.tick(FPS) # 60 frames per second 

# Quit Pygame properly
pygame.quit()
sys.exit()