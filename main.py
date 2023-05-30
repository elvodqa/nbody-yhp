import pygame
import pygame_gui
from body import NBody
from presets import solar_system, grid_3x3, galaxy_simulation, star_cluster, triple_ellipse_preset

running = True
pygame.init()

screen = pygame.display.set_mode([1280, 720], pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
pygame.display.set_caption('Physics Engine - v0.0.1')

manager = pygame_gui.UIManager((1280, 720))


clock = pygame.time.Clock()
camera = [0, 0]
camera_speed = 10

debug_font = pygame.font.SysFont('Arial', 12)



global objects 
objects = []

simulation_speed = 1

body_mass = 100
body_density = 1
body_color = (255, 255, 255)
G_constant = 1 # 6.67408e-11


clear_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1120, 0), (160, 50)),
                                            text='Clear Bodies',
                                            manager=manager)
speed_slider_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1120, 40), (160, 30)),
                                            text='Simulation Speed',
                                            manager=manager)

speed_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((1120, 60), (160, 50)),
                                            start_value=simulation_speed,
                                            value_range=(0, 1000),
                                            manager=manager)
speed_slider.set_current_value = 100
preset_selection_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1120, 100), (160, 30)),
                                            text='Presets',
                                            manager=manager)

preset_selection = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((1120, 120), (160, 200)),
                                            item_list=['Solar system', '3x3 grid', 'Galaxy', 'Cluster', 'Triple Ellipse'],
                                            manager=manager)

current_bodies = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((1120, 320), (160, 200)),
                                            item_list=objects,
                                            manager=manager)

# body config
body_mass_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1120, 520), (160, 30)),
                                            text='Body Mass',
                                            manager=manager)

body_mass_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((1120, 540), (160, 30)),
                                            manager=manager)
body_mass_input.set_text(str(body_mass))

body_density_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1120, 570), (160, 30)),
                                            text='Body Density',
                                            manager=manager)

body_density_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((1120, 590), (160, 30)),
                                            manager=manager)
body_density_input.set_text(str(body_density))
body_color_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1120, 620), (160, 30)),
                                            text='Body Color (R,G,B)',
                                            manager=manager)

body_color_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((1120, 640), (160, 30)),
                                            manager=manager)
body_color_input.set_text(str(body_color))

g_constant_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((1120, 680), (160, 30)),
                                            manager=manager)
g_constant_input.set_text(str(G_constant))
g_constant_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1120, 660), (160, 30)),
                                            text='G Constant',
                                            manager=manager)


radius_mode = pygame_gui.elements.UISelectionList(relative_rect=pygame.Rect((1120-160, 30), (160, 46)),
                                            item_list=['Realistic', 'Log2'],
                                            manager=manager)
radius_mode_text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((1120-160, 0), (160, 30)),
                                            text='Radius Mode',
                                            manager=manager)
