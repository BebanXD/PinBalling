import pygame
import math

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball and Circle Reflection")

# Define constants
BALL_RADIUS = 20
CIRCLE_RADIUS = 100
CIRCLE_CENTER = (screen_width // 2, screen_height // 2)

# Create Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS*2, BALL_RADIUS*2))
        self.image.fill(BLACK)
        pygame.draw.circle(self.image, WHITE, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 4, screen_height // 2)
        self.speed = 5
        self.angle = math.pi / 4  # Initial angle of motion

    def update(self):
        # Move the ball
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y += self.speed * math.sin(self.angle)
        
        # Check for collision with the circle
        if pygame.sprite.collide_rect(self, circle):
            # Calculate the angle of reflection
            dx = self.rect.centerx - CIRCLE_CENTER[0]
            dy = self.rect.centery - CIRCLE_CENTER[1]
            angle_to_center = math.atan2(dy, dx)
            self.angle = 2 * angle_to_center - self.angle
            
        # Check for collision with window walls
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.angle = math.pi - self.angle
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.angle = -self.angle

# Create Circle class
class Circle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((CIRCLE_RADIUS*2, CIRCLE_RADIUS*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (0, 0, 255, 100), (CIRCLE_RADIUS, CIRCLE_RADIUS), CIRCLE_RADIUS)
        self.rect = self.image.get_rect(center=CIRCLE_CENTER)

# Create sprites
ball = Ball()
circle = Circle()

all_sprites = pygame.sprite.Group()
all_sprites.add(ball, circle)

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
