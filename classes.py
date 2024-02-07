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

    def update_position(self): #update position due to speed, #update speed due to grav, # upda
        if self._velocity[0] > variables.max_x:
            self._velocity[0] = variables.max_x
        if self._velocity[1] > variables.max_y:
            self._velocity[1] = variables.max_y
        self._position[0] += self._velocity[0]
        self._position[1] += self._velocity[1]

    @staticmethod
    def change_score(Wert):
        variables.score = variables.score + Wert
    @staticmethod 
    def collision_checker(Ball_point, radius, Start_point, End_point, thickness): #only used for Line element collsision
        zähler = abs((End_point[0] - Start_point[0]) * (Start_point[1] - Ball_point[1]) + (Start_point[1] - End_point[1]) * (Start_point[0] - Ball_point[0]))
        nenner = math.sqrt((End_point[0] - Start_point[0])**2 + (End_point[1] - Start_point[1])**2)
        distance = zähler / nenner
        return distance <= (thickness/2 + radius) #maybe durch 2 für thickness machen idk
    
    def angle_between_points(self, ball): #return the angle  between two points by using a vector and skalar product, with x parallel vecotr of length 1
        connection_vector = pygame.math.Vector2( ball._position[0]-self._position[0] , ball._position[1]-self._position[1]) #relative vector 
        vector_length        = math.sqrt(connection_vector[0] ** 2 + connection_vector[1] ** 2)
        angle = np.arccos (vector_length / (connection_vector[0]+connection_vector[1]*0.001)) #ignor y component beacause v2= 1,0
        return angle

    def angle_between_line(self, line): #gets angle
        line_vector        = pygame.math.Vector2(line._position[0][0]-line._position[1][0] , line._position[0][1] -line._position[1][1])
        line_length        = math.sqrt(line_vector[0] ** 2 + line_vector[1] ** 2) 
        line_unit_vector   = pygame.math.Vector2(line_vector)/ line_length #fix here maybe
        line_normal_vector = pygame.math.Vector2(-line_unit_vector[1], line_unit_vector[0])
        velocity_vector    = pygame.math.Vector2(self._velocity[0],self._velocity[1])
        incident_angle     = (velocity_vector.angle_to(line_normal_vector)+90)* (np.pi/180)
        return incident_angle

    def collision_line(self, line): # regarding the angle reflects the ball
        if self.collision_checker(self._position, self._radius, line._position[0], line._position[1], line._size):
            angle = self.angle_between_line(line) 
            v_betrag = np.sqrt(self._velocity[0]**2 + self._velocity[1]**2)
            self._velocity[0] = (v_betrag * ( np.cos (angle)) + line._velocity[0]) * line._bounce 
            self._velocity[1] = (v_betrag * ( np.sin (angle)) + line._velocity[1]) * line._bounce
            v_betrag = np.sqrt(self._velocity[0]**2 + self._velocity[1]**2)
            self.update_position()
            self.change_score(line._points)

    def collision_ball(self, ball): #vllt noch zu primitiv , #macht nur einen impulsaustausch
        distance = ((self._position[0] - ball._position[0]) ** 2 + (self._position[1] - ball._position[1]) ** 2) ** 0.5
        if distance <= self._radius + ball._radius:
            v1= self._velocity[0]
            v2= self._velocity[1]
            self._velocity[0] = ball._velocity[0]
            self._velocity[1] = ball._velocity[1]
            ball._velocity[0] = v1
            ball._velocity[1] = v2
            self.update_position()
            ball.update_position()
            self.change_score(2)

    def collision_window(self):
        if (self._position[0] - self._radius) < 0: #left boarder
            self._velocity[0] *= -1
            self._position[0] = self._radius +5 #resets position to left boarder
        if (self._position[0] + self._radius) > WINDOW_X: #right boarder
            self._velocity[0] *= -1
            self._position[0] = WINDOW_X-self._radius - 5 #resets position to left boarder
            self.update_position()
            self.change_score(1)
        elif self._position[1] - self._radius < 0:  #top boarder
            self._velocity[1] *= -1
            self._position[1] = self._radius +5 #resets position to left boarder
            self.update_position()
            self.change_score(5)

    def gravity_update(self): #it works
        self._velocity[0] += self._gravity[0]
        self._velocity[1] += self._gravity[1]
        self.update_position()
    
    def draw(self):  #visualization
        self._screen.blit(self._skin,(self._position[0] - self._skin.get_width() // 2, self._position[1] - self._skin.get_height() // 2))    
        pygame.draw.circle(self._screen, (255, 255, 255), [self._position[0],self._position[1]] , self._radius,5)

class Line:
    def __init__(self, screen, color, size, bounce, points, position, velocity):
        self._screen = screen
        self._color  = color
        self._size   = size
        self._bounce = bounce
        self._points = points
        self._position = position
        self._velocity = velocity
    def update_position(self):
        self._position[0][0] +=  np.sin(self._velocity[0])*200
        self._position[1][0] +=  np.sin(self._velocity[0])*200
        self._position[0][1] +=  np.sin(self._velocity[1])*200
        self._position[1][1] +=  np.sin(self._velocity[1])*200
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
LINE1= Line(screen, (0,0,0), 50, 0.8, 1, [[0,650],[250,800]],   [0,0])
LINE2= Line(screen, (0,0,0), 50, 0.8, 1, [[550,800],[800,650]], [0,0])
LINE3= Line(screen, (0,0,0), 50, 1, 1,   [[0,800],[800,800]],   [0,0])
LINE_LIST = ["here is flipper_L", "here is flipper_R","here moving platform", LINE1, LINE2] #ersten zwei eintägen werden jeden Loop überarbeitet
