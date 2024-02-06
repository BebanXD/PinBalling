import pygame
import sys
import math

# Initialisierung von Pygame
pygame.init()

# Bildschirmgröße
WIDTH, HEIGHT = 800, 600

# Farben
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Geschwindigkeit des Balls
velocity = [5, 5]

# Erstellen des Bildschirms
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball-Wand Kollision")

# Position und Radius des Balls
ball_radius = 30
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

# Definition der schrägen Wand
wall_start = (200, 200)
wall_end = (600, 500)

# Berechnen der Vektoren für die schräge Wand
wall_vector = (wall_end[0] - wall_start[0], wall_end[1] - wall_start[1])
wall_length = math.sqrt(wall_vector[0] ** 2 + wall_vector[1] ** 2)
wall_unit_vector = (wall_vector[0] / wall_length, wall_vector[1] / wall_length)

clock = pygame.time.Clock()

# Funktion zur Berechnung des einfallenden Winkels
def calculate_incident_angle(velocity, wall_unit_vector):
    velocity_vector    = pygame.math.Vector2(velocity)
    wall_normal_vector = pygame.math.Vector2(-wall_unit_vector[1], wall_unit_vector[0])
    incident_angle = velocity_vector.angle_to(wall_normal_vector)
    return incident_angle

# Funktion zur Berechnung der Distanz zwischen zwei Punkten
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Haupt-Loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Bewegung des Balls
    ball_x += velocity[0]
    ball_y += velocity[1]

    # Kollision mit den Wänden
    # Überprüfung der Kollision mit der schrägen Wand
    ball_vector = pygame.math.Vector2(ball_x - wall_start[0], ball_y - wall_start[1])
    dot_product = ball_vector.dot(wall_unit_vector)
    dot_product = max(0, min(dot_product, wall_length))
    closest_point = (wall_start[0] + dot_product * wall_unit_vector[0], wall_start[1] + dot_product * wall_unit_vector[1])

    if distance((ball_x, ball_y), closest_point) <= ball_radius:
        incident_angle = calculate_incident_angle(velocity, wall_unit_vector)
        velocity = pygame.math.Vector2(velocity).rotate(-2 * incident_angle)

    # Kollision mit den vertikalen Wänden
    if ball_x + ball_radius >= WIDTH or ball_x - ball_radius <= 0:
        velocity[0] = -velocity[0]  # Richtung umkehren

    # Kollision mit den horizontalen Wänden
    if ball_y + ball_radius >= HEIGHT or ball_y - ball_radius <= 0:
        velocity[1] = -velocity[1]  # Richtung umkehren

    # Zeichne den Ball
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

    # Zeichne die schräge Wand
    pygame.draw.line(screen, RED, wall_start, wall_end, 3)

    pygame.display.flip()
    clock.tick(60)