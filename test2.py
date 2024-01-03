import pygame
from pathlib import Path

# Initialize PyGame
pygame.init()

# Initial window size
s_width = 600
s_height = 800

# Define spacetime 
GRAVITY_X = 0.0
GRAVITY_Y = 0.3
DT = 1 # ms (discretization of time) 

# Making display screen
screen = pygame.display.set_mode((s_width, s_height), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Setup 
running = True

# You could declare components (the initial ball, the other items, ...) here

# Main event loop
while running:
    for event in pygame.event.get():
        # Get's all the user action (keyboard, mouse, joysticks, ...)
        continue

        pygame.display.flip() # Update the display of the full screen
    clock.tick(60) # 60 frames per second

# Done! Time to quit.
