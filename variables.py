from constants import *

#overarching variables
running             = True      # while loop var.
griddy              = True   # enables grid for testing
game_state          = "play" #"start" or "play" or "end"
current_stage       = 1 # default set for quick testing
score               = 0 # tracks score #needed before classes are created
sound_counter       = 0 # 0 to play music at start

#start
ball_type           = 0 # default set for quick testing # from 0 to 3
radness_level       = 5 # default set for quick testing # from 0 to 5
selection_phase     = 0
current_selected    = 0
counter             = 0
counter2            = 0             
BALLSKIN_LIST       = [BALL1,BALL2,BALL3,BALL4]  # List of skins
ballskin            = BALLSKIN_LIST[0]    # keeps track of current balls in game

#play
max_balls           = 3 #😏
availible_balls     = max_balls     # keeps track of still availible balls
ball_list           = []            # keeps track of current balls in game
left_flipper        = 0             # position left flipper
right_flipper       = 0             # position right flipper
charge              = 0             # powermeter für Abschussrampe 
t_old               = 0             # time diff const, at point of ballspawn, for ball not to spawn

#radness variable
rad_txt_list        = []
rad_pic_list        = []


#end
input_string        = ""
error_event_counter = 0
record_counter      = 0

