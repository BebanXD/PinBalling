import pygame
import sys #to quit properly
import numpy as np

#Game Basics
pygame.init()                   # essential
pygame.display.set_caption("PinBalling") # window name
pygame.display.set_icon(pygame.image.load("Image\PINBALLING_LOGO.jpeg")) #window icon
clock    = pygame.time.Clock()   # essential
WINDOW_X = 800
WINDOW_Y = 900
screen   = pygame.display.set_mode([WINDOW_X, WINDOW_Y]) # essential

#game variables

#get imports
from functions import *
from classes import *
from constants import *
from variables import *

#game variables
griddy  = True          # enables grid for testing
running = True      # while loop var.

sound_counter       = 0 # 0 to play music at start
game_state          = "play" #start play end
play_stage          = 1 # default set for quick testing

ball_type           = 0 # default set for quick testing # from 0 to 3
radness_level       = 5 # default set for quick testing # from 0 to 5
selection_phase     = 0
current_selected    = 0
counter             = 0
ballskin_list       = [BALL1,BALL2,BALL3,BALL4]
ballskin            = ballskin_list[0]

counter2            = 0
max_balls           = 3 #😏
availible_balls     = max_balls
ball_list           = []
left_trigger        = 0
right_trigger       = 0


#run game
while running:
    #loop based variables
    t = pygame.time.get_ticks() #current time
    keys = pygame.key.get_pressed()  # for holding key pressed, gives input all the time
    if keys[pygame.K_ESCAPE]: #kill command
        running = False
        break
    #---------------------------------------------------------------------------------------------------------------

    #sounds
    if game_state == "start" and sound_counter == 0:
        pygame.mixer.Sound('Audio\SONG.mp3').play()
        sound_counter = 1
    if game_state == "play" and sound_counter == 1:
        pygame.mixer.Sound('Audio\SONG.mp3').play()
        sound_counter = 2 
    if game_state == "end"  and sound_counter == 2:
        pygame.mixer.Sound('Audio\SONG_SAD.mp3').play() 


    #Start
    if game_state == "start": #select stage , select ball , select METELNESS level     
        screen.blit(start_background,(0,0))
        #stage select
        screen.blit(stagetext,(150,50))
        screen.blit(pygame.transform.scale(stage1_background, (250, 250)),(100, 150))
        screen.blit(pygame.transform.scale(stage2_background, (250, 250)),(450, 150))
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
    
        if ball_type == 0:
            pygame.draw.circle(screen, (255, 0, 0), (100, 600), 85, 5)
        if ball_type == 1:
            pygame.draw.circle(screen, (255, 0, 0), (300, 600), 85, 5)
        if ball_type == 2:
            pygame.draw.circle(screen, (255, 0, 0), (500, 600), 85, 5)
        if ball_type == 3:
            pygame.draw.circle(screen, (255, 0, 0), (700, 600), 85, 5)

        if selection_phase == 2:
            #FIREWALL2 = pygame.transform.scale(FIREWALL, (radness_level*(400-10)/4, 50-10))
            #screen.blit(FIREWALL2,(200, 800+5)) 
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
            ball_type = selection(current_selected,4)
            ballskin  = ballskin_list[ball_type]
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
        if left_trigger > -np.pi/4 :
            left_trigger  -= 0.05
        if right_trigger > -np.pi/4 :
            right_trigger -= 0.05

        #inputs
        for event in pygame.event.get(): #inputs
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #spawns ball if balls are left
                    if availible_balls > 0:    
                        ball_list.append(Ball(screen,ballskin,1,30,[500,500],[1,1],GRAVITY))
                        availible_balls -= 1
        if keys[pygame.K_LEFT] :
            if left_trigger < np.pi/4 :
                left_trigger += 0.5
        if keys[pygame.K_RIGHT]:
            if right_trigger < np.pi/4 :
                right_trigger += 0.5
        
        #Flippers
        LINE_LIST[0] = Line(screen, (255,255,255), 20, 1, 1, [[250,800],[250+FLIPPER_LENGTH*np.cos(-left_trigger) ,800+FLIPPER_LENGTH*np.sin(-left_trigger) ]], [0,0])#left
        LINE_LIST[1] = Line(screen, (255,255,255), 20, 1, 1, [[550,800],[550-FLIPPER_LENGTH*np.cos(-right_trigger),800+FLIPPER_LENGTH*np.sin(-right_trigger)]], [0,0])#right

        #background
        if play_stage == 1:
            screen.blit(stage1_background,(0,0))
        if play_stage == 2:
            screen.blit(stage2_background,(0,0))
        screen.blit(FIRELIST[(int(t/150))%4],(250,800))

        #draw all objects
        for x in range(len(LINE_LIST)): 
            LINE_LIST[x].draw()

        
        #ball handler
        for x in range(len(ball_list)):
            ball_list[x].update_position()
            for y in range(len(ball_list)):
                if y is not x: #dont check collision with self
                    ball_list[x].collision_ball(ball_list[y])
            for y in range(len(LINE_LIST)): #checks all rec collisions
                ball_list[x].collision_line(LINE_LIST[y])
                
            ball_list[x].collision_window()
            ball_list[x].draw()

            if (ball_list[x]._position[1]>850):
                ball_list.remove(ball_list[x]) #removes ball privilegs
                break

        #lose condition
        if (availible_balls==0) and (len(ball_list)==0):
            game_state = "end"

        #radness handler
        #missing content ?
            
        #UI Overlay
        for x in range(availible_balls): #balls ui
            screen.blit(pygame.transform.scale(pygame.image.load("Image\LifeSkull.png"), (70, 70)),(25,800-x*70))
        screen.blit(font3.render(f"{(variables.score)}",False,"Red"),(45,45))
        
        #---------------------------------------------------------------------------------------------------------------
       
    #End
    if game_state == "end": #shows endscreen and manages highscores over games
        
        #End Display
        gameover_txt = font3.render("Final Score: "+ str(score),False,"Red")
        input_txt    = font3.render(input_string,False,"White")

        #your score and input
        screen.blit(gameoverscreen, (0,0))
        screen.blit(gameover_txt,   (150,50))
        screen.blit(record_txt,     (150,100))
        screen.blit(input_txt,      (150,150))
        screen.blit(highscore_txt,      (150,400))
        if error_event_counter == 1:
            screen.blit(short_error_txt,(150,250))
        if error_event_counter == 2:
            screen.blit(long_error_txt,(150,250))
        if error_event_counter == 3:
            screen.blit(submitted_txt,(150,250))
        if error_event_counter == 4:
            screen.blit(record_error_txt,(150,250))


        #input for name into highscore list
        for event in pygame.event.get(): # for pressing key once
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_BACKSPACE) and (record_counter == 0):  #can only change if not submitted already
                    input_string = input_string[:-1]
                elif event.key == pygame.K_SPACE:
                    print() #does nothing #so no space is messing up the highscore function
                elif (event.key == pygame.K_KP_ENTER) or (event.key == pygame.K_RETURN):
                    if (len(input_string) == 0) :
                        error_event_counter = 1
                        break
                    if (len(input_string) > 15) :
                        error_event_counter = 2
                        break
                    elif record_counter == 0:
                        record_counter = 1
                        error_event_counter = 3 #eigentlich kein error aber egal
                        with open("Highscores.txt", "a") as file:
                            file.write(input_string + " " + str(score) + '\n')
                    else:
                         error_event_counter = 4
                         if radness_level == 5:  pygame.mixer.Sound('Audio\SICK_ASS_RIFF.mp3').play()  
                else:
                    if (record_counter == 0): #can only change if not submitted already
                        input_string += event.unicode  

        # top 5 highscores
        for x in range(len(read_highest_scores())):
            highscore_name_txt = font3.render(str(read_highest_scores()[x][0]),False,"Red")
            screen.blit(highscore_name_txt,  (150,450+x*50))
            highscore_value_txt = font3.render(str(read_highest_scores()[x][1]),False,"Red")
            screen.blit(highscore_value_txt, (600,450+x*50))
    #---------------------------------------------------------------------------------------------------------------
    
    #Gridview
    if griddy == True: #Grid Display 
        for y in range (50,WINDOW_Y+50,50):
            for x in range (50,WINDOW_X+50,50):
                screen.blit(font4.render(f"{(y)}",False,"Red"),(0,y))
                screen.blit(font4.render(f"{(x)}",False,"Red"),(x,0))
                pygame.draw.line(screen, (0, 0, 255), (0,y), (x,y),1)
                pygame.draw.line(screen, (0, 0, 255), (x,0), (x,y),1)
    #---------------------------------------------------------------------------------------------------------------

    # Clocktick
    pygame.display.flip() #is needed somehow,dont know what it does
    pygame.display.update()
    clock.tick(60) # 60 frames per second 

# Quit Pygame properly
pygame.quit()
sys.exit()