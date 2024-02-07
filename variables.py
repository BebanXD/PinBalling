from constants import *

#overarching variables
running             = True   # while loop var.
griddy              = True   # enables grid for testing
game_state          = "start" #"start" or "play" or "end"
current_stage       = 1      # default set for quick testing
score               = 0      # tracks score #needed before classes are created
sound_counter       = 0      # 0 to play music at start #3 to play no music

#start
ball_type           = 0                         # default set for quick testing # from 0 to 3
radness_level       = 5                         # default set for quick testing # from 0 to 5
selection_phase     = 0                         # current stage of selection
current_selected    = 0                         # holds the position of the red box
counter             = 0                         # tracks selection progress
counter2            = 0                         # makes tracks sound  when radness is selected to level 5          
BALLSKIN_LIST       = [BALL1,BALL2,BALL3,BALL4] # List of skins
ballskin            = BALLSKIN_LIST[0]          # keeps track of current balls in game

#play
max_balls           = 5             # max amounts of balls #normal 3
availible_balls     = max_balls     # keeps track of still availible balls
extra_balls_counter = 1000          # starting point for when to get an extra ball
ball_list           = []            # keeps track of current balls in game
left_flipper        = 0             # position left flipper
right_flipper       = 0             # position right flipper
charge              = 0             # powermeter für Abschussrampe 
t_old               = 0             # time diff const, at point of ballspawn, for ball not to spawn
max_x               = 15            # eig const
max_y               = 15            # eig const

#radness variable
rad_txt_list        = []    # carries all the flying text
rad_pic_list        = []    # carries all the apearing pictures


#end
input_string        = ""    # input name
error_event_counter = 0     # tracks with error has occured, and should be displayed
record_counter      = 0     # tracks if the name has already been written to file

