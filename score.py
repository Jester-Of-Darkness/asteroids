import pygame
from asteroid import Asteroid
from constants import *


class Score:
    def __init__(self):
        self.score = 0

    def points(self, asteroid_radius):

        if asteroid_radius == 20:
            self.score += 6
        elif asteroid_radius == 40:
            self.score += 12
        elif asteroid_radius == 60:
            self.score += 18

    def reset_score(self):
        self.score = 0





    