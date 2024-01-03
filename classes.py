import pygame
import numpy as np

#tripple copy
WINDOW_X = 800
WINDOW_Y = 900

class Ball:
    def __init__(self, screen, skin, radius, position, velocity, gravity):
        self._screen = screen
        self._skin = pygame.transform.scale(skin, (radius*2.1, radius*2.1))
        self._radius = radius
        self._position = position 
        self._velocity = velocity
        self._gravity = gravity
        self._counter = 0
    # access data
    def get_position(self):
        return self._position
    def get_velocity(self):
        return self._velocity
    # run follwoing every loop 
    def update_position(self):
        self._velocity[0] += self._gravity[0]
        self._velocity[1] += self._gravity[1]
        self._position[0] += self._velocity[0]
        self._position[1] += self._velocity[1]
    def collision_ball(self, ball): #vllt noch zu primitiv vllt noch geschw. berücksichtigen ect.
        distance = ((self._position[0] - ball.get_position()[0]) ** 2 + (self._position[1] - ball.get_position()[1]) ** 2) ** 0.5
        if distance <= self._radius + ball._radius:
            self._velocity[0] *= -1
            self._velocity[1] *= -1
    def collision_rect(self, rect):
        x_location  = self._radius + self._position[0]
        y_location  = self._radius + self._position[1]
        x_intervall = [rect._position[0],rect._position[0]+rect._size[0]]
        y_intervall = [rect._position[1],rect._position[1]+rect._size[1]]
        if ((x_intervall[0]<=x_location) and (x_intervall[1]>=x_location)) and ((y_intervall[0]<=y_location) and (y_intervall[1]>=y_location)):
            self._velocity[0] *= -1
            self._velocity[1] *= -1
    def collision_window(self):  #needs to be last for ball to stay inside of window   #alternativ auch mit geschw. vektor richtung bestimmen und zukünfitge kollision prüfen #vllt besser für stationäre Grenzen
        if self._position[0] - self._radius < 0 or self._position[0] + self._radius > WINDOW_X:
            self._velocity[0] *= -1
        if self._position[1] - self._radius < 0 or self._position[1] + self._radius > WINDOW_Y:
            self._velocity[1] *= -1
    def draw(self):
        self._screen.blit(self._skin,(self._position[0] - self._skin.get_width() // 2, self._position[1] - self._skin.get_height() // 2))    
        pygame.draw.circle(self._screen, (255, 255, 255), [self._position[0],self._position[1]] , self._radius,5)
    def deletion(self):
        del self

class Rect:
    def __init__(self, screen, color, size, position, velocity):
        self._screen = screen
        self._color = color
        self._size = size
        self._position = position
        self._velocity = velocity
    # access data
    def get_position(self):
        return self._position
    def get_size(self):
        return self._size
    def get_velocity(self):
        return self._velocity
    # run follwoing every loop 
    def update_position(self):
        self._position[0] += self._velocity[0]
        self._position[1] += self._velocity[1]
    def draw(self):
        pygame.draw.rect(self._screen, self._color, (self._position, self._size))
