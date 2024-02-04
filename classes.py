import pygame
import math
import numpy as np

from constants import *
import variables
from functions import *

class Ball:
    def __init__(self, screen, skin, loss, radius, position, velocity, gravity):
        self._screen = screen
        self._skin = pygame.transform.scale(skin, (radius*2.1, radius*2.1))
        self._loss= loss
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
    def update_position(self):
        self._velocity[0] += self._gravity[0]
        self._velocity[1] += self._gravity[1]
        self._position[0] += self._velocity[0]
        self._position[1] += self._velocity[1]

    @staticmethod
    def change_score(Wert):
        variables.score = variables.score + Wert

    def collision_ball(self, ball): #vllt noch zu primitiv vllt noch geschw. berücksichtigen ect.
        distance = ((self._position[0] - ball.get_position()[0]) ** 2 + (self._position[1] - ball.get_position()[1]) ** 2) ** 0.5
        if distance <= self._radius + ball._radius:
            self._velocity[0] *= -1
            self._velocity[1] *= -1
            self.change_score(1)

    @staticmethod 
    def collision_checker(Ball_point, radius, Start_point, End_point, thickness):
        zähler = abs((End_point[0] - Start_point[0]) * (Start_point[1] - Ball_point[1]) + (Start_point[1] - End_point[1]) * (Start_point[0] - Ball_point[0]))
        nenner = math.sqrt((End_point[0] - Start_point[0])**2 + (End_point[1] - Start_point[1])**2)
        distance = zähler / nenner
        return distance <= (thickness/2 + radius) #maybe durch 2 für thickness machen idk

    def collision_line(self, obj):
        if self.collision_checker(self._position, self._radius, obj._position[0], obj._position[1], obj._size):
            self._velocity[0] = -(self._velocity[0] + obj._velocity[0]) * obj._bounce
            self._velocity[1] = -(self._velocity[1] + obj._velocity[1]) * obj._bounce
            if not (self._velocity[0] == 0  or self._velocity[1] ==0): #quick division 0 fix
                self._position[0] += 5 *(self._velocity[0]/abs(self._velocity[0]))  #bugfix to make some space between collision
                self._position[1] += 5 *(self._velocity[1]/abs(self._velocity[1]))  #bugfix to make some space between collision
            self.change_score(obj._points)

    def collision_window(self):  #needs to be last for ball to stay inside of window   #alternativ auch mit geschw. vektor richtung bestimmen und zukünfitge kollision prüfen #vllt besser für stationäre Grenzen
        if self._position[0] - self._radius < 0 or self._position[0] + self._radius > WINDOW_X:
            self._velocity[0] *= -1
            self._position[0] += 5 *(self._velocity[0]/abs(self._velocity[0]))  #bugfix to make some space between collision
        if self._position[1] - self._radius < 0 or self._position[1] + self._radius > WINDOW_Y:
            self._velocity[1] *= -1
            self._position[1] += 5 *(self._velocity[1]/abs(self._velocity[1]))  #bugfix to make some space between collision
            variables.score = variables.score + obj._points
    def draw(self):  #visualization
        self._screen.blit(self._skin,(self._position[0] - self._skin.get_width() // 2, self._position[1] - self._skin.get_height() // 2))    
        pygame.draw.circle(self._screen, (255, 255, 255), [self._position[0],self._position[1]] , self._radius,5)

class Line:
    def __init__(self, screen, color, size, bounce, points, position, velocity):
        self._screen = screen
        self._color = color
        self._size = size
        self._bounce = bounce
        self._points = points
        self._position = position
        self._velocity = velocity
    def get_position(self): 
        return self._position
    def get_velocity(self):
        return self._velocity
    def update_position(self):
        self._position[0][0] += self._velocity[0]
        self._position[1][0] += self._velocity[0]
        self._position[0][1] += self._velocity[1]
        self._position[1][1] += self._velocity[1]
    def draw(self):
        pygame.draw.line(self._screen, (255,255,255), self._position[0], self._position[1], self._size+5) #line in background for outline
        pygame.draw.line(self._screen, self._color, self._position[0], self._position[1], self._size)

class Rad_pic:
    def __init__(self, image, position,size, growth, growthtime):
        self._image= image
        self._position = position
        self._growth = growth
        self._growthtime = growthtime
        self._size = size
        self._image = pygame.transform.scale(self._image,(size[0],size[1]))
    def transform(self):
        self._position[0] = self._position[0]-self._growth*self._size[0]
        self._position[1] = self._position[1]-self._growth*self._size[1]
        self._size[0] =self._size[0] + self._growth*self._size[0]
        self._size[1] =self._size[1] + self._growth*self._size[1]
        self._image = pygame.transform.scale(self._image,(self._size[0], self._size[1]))
    def draw(self):
        screen.blit(self._image,(self._position[0],self._position[1]))

class Rad_txt:
    def __init__(self, text, position, velocity, shakyness):
        self._text = text
        self._position = position
        self._velocity = velocity
        self._shakyness = shakyness
    def update_position(self):
        self._position[0] += self._velocity[0]
        self._velocity[1] += self._velocity[1]
        self._position[1] += np.sin(self._velocity[1])* self._shakyness
    def draw(self):
        screen.blit(self._text, (self._position[0],self._position[1]))
    


#  screen, color, size, bounce, points, position[[][]], velocity[]
LINE1= Line(screen, (0,0,0), 50, 1, 1, [[0,650],[250,800]], [0,0])
LINE2= Line(screen, (0,0,0), 50, 1, 1, [[550,800],[800,650]], [0,0])
LINE3= Line(screen, (0,0,0), 50, 1, 1, [[0,700],[800,700]], [0,0])
LINE_LIST = ["here is flipper_L", "here is flipper_R", LINE1, LINE2, LINE3] #ersten zwei eintägen werden jeden Loop überarbeitet
