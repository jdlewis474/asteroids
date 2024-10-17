import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        x_pos = self.position[0]
        y_pos = self.position[1]
        split_angle = random.uniform(20,50)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child_1 = Asteroid(x_pos, y_pos, child_radius)
        child_2 = Asteroid(x_pos, y_pos, child_radius)
        child_1.velocity = self.velocity.rotate(split_angle) * 1.2
        child_2.velocity = self.velocity.rotate(split_angle * -1) * 1.2