radius_mode_val = 'Realistic'
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
                body.density = body_density
                body.color = body_color
                if radius_mode_val == 'Log2':
                    body.set_mass(body_mass, False)
                if radius_mode_val == 'Realistic':
                    body.set_mass(body_mass, True)
                objects.append(body)
                print("Body added: "+body.__repr__())
                objs = []
                for obj in objects:
                    objs.append(obj.repr_pos())
                current_bodies.set_item_list(objs)

        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_UP:
                simulation_speed += 0.1
            if event.key == pygame.K_DOWN:
                simulation_speed -= 0.1
                if simulation_speed < 0:
                    simulation_speed = 0

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == clear_button:
                    objects = []
                    objs = []
                    for obj in objects:
                        objs.append(obj.repr_pos())
                    current_bodies.set_item_list(objs)
                    print(r'Physics objects cleared.')
        
        if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
            if event.ui_element == speed_slider:
                simulation_speed = event.value / 100
                print(f'Simulation speed: {simulation_speed}')

        if event.type == pygame_gui.UI_SELECTION_LIST_NEW_SELECTION:
            if event.ui_element == radius_mode:
                if event.text == 'Realistic':
                    radius_mode_text = 'Realistic'
                    for obj in objects:
                        obj.set_mass(obj.mass, True)
                if event.text == 'Log2':
                    radius_mode_text = 'Log2'
                    for obj in objects:
                        obj.set_mass(obj.mass, False)
                print(f'Radius mode: 1')
            
            if event.ui_element == current_bodies:
                for obj in objects:
                    if obj.repr_pos() == event.text:
                        # go to body 
                        camera[0] = obj.x - (1280 / 2)
                        camera[1] = obj.y - (720 / 2)
                        print(f'Camera position: {camera}')

            if event.ui_element == preset_selection:
                objects = []
                print(r'Physics objects cleared.')
                if event.text == 'Solar system':
                    objects, simulation_speed = solar_system()
                if event.text == '3x3 grid':
                    objects, simulation_speed = grid_3x3()
                if event.text == 'Galaxy':
                    objects, simulation_speed = galaxy_simulation()
                if event.text == 'Cluster':
                    objects, simulation_speed = star_cluster()
                if event.text == 'Triple Ellipse':
                    objects, simulation_speed = triple_ellipse_preset()
                else:
                    print('No preset selected.')
                objs = []
                for obj in objects:
                    objs.append(obj.repr_pos())
                current_bodies.set_item_list(objs)
                print(f'Simulation speed: {simulation_speed}')
                print(f'Objects: {objects}')
        
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
            if event.ui_element == body_mass_input:
                body_mass = float(eval(event.text)) # eval() is used to allow scientific notation, like: 1e+24, 2*10**24, etc.
                print(f'Body mass: {body_mass}')
            if event.ui_element == body_density_input:
                body_density = float(eval(event.text)) # eval() is used to allow scientific notation, like: 1e+24, 2*10**24, etc.
                print(f'Body density: {body_density}')
            if event.ui_element == body_color_input:
                body_color = tuple(map(int, event.text.split(',')))
                print(f'Body color: {body_color}')
            if event.ui_element == g_constant_input:
                G_constant = float(eval(event.text)) # eval() is used to allow scientific notation, like: 1e+24, 2*10**24, etc.
                print(f'G constant: {G_constant}')

    keys = pygame.key.get_pressed()
    
    # if shift is down, camera goes faster       
    if keys[pygame.K_LSHIFT]:
        camera_speed = 30
    else:
        camera_speed = 10

    # WASD camera movement
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
        if obj.update(objects, G_constant, body_delta):
            #objs = []
            #for obj in objects:
            #    objs.append(obj.repr_pos())
            #current_bodies.set_item_list(objs)
            pass

        objs.clear()
        objs.append(obj.repr_pos())
    
    #screen.fill((88, 85, 83)) # Clear screen
    screen.fill((0, 0, 0))
    # Drawing starts here ---

    for obj in objects:
        obj.draw(screen, camera)
    manager.draw_ui(screen)
    ## Drawing ends here ---

    # Debug information
    debug_text = debug_font.render(f'Camera: {camera}, Speed: {camera_speed}', True, (255, 255, 255))
    screen.blit(debug_text, (0, 0))
    # fps
    fps_text = debug_font.render(f'FPS: {round(clock.get_fps())}', True, (255, 255, 255))
    screen.blit(fps_text, (0, 15))
    # total number of objects
    obj_text = debug_font.render(f'Objects: {len(objects)}', True, (255, 255, 255))
    screen.blit(obj_text, (0, 30))
    # simulation speed
    sim_text = debug_font.render(f'Simulation speed: {simulation_speed}', True, (255, 255, 255))
    screen.blit(sim_text, (0, 45))
    # draw borders of 0x0 to 1280x720
    #pygame.draw.rect(screen, (255, 255, 255), (0+camera[0], 0+camera[1], 1280+camera[0], 720+camera[1]), 1)

    pygame.display.flip()
    clock.tick(60) # Update everything 30 times per second


pygame.quit()
