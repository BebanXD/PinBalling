import pygame
import sys #to quit properly
import numpy as np
from pathlib import Path

#Game Basics
pygame.init()                   # essential
pygame.display.set_caption("PinBalling") # window name
pygame.display.set_icon(pygame.image.load("Image\PINBALLING_LOGO.jpeg")) #window icon
clock    = pygame.time.Clock()   # essential
WINDOW_X = 800
WINDOW_Y = 900
screen   = pygame.display.set_mode([WINDOW_X, WINDOW_Y]) # essential

#get imports
from functions import *
from classes import *
from constants import *

#game variables
griddy = 0          # enables grid for testing
running = True      # while loop var.
score   = 0         # tracks score

game_state          = "play"
play_stage          = 1 # default set for quick testing
ball_type           = 1 # default set for quick testing
radness_level       = 5 # default set for quick testing
selection_phase     = 0
current_selected    = 0
counter             = 0
counter2            = 0

balls_remaining     = 3

#run game
while running:
    #loop based variables
    t = pygame.time.get_ticks() #current time
    keys = pygame.key.get_pressed()  # for holding key pressed, gives input all the time
    if keys[pygame.K_ESCAPE]: #kill command
        running = False
        break
    #---------------------------------------------------------------------------------------------------------------

    #Start
    if game_state == "start": #select stage , select ball , select METELNESS level
        start_background = pygame.transform.scale(start_background, (WINDOW_X, WINDOW_Y))
        screen.blit(start_background,(0,0))
        #stage select
        screen.blit(stagetext,(150,50))
        stage1_background = pygame.transform.scale(stage1_background, (250, 250))
        screen.blit(stage1_background,(100, 150))
        stage2_background = pygame.transform.scale(stage2_background, (250, 250))
        screen.blit(stage2_background,(450, 150))    
        #ball select
        screen.blit(ballstext,(150,450))
        screen.blit(BALL1,(100 - BALL1.get_width() // 2, 600 - BALL1.get_height() // 2))    
        screen.blit(BALL2,(300 - BALL2.get_width() // 2, 600 - BALL2.get_height() // 2))    
        screen.blit(BALL3,(500 - BALL3.get_width() // 2, 600 - BALL3.get_height() // 2))    
        screen.blit(BALL4,(700 - BALL4.get_width() // 2, 600 - BALL4.get_height() // 2))    
        #radness select
        pygame.draw.rect(screen, (255, 0, 0), (200, 800, 400, 50), 5)

        #conditional display
        if play_stage == 1:
            pygame.draw.rect(screen, (255, 0, 0), (100, 150, 250, 250), 5)
        if play_stage == 2:
            pygame.draw.rect(screen, (255, 0, 0), (450, 150, 250, 250), 5)
    
        if ball_type == 1:
            pygame.draw.circle(screen, (255, 0, 0), (100, 600), 85, 5)
        if ball_type == 2:
            pygame.draw.circle(screen, (255, 0, 0), (300, 600), 85, 5)
        if ball_type == 3:
            pygame.draw.circle(screen, (255, 0, 0), (500, 600), 85, 5)
        if ball_type == 4:
            pygame.draw.circle(screen, (255, 0, 0), (700, 600), 85, 5)

        if selection_phase == 2:
            pygame.draw.rect(screen, (0, 0, 0), (200+5, 800+5, radness_level*(400-10)/4, 50-10))
        if radness_level == 5:
            screen.blit(radnesswarning,(50,700))
            if counter2 == 0: # so it makes a sound everytime the treshold is reached
                counter2 += 1
                pygame.mixer.Sound('Audio\SICK_ASS_RIFF.mp3').play() 
        else:
            screen.blit(radnesstext,(150,700))
            counter2 = 0


        #input
        for event in pygame.event.get(): #inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    selection_phase += 1
                elif event.key == pygame.K_LEFT:
                    current_selected -= 1
                elif event.key == pygame.K_RIGHT:
                    current_selected += 1

        #selection phases
        if selection_phase == 0: #stage select
            play_stage = selection(current_selected,2) + 1
        elif selection_phase == 1: #balls select
            if counter == 0: #resets selection to 0 once
                current_selected = 0
                counter += 1
            ball_type = selection(current_selected,4) + 1
        elif selection_phase == 2: #radness select
            if counter == 1: #resets selection to 0 once
                current_selected = 0
                counter += 1 
            radness_level = selection(current_selected,6)
        elif selection_phase == 3:
            game_state ="play"
        
    #---------------------------------------------------------------------------------------------------------------

    #Game
    if game_state == "play": # main game
        #radness_handler(radness_level)


        #variables
        



        if play_stage == 1:
            stage1_background = pygame.transform.scale(stage1_background, (WINDOW_X, WINDOW_Y))
            screen.blit(stage1_background,(0,0))

        if play_stage == 2:
            stage2_background = pygame.transform.scale(stage2_background, (WINDOW_X, WINDOW_Y))
            screen.blit(stage2_background,(0,0))
        
    #---------------------------------------------------------------------------------------------------------------
       
    #End
    if game_state == "end": #shows endscreen and manages highscores over games
        
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
                    print() #does nothing #so no space is messing up the highscore function
                elif event.key == pygame.K_KP_ENTER:
                    if(len(input_string) == 0 ):
                        print("enter")
                    elif record_counter == 1:
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
    #---------------------------------------------------------------------------------------------------------------
    
    if griddy == True: #Grid Display 
        for y in range (50,WINDOW_Y+50,50):
            for x in range (50,WINDOW_X+50,50):
                screen.blit(font4.render(f"{(y)}",False,"Red"),(0,y))
                screen.blit(font4.render(f"{(x)}",False,"Red"),(x,0))
                pygame.draw.line(screen, (0, 0, 255), (0,y), (x,y),3)
                pygame.draw.line(screen, (0, 0, 255), (x,0), (x,y),3)

    # Clocktick
    pygame.display.update()
    clock.tick(60) # 60 frames per second 

# Quit Pygame properly
pygame.quit()
sys.exit()