import unittest
import pygame
from pygame.locals import *
from classes import Ball

class TestBall(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 900))
        self.ball = Ball(self.screen, pygame.image.load("ball.png"), 0.5, 20, (400, 500), (5, 5), (0, -9.8), (0, 0.5))

    def tearDown(self):
        pygame.quit()

    def test_ball_stays_in_window(self):
        self.ball._position = (-100, -100)
        self.ball.collision_window()
        self.assertTrue(self.ball._position[0] >= 0 and self.ball._position[0] <= 800)
        self.assertTrue(self.ball._position[1] >= 0 and self.ball._position[1] <= 900)

    def test_ball_velocity_reversed_on_window_collision(self):
        self.ball._position = (800, 900)
        self.ball.collision_window()
        self.assertEqual(self.ball._velocity[0], -self.ball._velocity[0])
        self.assertEqual(self.ball._velocity[1], -self.ball._velocity[1])

if __name__ == '__main__':
    unittest.main()