import random
from body import NBody


def solar_system():
    global objects
    objects = []


    simulation_speed = 1
    return objects, simulation_speed


def galaxy_simulation():
    global objects 
    objects = []

    # every object is 1px in diameter. Thousands of stars scattered randomly
    for i in range(200):
        random_x = random.randint(0, 1280)
        random_y = random.randint(0, 600)
        if random_x > 1280/2:
            random_x += 100
        else:
            random_x -= 100
        if random_y > 600/2:
            random_y += 100
        else:
            random_y -= 100
        body = NBody(random_x, random_y, False)
        body.density = 1
        body.set_mass(random.randint(100, 300))
        #body.mass = 1

        body.radius = random.randint(1, 6)
        body.color = (255, 255, 255)
        objects.append(body)

    # Sun equivalent
    body = NBody(500, 500, False)
    body.density = 1.4
    body.set_mass(10000)
    body.color = (255, 255, 0)
    objects.append(body)

    simulation_speed = 0.1
    return objects, simulation_speed


def grid_3x3():
   # A 3x3 grid of planets with with random mass and density
    global objects
    objects = []
    #  * * *
    #  * * *
    #  * * *
    for i in range(3):
        for j in range(3):
            body = NBody(100 + i*300 + 210, 100 + j*300 - 70)
            body.set_mass(100)
            body.density = 1
            body.vx = 0
            body.vy = 0
            body.color = (255, 255, 255)
            objects.append(body)

    simulation_speed = 1

    return objects, simulation_speed

def star_cluster():
    global objects
    objects = []

    # 1px radius next to each other
    for i in range(20):
        for j in range(20):
            body = NBody(400+i+10, 400+j+10, False)
            body.mass = 100
            body.density = 1
            body.radius = 2
            body.vx = 0
            body.vy = 0
            body.color = (255, 255, 255)
            objects.append(body)
        
    simulation_speed = 0
    return objects, simulation_speed

def example_preset():
    global objects
    objects = []

    body = NBody(X, Y)
    body.density = 1
    body.set_mass(100)
    body.vx = 0
    body.vy = 0
    body.color = (255, 255, 255)
    objects.append(body)

    simulation_speed = 0.1
    return objects, simulation_speed
from math import sin, cos

def triple_ellipse_preset():
    global objects
    objects = []

    # Define the properties of the ellipses
    ellipse1_radius_x = 100
    ellipse1_radius_y = 200
    ellipse1_speed = 0.02

    ellipse2_radius_x = 150
    ellipse2_radius_y = 250
    ellipse2_speed = 0.03

    ellipse3_radius_x = 200
    ellipse3_radius_y = 300
    ellipse3_speed = 0.05

    # Define the number of bodies in each ellipse
    bodies_per_ellipse = 3

    # Create bodies for the first ellipse
    for i in range(bodies_per_ellipse):
        angle = i * (2 * 3.14159 / bodies_per_ellipse)
        body = NBody(0, 0)
        body.density = 1
        body.set_mass(10)
        body.vx = 0
        body.vy = 0
        body.color = (255, 0, 0)  # Red color for the first ellipse
        body.x = ellipse1_radius_x * cos(angle)
        body.y = ellipse1_radius_y * sin(angle)
        objects.append(body)

    # Create bodies for the second ellipse
    for i in range(bodies_per_ellipse):
        angle = i * (2 * 3.14159 / bodies_per_ellipse)
        body = NBody(0, 0)
        body.density = 1
        body.set_mass(10)
        body.vx = 0
        body.vy = 0
        body.color = (0, 255, 0)  # Green color for the second ellipse
        body.x = ellipse2_radius_x * cos(angle)
        body.y = ellipse2_radius_y * sin(angle)
        objects.append(body)

    # Create bodies for the third ellipse
    for i in range(bodies_per_ellipse):
        angle = i * (2 * 3.14159 / bodies_per_ellipse)
        body = NBody(0, 0)
        body.density = 1
        body.set_mass(10)
        body.vx = 0
        body.vy = 0
        body.color = (0, 0, 255)  # Blue color for the third ellipse
        body.x = ellipse3_radius_x * cos(angle)
        body.y = ellipse3_radius_y * sin(angle)
        objects.append(body)

    simulation_speed = 0.1
    return objects, simulation_speed

