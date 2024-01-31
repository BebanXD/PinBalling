import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tall Rectangle")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up rectangle
rect_width, rect_height = 50, 50
rect_x = (width - rect_width) // 2
rect_y = height - rect_height

# Set up clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update rectangle height
    rect_height += 1

    # Clear the screen
    screen.fill(black)

    # Draw rectangle
    pygame.draw.rect(screen, white, (rect_x, rect_y, rect_width, rect_height))

    # Update display
    pygame.display.flip()

    # Set frames per second
    clock.tick(30)
