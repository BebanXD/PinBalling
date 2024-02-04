#import modules
import pygame
import sys #to quit properly
import numpy as np

#Game Init
pygame.init()                   # essential #needs to happen before constants import
pygame.mixer.init()             # for sound managment
pygame.display.set_caption("PinBalling") # window name
pygame.display.set_icon(pygame.image.load("Image\PINBALLING_LOGO.jpeg")) #window icon
clock    = pygame.time.Clock()   # essential

#import files
from constants import *
import variables 
from functions import *
from classes   import *

#run game
while variables.running:
    #loop based variables
    t = pygame.time.get_ticks() #current time
    keys = pygame.key.get_pressed()  # for holding key pressed, gives input all the time

    #close game
    if keys[pygame.K_ESCAPE]: #kill command
        variables.running = False
        break
    #---------------------------------------------------------------------------------------------------------------

    #music
    if variables.game_state ==("play" or "start")and variables.sound_counter == 0:
        pygame.mixer.music.load('Audio\SONG.mp3')
        pygame.mixer.music.play()
        variables.sound_counter = 1
    if variables.game_state == "end"  and variables.sound_counter == 1:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('Audio\SONG_SAD.mp3')
        pygame.mixer.music.play()
        variables.sound_counter = 0
    #---------------------------------------------------------------------------------------------------------------    
    
    #Start
    if variables.game_state == "start": #select stage , select ball , select METELNESS level     
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
        if variables.current_stage == 1:
            pygame.draw.rect(screen, (255, 0, 0), (100, 150, 250, 250), 5)
        if variables.current_stage == 2:
            pygame.draw.rect(screen, (255, 0, 0), (450, 150, 250, 250), 5)
    
        if variables.ball_type == 0:
            pygame.draw.circle(screen, (255, 0, 0), (100, 600), 85, 5)
        if variables.ball_type == 1:
            pygame.draw.circle(screen, (255, 0, 0), (300, 600), 85, 5)
        if variables.ball_type == 2:
            pygame.draw.circle(screen, (255, 0, 0), (500, 600), 85, 5)
        if variables.ball_type == 3:
            pygame.draw.circle(screen, (255, 0, 0), (700, 600), 85, 5)

        if variables.selection_phase == 2:
            #FIREWALL2 = pygame.transform.scale(FIREWALL, (radness_level*(400-10)/4, 50-10))
            #screen.blit(FIREWALL2,(200, 800+5)) 
            pygame.draw.rect(screen, (0, 0, 0), (200+5, 800+5, variables.radness_level*(400-10)/4, 50-10))
        if variables.radness_level == 5:
            screen.blit(radnesswarning,(50,700))
            if variables.counter2 == 0: # so it makes a sound everytime the treshold is reached
                variables.counter2 += 1
                pygame.mixer.Sound('Audio\SICK_ASS_RIFF.mp3').play() 
        else:
            screen.blit(radnesstext,(150,700))
            variables.counter2 = 0


        #input
        for event in pygame.event.get(): #inputs
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE) or (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER):
                    variables.selection_phase += 1
                elif event.key == pygame.K_LEFT:
                    variables.current_selected -= 1
                elif event.key == pygame.K_RIGHT:
                    variables.current_selected += 1

        #selection phases
        if variables.selection_phase == 0: #stage select
            variables.current_stage = selection(variables.current_selected,2) + 1
        elif variables.selection_phase == 1: #balls select
            if variables.counter == 0: #resets selection to 0 once
                variables.current_selected = 0
                variables.counter += 1
            variables.ball_type = selection(variables.current_selected,4)
            variables.ballskin  = BALLSKIN_LIST[variables.ball_type]
        elif variables.selection_phase == 2: #radness select
            if variables.counter == 1: #resets selection to 0 once
                variables.current_selected = 0
                variables.counter += 1 
            variables.radness_level = selection(variables.current_selected,6)
        elif variables.selection_phase == 3:
            variables.game_state ="play"
    #---------------------------------------------------------------------------------------------------------------

    #Game
    if variables.game_state == "play": # main game
        if variables.left_flipper> -np.pi/4 :
            variables.left_flipper -= 0.05
        if variables.right_flipper > -np.pi/4 :
            variables.right_flipper -= 0.05
        if variables.charge > 0:
            variables.charge -= 1

        #inputs
        for event in pygame.event.get(): #inputs
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER)  : #spawns ball if balls are left
                    if (variables.availible_balls > 0) and t > variables.t_old + 120 :    
                        variables.ball_list.append(Ball(screen,variables.ballskin,1,30,[500,500],[0,-variables.charge/4],GRAVITY))
                        variables.availible_balls -= 1
                        variables.t_old=t
                if (event.key == pygame.K_SPACE): #boosts ball inital speed
                    if variables.charge < 100:
                        variables.charge += 10
        if keys[pygame.K_LEFT] :
            if variables.left_flipper< np.pi/4 :
                variables.left_flipper+= 0.5
        if keys[pygame.K_RIGHT]:
            if variables.right_flipper < np.pi/4 :
                variables.right_flipper += 0.5
        
        #Flippers
        LINE_LIST[0] = Line(screen, (255,255,255), 20, 1, 1, [[250,800],[250+FLIPPER_LENGTH*np.cos(-variables.left_flipper) ,800+FLIPPER_LENGTH*np.sin(-variables.left_flipper) ]], [0,0])#left
        LINE_LIST[1] = Line(screen, (255,255,255), 20, 1, 1, [[550,800],[550-FLIPPER_LENGTH*np.cos(-variables.right_flipper),800+FLIPPER_LENGTH*np.sin(-variables.right_flipper)]], [0,0])#right

        #background
        if variables.current_stage == 1:
            screen.blit(stage1_background,(0,0))
        if variables.current_stage == 2:
            screen.blit(stage2_background,(0,0))
        screen.blit(FIRELIST[(int(t/150))%4],(250,800))

        #draw all objects
        for x in range(len(LINE_LIST)): 
            LINE_LIST[x].draw()

        
        #ball handler
        for x in range(len(variables.ball_list)):
            variables.ball_list[x].update_position()
            for y in range(len(variables.ball_list)):
                if y is not x: #dont check collision with self
                    variables.ball_list[x].collision_ball(variables.ball_list[y])
            for y in range(len(LINE_LIST)): #checks all rec collisions
                variables.ball_list[x].collision_line(LINE_LIST[y])
                
            variables.ball_list[x].collision_window()
            variables.ball_list[x].draw()

            if (variables.ball_list[x]._position[1]>850):
                variables.ball_list.remove(variables.ball_list[x]) #removes ball privilegs
                break

        #lose condition
        if (variables.availible_balls==0) and (len(variables.ball_list)==0):
            variables.game_state = "end"

        #UI Overlay
        for x in range(variables.availible_balls): #balls ui
            screen.blit(pygame.transform.scale(pygame.image.load("Image\LifeSkull.png"), (70, 70)),(25,800-x*70))
        screen.blit(font3.render(f"{(variables.score)}",False,"Red"),(45,45))
        pygame.draw.rect(screen, (0, 0, 0),   (700-5, 875-(2*100)-5, 50+10, 400+10), 5) #chargemeter background
        pygame.draw.rect(screen, (255, 0, 0), (700, 875-(2*variables.charge), 50, 4*variables.charge)) #chargemeter

        #radness handler
        if variables.radness_level > 0:
            if variables.radness_level:
                #text
                if probability_per_second(variables.radness_level**2):
                    x = t%len(TEXTLIST)
                    variables.rad_txt_list.append(Rad_txt(font3.render(TEXTLIST[x],False,"Red"),[-300,(np.random.rand()*WINDOW_Y)],[2+np.random.rand()*10,0],np.random.rand()*100))
                #image
                if probability_per_second(variables.radness_level**2):
                    x = t%len(IMAGELIST)
                    variables.rad_pic_list.append(Rad_pic(pygame.image.load(IMAGELIST[x]),[np.random.rand()*WINDOW_X,np.random.rand()*WINDOW_X],[50,50],0.1,t+(2+np.random.rand()*5)*600))
                #sound
                if probability_per_second(variables.radness_level**2):
                    x = t%len(SOUNDLIST)
                    pygame.mixer.Sound(SOUNDLIST[x]).play()

        for x in range(len(variables.rad_pic_list)):
            variables.rad_pic_list[x].transform
            variables.rad_pic_list[x].draw()
            if t > variables.rad_pic_list[x]._growthtime : #removes after out of screen to safe memory
                variables.rad_pic_list.remove(variables.rad_pic_list[x])
                break
           
        for x in range(len(variables.rad_txt_list)):
            variables.rad_txt_list[x].draw()
            variables.rad_txt_list[x].update_position()
            if variables.rad_txt_list[x]._position[0] > WINDOW_X: #removes after out of screen to safe memory
                variables.rad_txt_list.remove(variables.rad_txt_list[x])
                break
        #---------------------------------------------------------------------------------------------------------------
       
    #End
    if variables.game_state == "end": #shows endscreen and manages highscores over games
        
        #End Display
        gameover_txt = font3.render("Final Score: "+ str(variables.score),False,"Red")
        input_txt    = font3.render(variables.input_string,False,"White")

        #your score and input
        screen.blit(gameoverscreen, (0,0))
        screen.blit(gameover_txt,   (150,50))
        screen.blit(record_txt,     (150,100))
        screen.blit(input_txt,      (150,150))
        screen.blit(highscore_txt,      (150,400))
        if variables.error_event_counter == 1:
            screen.blit(short_error_txt,(150,250))
        if variables.error_event_counter == 2:
            screen.blit(long_error_txt,(150,250))
        if variables.error_event_counter == 3:
            screen.blit(submitted_txt,(150,250))
        if variables.error_event_counter == 4:
            screen.blit(record_error_txt,(150,250))

        
        #input for name into highscore list
        for event in pygame.event.get(): # for pressing key once
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_BACKSPACE) and (variables.record_counter == 0):  #can only change if not submitted already
                    variables.input_string = variables.input_string[:-1]
                elif event.key == pygame.K_SPACE:
                    print() #does nothing #so no space is messing up the highscore function
                elif (event.key == pygame.K_KP_ENTER) or (event.key == pygame.K_RETURN):
                    if (len(variables.input_string) == 0) :
                        variables.error_event_counter = 1
                        break
                    if (len(variables.input_string) > 15) :
                        variables.error_event_counter = 2
                        break
                    elif variables.record_counter == 0:
                        variables.record_counter = 1
                        variables.error_event_counter = 3 #eigentlich kein error aber egal
                        with open("Highscores.txt", "a") as file:
                            file.write(variables.input_string + " " + str(variables.score) + '\n')
                    else:
                         variables.error_event_counter = 4
                         if variables.radness_level == 5:  pygame.mixer.Sound('Audio\SICK_ASS_RIFF.mp3').play()  
                else:
                    if (variables.record_counter == 0): #can only change if not submitted already
                        variables.input_string += event.unicode  

        # top 5 highscores
        for x in range(len(read_highest_scores())):
            highscore_name_txt = font3.render(str(read_highest_scores()[x][0]),False,"Red")
            screen.blit(highscore_name_txt,  (150,450+x*50))
            highscore_value_txt = font3.render(str(read_highest_scores()[x][1]),False,"Red")
            screen.blit(highscore_value_txt, (600,450+x*50))
    #---------------------------------------------------------------------------------------------------------------
    
    #Gridview
    if variables.griddy == True: #Grid Display 
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
    clock.tick(FPS) # 60 frames per second 

# Quit Pygame properly
pygame.quit()
sys.exit()