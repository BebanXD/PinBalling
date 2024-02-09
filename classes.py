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

    def update_position(self): #update position due to speed, #caps max speed
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
    def betrag(x,y): #einfache drehmatrix
        return np.sqrt(x**2 +y**2) 
    @staticmethod
    def transformation_x(x,y,angle): #einfache drehmatrix
        return x*np.cos(angle) + y*np.sin(angle)
    @staticmethod
    def transformation_y(x,y,angle): #einfache drehmatrix
        return x*np.sin(angle) - y*np.cos(angle)
    @staticmethod
    def angle_checker(x, y):
        theta = np.arctan(np.abs(y)/np.abs(x))  # Compute the angle in radians
        if x < 0 and y > 0:
            theta =  np.pi - theta
        if x <= 0 and y <= 0: # vllt bie größer gleich hier fehler
            theta = theta + np.pi
        if x > 0 and y < 0:
            theta =  np.pi *2 -theta
        return theta   # Convert radians to degrees

    def collision_checker(self, line): #uses drehmatrix to turn until the line is parallel to the x axis
        if self.betrag(line._position[0][0],line._position[0][1]) < self.betrag(line._position[1][0],line._position[1][1]): #shortest vector becomes x1
            x1 = line._position[0][0]
            y1 = line._position[0][1]
            angle = self.angle_checker  (line._position[1][0]-x1,line._position[1][1]-y1)
            x2_t = self.transformation_x(line._position[1][0]-x1,line._position[1][1]-y1,angle) #x end intervall
            y2_t = self.transformation_y(line._position[1][0]-x1,line._position[1][1]-y1,angle) #y end intervall
        else: #if the end vector of line is smaller, the  intervall is limited by the startingvektor
            x1 = line._position[1][0]
            y1 = line._position[1][1]
            angle = self.angle_checker  (line._position[0][0]-x1,line._position[0][1]-y1)
            x2_t = self.transformation_x(line._position[0][0]-x1,line._position[0][1]-y1,angle) #x end intervall
            y2_t = self.transformation_y(line._position[0][0]-x1,line._position[0][1]-y1,angle) #y end intervall
        x_t = self.transformation_x(self._position[0]-x1,self._position[1]-y1,angle) # x transformed
        y_t = self.transformation_y(self._position[0]-x1,self._position[1]-y1,angle) # y transformed
        if ((x_t + self._radius) > 0)  and ((x_t- self._radius) < x2_t ): #checks if x coord. is in intevall 
            if ((y_t+ self._radius) > (0 -line._size/2))  and ((y_t - self._radius) < (y2_t + line._size/2)): #checks if y coord. is in  the intevall
                return True

    def angle_between_line(self, line): #gets angle
        line_vector        = pygame.math.Vector2(line._position[0][0]-line._position[1][0] , line._position[0][1] -line._position[1][1])
        line_length        = math.sqrt(line_vector[0] ** 2 + line_vector[1] ** 2) 
        line_unit_vector   = pygame.math.Vector2(line_vector)/ line_length #fix here maybe
        line_normal_vector = pygame.math.Vector2(-line_unit_vector[1], line_unit_vector[0])
        velocity_vector    = pygame.math.Vector2(self._velocity[0],self._velocity[1])
        incident_angle     = (velocity_vector.angle_to(line_normal_vector))* (np.pi/180)
        #print(incident_angle /(np.pi/180))
        return incident_angle
    
    def collision_line(self, line): # regarding the angle reflects the ball
        if self.collision_checker(line):
            angle = self.angle_between_line(line) 
            if True: # no collision on edges of lines
                v_betrag = np.sqrt(self._velocity[0]**2 + self._velocity[1]**2)
                self._velocity[0] = (v_betrag * ( -np.sin (angle)) + line._velocity[0]) * line._bounce 
                self._velocity[1] = (v_betrag * ( np.cos (angle))  + line._velocity[1]) * line._bounce
                self.update_position()
                if self.collision_checker(line):
                    self._position[0] += (10 * (-np.sin (angle))) #bugfix so it doesnt collide with the flippers twice
                    self._position[1] += (10 * ( np.cos (angle))) #bugfix so it doesnt collide with the flippers twice
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
            self.update_position()
            self.change_score(2)
        if (self._position[0] + self._radius) > WINDOW_X: #right boarder
            self._velocity[0] *= -1
            self._position[0] = WINDOW_X-self._radius - 5 #resets position to left boarder
            self.update_position()
            self.change_score(2)
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
        pygame.draw.line(self._screen,   self._color, self._position[0], self._position[1], self._size)

class Rad_txt:
    def __init__(self, text, position, velocity, ):
        self._text = text
        self._position = position
        self._og_position_y = position
        self._velocity = velocity
    def update_position(self):
        self._position[0] += self._velocity[0]
    def draw(self):
        screen.blit(self._text, (self._position[0],self._position[1]))
    

#  screen, color, size, bounce, points, position[[][]], velocity[]
LINE1= Line(screen, (0,0,0), 50, 0.8, 1, [[0,650],[250,800]],   [0,0])
LINE2= Line(screen, (0,0,0), 50, 0.8, 1, [[550,800],[800,650]], [0,0])
LINE_LIST = ["here is flipper_L", "here is flipper_R","here moving platform", LINE1, LINE2] #ersten zwei eintägen werden jeden Loop überarbeitet
