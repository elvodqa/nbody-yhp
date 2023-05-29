from body import NBody


def sun_and_planet():
    global objects 
    objects = []
    # sun object with big mass and radius at center
    sun = NBody(640, 360)
    sun.set_mass(10000)
    sun.color = (255, 255, 0)
    objects.append(sun)

    # planet with initial velocity near sun
    planet = NBody(640, 100)
    planet.vx = 0
    planet.vy = 1
    planet.set_mass(100)
    planet.color = (255, 255, 255)
    objects.append(planet)

    simulation_speed = 1
    
    return objects, simulation_speed

def sun_and_moon():
    global objects 
    objects = []
    # sun object with big mass and radius at center
    sun = NBody(640, 360)
    sun.set_mass(10000)
    sun.color = (255, 255, 0)
    objects.append(sun)

    # planet with initial velocity near sun
    planet = NBody(640, 100)
    planet.vx = 0
    planet.vy = 1
    planet.set_mass(100)
    planet.color = (255, 255, 255)
    objects.append(planet)

    # moon with initial velocity near planet
    moon = NBody(640, 150)
    moon.vx = 0
    moon.vy = 1.5
    moon.set_mass(10)
    moon.color = (255, 255, 255)
    objects.append(moon)

    simulation_speed = 1
    
    return objects, simulation_speed

def sun_and_2_planets():
    global objects 
    objects = []
    # sun object with big mass and radius at center
    sun = NBody(640, 360)
    sun.set_mass(10000)
    sun.color = (255, 255, 0)
    objects.append(sun)

    # planet with initial velocity near sun
    planet = NBody(640, 100)
    planet.vx = 0
    planet.vy = 1
    planet.set_mass(100)
    planet.color = (255, 255, 255)
    objects.append(planet)

    # moon with initial velocity near planet
    moon = NBody(640, 150)
    moon.vx = 0
    moon.vy = 1.5
    moon.set_mass(10)
    moon.color = (255, 255, 255)
    objects.append(moon)

    # moon with initial velocity near planet
    moon2 = NBody(640, 200)
    moon2.vx = 0
    moon2.vy = 2
    moon2.set_mass(10)
    moon2.color = (255, 255, 255)
    objects.append(moon2)

    simulation_speed = 1
    
    return objects, simulation_speed

def sun_and_3_planets():
    global objects 
    objects = []
    # sun object with big mass and radius at center
    sun = NBody(640, 360)
    sun.set_mass(10000)
    sun.color = (255, 255, 0)
    objects.append(sun)

    # planet with initial velocity near sun
    planet = NBody(640, 100)
    planet.vx = 0
    planet.vy = 1
    planet.set_mass(100)
    planet.color = (255, 255, 255)
    objects.append(planet)

    # moon with initial velocity near planet
    moon = NBody(640, 150)
    moon.vx = 0
    moon.vy = 1.5
    moon.set_mass(10)
    moon.color = (255, 255, 255)
    objects.append(moon)

    # moon with initial velocity near planet
    moon2 = NBody(640, 200)
    moon2.vx = 0
    moon2.vy = 2
    moon2.set_mass(10)
    moon2.color = (255, 255, 255)
    objects.append(moon2)

    # moon with initial velocity near planet
    moon3 = NBody(640, 250)
    moon3.vx = 0
    moon3.vy = 2.5
    moon3.set_mass(10)
    moon3.color = (255, 255, 255)
    objects.append(moon3)

    simulation_speed = 1
    
    return objects, simulation_speed
