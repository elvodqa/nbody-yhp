import pygame
import pygame_gui
from body import NBody
from presets import sun_and_planet, sun_and_moon, sun_and_2_planets, sun_and_3_planets

running = True
pygame.init()

screen = pygame.display.set_mode([1280, 720], pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
pygame.display.set_caption('Physics Engine - v0.0.1')

manager = pygame_gui.UIManager((1280, 720))


clock = pygame.time.Clock()
camera = [0, 0]
camera_speed = 5

debug_font = pygame.font.SysFont('Arial', 12)



global objects 
objects = []

simulation_speed = 1


clear_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1120, 0), (160, 50)),
                                            text='Clear Bodies',
                                            manager=manager)
speed_slider_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1120, 40), (160, 30)),
                                            text='Simulation Speed',
                                            manager=manager)

speed_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((1120, 60), (160, 50)),
                                            start_value=simulation_speed,
                                            value_range=(0, 500),
                                            manager=manager)
speed_slider.set_current_value = 100
preset_selection_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1120, 100), (160, 30)),
                                            text='Presets',
                                            manager=manager)

preset_selection = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((1120, 120), (160, 200)),
                                            item_list=['Sun and planet', 'Sun and moon', 'Sun and 2 planets', 'Sun and 3 planets'],
                                            manager=manager)

def clear_objects():
    objects = []
    print(r'Physics objects cleared.')

while running:
    body_delta = (clock.tick(60) / 1000) * simulation_speed
    time_delta = (clock.tick(60) / 1000)
    for event in pygame.event.get():
        manager.process_events(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # right button
            if event.button == 3:
                # position according to the camera
                pos = pygame.mouse.get_pos()
                pos = [pos[0] - camera[0], pos[1] - camera[1]]
                body = NBody(pos[0], pos[1])
                objects.append(body)
                # print "Body added repr"
                print("Body added: "+body.__repr__())
        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_UP:
                simulation_speed += 0.1
            if event.key == pygame.K_DOWN:
                simulation_speed -= 0.1
                if simulation_speed < 0:
                    simulation_speed = 0
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == clear_button:
                    clear_objects()
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == speed_slider:
                simulation_speed = event.value / 100
                print(f'Simulation speed: {simulation_speed}')
        if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
            if event.ui_element == preset_selection:
                clear_objects()
                if event.text == 'Sun and planet':
                    objects, simulation_speed = sun_and_planet()
                elif event.text == 'Sun and moon':
                    objects, simulation_speed = sun_and_moon()
                elif event.text == 'Sun and 2 planets':
                    objects, simulation_speed = sun_and_2_planets()
                elif event.text == 'Sun and 3 planets':
                    objects, simulation_speed = sun_and_3_planets()
                else:
                    print('No preset selected.')
                print(f'Simulation speed: {simulation_speed}')
                print(f'Objects: {objects}')

                
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

    manager.update(time_delta)
    # Update objects
    for obj in objects:
        obj.update(objects, body_delta)

    
    screen.fill((88, 85, 83)) # Clear screen
    # Drawing starts here ---

    for obj in objects:
        obj.draw(screen, camera)
    manager.draw_ui(screen)
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


