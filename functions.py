import pygame
import numpy as np


def read_highest_scores(): #reads out top 5 highscores
    output =[]
    scores = {}
    with open('Highscores.txt', 'r') as file:
        for line in file:
            name, score = line.strip().rsplit(' ', 1)
            scores[name] = int(score)
    
    # Sort
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # return the top 5 scores
    for name, score in sorted_scores[:5]:
        output.append([name,score])
    return output

def selection(input,length):
    return input % length 