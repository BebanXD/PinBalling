import pygame
import numpy as np

import variables
from constants import *

def read_highest_scores(): #gives top highscore list
    output = []
    scores = {}
    with open('Highscores.txt', 'r') as file:
        for line in file:
            name, score = line.strip().rsplit(' ', 1)
            scores[name] = int(score)
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    if len(sorted_scores)<5:
        for name, score in sorted_scores:
            output.append([name,score])
        return output
    for name, score in sorted_scores[:5]:
        output.append([name,score])
    return output

def selection(input,length):
    return input % length 

def probability_per_second(percentage):
    random = np.random.rand()
    Bool = random < (percentage)/100 / FPS 
    return Bool