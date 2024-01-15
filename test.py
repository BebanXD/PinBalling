import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Example')

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Rectangle properties
rect_width = 50
rect_height = 50
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2
rect_speed = 5
selection_phase =0
current_selected =1
# Game Loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen with a white background

    for event in pygame.event.get(): #inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                selection_phase += 1
            elif event.key == pygame.K_LEFT:
                current_selected -= 1
            elif event.key == pygame.K_RIGHT:
                current_selected += 1
    print(current_selected)
    # Keep the rectangle within the screen bounds


    # Draw the rectangle
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
