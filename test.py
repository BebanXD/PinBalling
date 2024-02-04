import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Growing Picture")

# Load the image
image_path = "Image\RANDOM_1.jpg"  # Replace with the actual path to your image
original_image = pygame.image.load(image_path)
image_rect = original_image.get_rect()

# Initial scale and position
scale_factor = 1.0
x, y = (width - image_rect.width) // 2, (height - image_rect.height) // 2

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Increase the scale factor gradually
    scale_factor += 0.01

    # Resize the image
    scaled_image = pygame.transform.scale(original_image, (int(image_rect.width * scale_factor),
                                                            int(image_rect.height * scale_factor)))

    # Update the position
    x = (width - scaled_image.get_width()) // 2
    y = (height - scaled_image.get_height()) // 2

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the scaled image on the screen
    screen.blit(scaled_image, (x, y))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)

# Quit Pygame (this will never be reached in this infinite loop)
pygame.quit()
