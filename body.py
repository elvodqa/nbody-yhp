import math
import random
import pygame


class NBody:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.vx = 0 # velocity x / y
        self.vy = 0
        self.ax = 0 # acceleration x / y
        self.ay = 0

        self.density = 10 # density is introcuded
        self.set_mass(100)
        # radius according to mass
        self.radius = self.mass**(1/3) * 10
        self.color = (255, 255, 255)
    
    def update(self, objects, delta):
        # Calculate acceleration
        for obj in objects:
            if obj == self:
                continue

            # Calculate distance between objects
            dx = obj.x - self.x # delta x: difference between x values
            dy = obj.y - self.y # delta y: difference between y values
            distance = (dx**2 + dy**2)**0.5 # Use pythagoras theorem

            # Calculate force
            force = (self.mass * obj.mass) / (distance**2) # F = G * (m1 * m2) / r^2

            # Calculate acceleration
            self.ax += force * dx / distance # a = F / m
            self.ay += force * dy / distance # a = F / m

        # Update velocity
        self.vx += self.ax
        self.vy += self.ay

        # Update position
        self.x += self.vx * delta
        self.y += self.vy * delta

        # Reset acceleration
        self.ax = 0
        self.ay = 0

        # if colliding and the other object is bigger, destory self
        for obj in objects:
            if obj == self:
                continue
            if self.is_colliding(obj):
                if obj.radius > self.radius:
                    objects.remove(self)
                    print("Body removed: "+self.__repr__())
                if obj.radius < self.radius:
                    objects.remove(obj)
                    print("Body removed: "+obj.__repr__())
                if obj.radius == self.radius:
                    self.play_explasion_effect(objects, self.x, self.y, self.color)
                    self.play_explasion_effect(objects, obj.x, obj.y, obj.color)
                    objects.remove(self)
                    objects.remove(obj)
                    print("Body removed: "+self.__repr__()+" and "+obj.__repr__())
                    # Create a new particle for each pixel

    def draw(self, screen, camera):
        pygame.draw.circle(screen, self.color, (int(self.x + camera[0]), int(self.y + camera[1])), self.radius)

    def __str__(self) -> str:
        return f'Physics object at ({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'Physics object at ({self.x}, {self.y})'

    def is_colliding(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = (dx**2 + dy**2)**0.5
        return distance < self.radius + other.radius
    
    def set_mass(self, new_mass):
        self.mass = new_mass
        # density = mass / volume
        volume = self.mass / self.density
        # volume = 4/3 * pi * r^3
        self.radius = (  (volume/((4/3)*math.pi))**1/3   ) / 10

    def play_explasion_effect(self, objects, x, y, color):
        # Create a new particle for each pixel
        for i in range(3):
            # Create a new particle
            particle = NBody(x, y)
            particle.color = color
            particle.set_mass(100)
            particle.vx = (random.random() - 0.5) * 10
            particle.vy = (random.random() - 0.5) * 10
            # randomize x and y by 1-10 pixels
            particle.x += (random.random() - 0.5) * 10
            particle.y += (random.random() - 0.5) * 10

            objects.append(particle)