import pygame
from body import NBody

running = True
pygame.init()

screen = pygame.display.set_mode([1280, 720], pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
pygame.display.set_caption('Physics Engine - v0.0.1')


clock = pygame.time.Clock()
camera = [0, 0]
camera_speed = 5

debug_font = pygame.font.SysFont('Arial', 12)



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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # position according to the camera
            pos = pygame.mouse.get_pos()
            pos = [pos[0] - camera[0], pos[1] - camera[1]]
            body = NBody(pos[0], pos[1])
            objects.append(body)
            # print "Body added repr"
            print("Body added: "+body.__repr__())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                objects = []
                print(r'Physics objects cleared.')
            if event.key == pygame.K_UP:
                simulation_speed += 0.1
            if event.key == pygame.K_DOWN:
                simulation_speed -= 0.1
                if simulation_speed < 0:
                    simulation_speed = 0
                
    # WASD camera movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        camera[1] += camera_speed
    if keys[pygame.K_s]:
        camera[1] -= camera_speed
    if keys[pygame.K_a]:
        camera[0] += camera_speed
    if keys[pygame.K_d]:
        camera[0] -= camera_speed

    delta = (clock.tick(60) / 1000) * simulation_speed # delta time in seconds
    # Update objects
    for obj in objects:
        obj.update(objects, delta)

   
    screen.fill((88, 85, 83)) # Clear screen
    # Drawing starts here ---

    for obj in objects:
        obj.draw(screen, camera)

    ## Drawing ends here ---

    # Debug information
    debug_text = debug_font.render(f'Camera: {camera}', True, (0, 0, 0))
    screen.blit(debug_text, (0, 0))
    # fps
    fps_text = debug_font.render(f'FPS: {round(clock.get_fps())}', True, (0, 0, 0))
    screen.blit(fps_text, (0, 15))
    # total number of objects
    obj_text = debug_font.render(f'Objects: {len(objects)}', True, (0, 0, 0))
    screen.blit(obj_text, (0, 30))
    # simulation speed
    sim_text = debug_font.render(f'Simulation speed: {simulation_speed}', True, (0, 0, 0))
    screen.blit(sim_text, (0, 45))
    # draw borders of 0x0 to 1280x720
    #pygame.draw.rect(screen, (255, 255, 255), (0+camera[0], 0+camera[1], 1280+camera[0], 720+camera[1]), 1)

    pygame.display.flip()
    clock.tick(60) # Update everything 30 times per second


pygame.quit()


