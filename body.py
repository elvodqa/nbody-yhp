import math
import random
import pygame


class NBody:
    def __init__(self, x, y, debug=True) -> None:
        self.x = x # Position x
        self.y = y # Position y
        self.vx = 0 # velocity x
        self.vy = 0 # velocity y
        self.ax = 0 # acceleration x
        self.ay = 0 # acceleration y
        self.density = 10 # density is introcuded,
        self.set_mass(100)
        self.color = (255, 255, 255) # Color of the planet in RGB format
        self.trails = [] # A list for drawing a trail behind the planet
        self.debug = debug # Debug mode for displaying trails and info
        if self.debug:
            self.info_font = pygame.font.SysFont('Arial', 11) # Load the font for displaying info
    
    def update(self, objects, G, delta):
        # Calculate acceleration
        for obj in objects:
            if obj == self:
                continue

            # Calculate distance between objects
            dx = obj.x - self.x # delta x: difference between x values
            dy = obj.y - self.y # delta y: difference between y values
            distance = (dx**2 + dy**2)**0.5 # Use pythagoras theorem

            # Calculate force
            if distance**2 == 0:
                distance = 0.1 # Temporary fix for division by zero  |  Newton's law of universal gravitation
            #G = 6.67408 * 10**-11 # Gravitational constant
            force = G * ((self.mass * obj.mass) / (distance**2))             # F = G * (m1 * m2) / r^2

            # Calculate acceleration
            self.ax += force * dx / distance # a = F / m
            self.ay += force * dy / distance # a = F / m

        # update acceleration and velocity with delta
        self.vx += self.ax * delta
        self.vy += self.ay * delta
        self.x += self.vx * delta
        self.y += self.vy * delta
        """
        # Update velocity
        self.vx += self.ax
        self.vy += self.ay

        # Update position
        self.x += self.vx
        self.y += self.vy

        # Reset acceleration
        self.ax = 0
        self.ay = 0
        """

        # if colliding and the other object is bigger, destory self
        for obj in objects:
            if obj == self:
                continue
            if self.is_colliding(obj):
                """
                if obj.radius > self.radius:
                    objects.remove(self)
                    print("Body removed: "+self.__repr__())
                if obj.radius < self.radius:
                    objects.remove(obj)
                    print("Body removed: "+obj.__repr__())
                if obj.radius == self.radius:
                    objects.remove(self)
                    objects.remove(obj)
                    print("Body removed: "+self.__repr__()+" and "+obj.__repr__())
                """
                return True
                    
        #self.trails.append((self.x, self.y))    
        # append trails every 10 px moved
        if self.debug:
            if len(self.trails) == 0 or (self.trails[-1][0] - self.x)**2 + (self.trails[-1][1] - self.y)**2 > 10**2:
                self.trails.append((self.x, self.y))        
        return False

    def draw(self, screen, camera):
        # Draw trails
        #for i in range(len(self.trails) - 1):
        #    pygame.draw.line(screen, self.color, (int(self.trails[i][0] + camera[0]), int(self.trails[i][1] + camera[1])), (int(self.trails[i+1][0] + camera[0]), int(self.trails[i+1][1] + camera[1])), 1)

        # Draw points leaving trails
        for trail in self.trails:
            pygame.draw.circle(screen, self.color, (trail[0] + camera[0], trail[1] + camera[1]), 1)

        pygame.draw.circle(screen, self.color, (self.x + camera[0], self.y + camera[1]), self.radius)
        
        if self.debug:
            # Draw info
            # mass
            info = self.info_font.render(f'{self.mass} kg', True, (255, 255, 255))
            screen.blit(info, (self.x + camera[0] - info.get_width() / 2, self.y + camera[1] - info.get_height() / 2))
            # velocity
            info = self.info_font.render(f'{self.vx:.2f} m/s', True, (255, 255, 255))
            screen.blit(info, (self.x + camera[0] - info.get_width() / 2, self.y + camera[1] - info.get_height() / 2 + 10))
            info = self.info_font.render(f'{self.vy:.2f} m/s', True, (255, 255, 255))
            screen.blit(info, (self.x + camera[0] - info.get_width() / 2, self.y + camera[1] - info.get_height() / 2 + 20))
            # acceleration
            info = self.info_font.render(f'{self.ax:.2f} m/s^2', True, (255, 255, 255))
            screen.blit(info, (self.x + camera[0] - info.get_width() / 2, self.y + camera[1] - info.get_height() / 2 + 30))
            info = self.info_font.render(f'{self.ay:.2f} m/s^2', True, (255, 255, 255))
            screen.blit(info, (self.x + camera[0] - info.get_width() / 2, self.y + camera[1] - info.get_height() / 2 + 40))
            # position
            info = self.info_font.render(f'{self.repr_pos()}', True, (255, 255, 255))
            screen.blit(info, (self.x + camera[0] - info.get_width() / 2, self.y + camera[1] - info.get_height() / 2 + 50))


    def __str__(self) -> str:
        return f'Physics object at ({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'Physics object at ({self.x}, {self.y})'
    
    def repr_pos(self) -> str:
        return f'Pos: ({int(self.x)}, {int(self.y)})'

    def is_colliding(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = (dx**2 + dy**2)**0.5
        return distance < self.radius + other.radius
    
    def set_mass(self, new_mass, realistic=True):
        self.mass = new_mass
        # density = mass / volume
        volume = self.mass / self.density
        # volume = 4/3 * pi * r^3
        if realistic:
            self.radius = (  (volume/((4/3)*math.pi))**1/3   ) / 10
        else:
            self.radius = math.log2(self.mass) * 2

    