def orbit_two(G = 10):
    global objects
    objects = []
    mass=1000000
    rad=100

    body1 = NBody(1280/2, 720/2, True)
    body1.density = 1
    body1.set_mass(mass, False)
    body1.vx = 0
    body1.vy = 0
    body1.color = (255, 255, 255)
    objects.append(body1)

    body2 = NBody(1280/2, (720/2)+rad, True)
    body2.density = 1
    body2.set_mass(100, False)
    body2.vx = (G*mass/rad)**0.5
    body2.vy = 0
    body2.color = (255, 255, 255)
    objects.append(body2)

    simulation_speed = 0.1
    return objects, simulation_speed

def orbit_three(G = 10):
    global objects
    objects = []

    mass=1000000
    rad=100

    body1 = NBody(1280/2, 720/2, True)
    body1.density = 1
    body1.set_mass(mass, False)
    body1.vx = 0
    body1.vy = 0
    body1.color = (255, 255, 255)
    objects.append(body1)

    body2 = NBody(1280/2, (720/2)+rad, True)
    body2.density = 1
    body2.set_mass(100, False)
    body2.vx = (G*mass/rad)**0.5
    body2.vy = 0
    body2.color = (255, 255, 255)
    objects.append(body2)

    body3 = NBody(1280/2, (720/2)+(2*rad), True)
    body3.density = 1
    body3.set_mass(100, False)
    body3.vx = -(G*mass/(rad*2))**0.5
    body3.vy = 0
    body3.color = (255, 255, 255)
    objects.append(body3)

    simulation_speed = 0.1
    return objects, simulation_speed

def orbit_four(G=10):
    global objects
    objects = []

    mass=1000000
    rad=100

    body1 = NBody(1280/2, 720/2, True)
    body1.density = 1
    body1.set_mass(mass, False)
    body1.vx = 0
    body1.vy = 0
    body1.color = (255, 255, 255)
    objects.append(body1)

    body2 = NBody(1280/2, (720/2)+rad, True)
    body2.density = 1
    body2.set_mass(100, False)
    body2.vx = (G*mass/rad)**0.5
    body2.vy = 0
    body2.color = (255, 255, 255)
    objects.append(body2)

    body3 = NBody(1280/2, (720/2)+(2*rad), True)
    body3.density = 1
    body3.set_mass(100, False)
    body3.vx = -(G*mass/(rad*2))**0.5
    body3.vy = 0
    body3.color = (255, 255, 255)
    objects.append(body3)

    body4 = NBody(1280/2, (720/2)+(3*rad), True)
    body4.density = 1
    body4.set_mass(100, False)
    body4.vx = 0
    body4.vy = (G*mass/(rad*3))**0.5
    body4.color = (255, 255, 255)
    objects.append(body4)

    simulation_speed = 0.1
    return objects, simulation_speed

def ducati_three(G = 10):
    global objects
    objects = []

    mass=1000000
    rad=100

    body1 = NBody(0, -0.070946548000287 * 100, True)
    body1.density = 1
    body1.set_mass(mass, False)
    body1.vx = -1.231870762148251 * 100
    body1.vy = 0
    body1.color = (255, 255, 255)
    objects.append(body1)

    body2 = NBody(0, 1.075903540029147 * 100, True)
    body2.density = 1
    body2.set_mass(mass, False)
    body2.vx = 0.195089035291636 * 100
    body2.vy = 0
    body2.color = (255, 255, 255)
    objects.append(body2)

    body3 = NBody(0, -1.004956992028862 * 100, True)
    body3.density = 1
    body3.set_mass(mass, False)
    body3.vx = 1.036781726856616 * 100
    body3.vy = 0
    body3.color = (255, 255, 255)
    objects.append(body3)

    simulation_speed = 0.1
    return objects, simulation_speed

def sun_earth_moon(G = 10):
    global objects
    objects = []
    mass=1000000
    rad=300

    body1 = NBody(1280/2, 720/2, True)
    body1.density = 1
    body1.set_mass(mass, False)
    body1.vx = 0
    body1.vy = 0
    # yellow
    body1.color = (255, 255, 0)
    objects.append(body1)

    body2 = NBody(1280/2, (720/2)+rad, True)
    body2.density = 1
    body2.set_mass(1000, False)
    body2.radius = 5
    body2.vx = (G*mass/rad)**0.5
    body2.vy = 0
    # blue
    body2.color = (0, 150, 200)
    objects.append(body2)

    body3 = NBody(1280/2, (720/2)+rad+10, True)
    body3.density = 1
    body3.set_mass(10, False)
    body3.radius = 2
    rad = 10
    body3.vx = (G*body2.mass/rad)**0.5 + body2.vx
    body3.vy = 0
    body3.color = (255, 255, 255)
    objects.append(body3)
    simulation_speed = 0.1
    return objects, simulation_speed

