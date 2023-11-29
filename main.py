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
bg_orig=pygame.image.load(Path(__file__).parents[0] / Path("bkg.jpg")).convert()
clock = pygame.time.Clock()

# Setup 
running = True

# You could declare components (the initial ball, the other items, ...) here

ball_x = 100
ball_y = 150
ball_vx = 0
ball_vy = 0

ball_radius = 30

ball2_x = 200
ball2_y = 150
ball2_vx = 0
ball2_vy = 0

ball2_radius = 40


# Main event loop
while running:
    for event in pygame.event.get():
        # Get's all the user action (keyboard, mouse, joysticks, ...)
        continue

    # Adjust screen
    s_width, s_height = screen.get_width(), screen.get_height()
    bg = pygame.transform.scale(bg_orig, (s_width, s_height))
    screen.blit(bg, (0, 0)) # redraws background image


    # Here the action could take place

    # s = s0 + v0*t + 1/2a*t**2

    ball_vy = ball_vy + GRAVITY_Y*DT
    ball2_vy = ball2_vy + GRAVITY_Y*DT

    if ball_y >= screen.get_height():
        ball_vy = ball_vy * (-1)
    if ball2_y >= screen.get_height():
        ball2_vy = ball2_vy * (-1)

    ball_y = ball_y + ball_vy*DT + 0.5 * GRAVITY_Y*DT**2
    ball2_y = ball2_y + ball2_vy*DT + 0.5 * GRAVITY_Y*DT**2

    pygame.draw.circle(screen, (35, 161, 224), [ball_x,ball_y] , ball_radius)
    pygame.draw.circle(screen, (35, 161, 224), [ball2_x,ball2_y] , ball2_radius)


    pygame.display.flip() # Update the display of the full screen
    clock.tick(60) # 60 frames per second

# Done! Time to quit.
