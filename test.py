import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rotating Lines")

# Set up line parameters
start_point = (width // 2, height // 2)
line_length = 100
line_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
rotation_speed = 0.02  # Adjust the rotation speed as needed

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Rotate and draw lines with variable thickness
    for i in range(len(line_colors)):
        thickness = int(2 + 2 * math.sin(pygame.time.get_ticks() * 0.002))  # Variable thickness
        angle = pygame.time.get_ticks() * rotation_speed
        end_point = (
            start_point[0] + int(line_length * math.cos(angle)),
            start_point[1] + int(line_length * math.sin(angle)),
        )
        pygame.draw.line(screen, line_colors[i], start_point, end_point, thickness)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(30)
