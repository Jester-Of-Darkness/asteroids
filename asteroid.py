import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity=pygame.Vector2(0, 0)):
        super().__init__(x, y, radius, velocity)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_vel_1 = self.velocity.rotate(angle) * 1.2
        new_vel_2 = self.velocity.rotate(-angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius, new_vel_1)
        Asteroid(self.position.x, self.position.y, new_radius, new_vel_2)


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2 )

    def update(self, dt):
        self.position += self.velocity * dt