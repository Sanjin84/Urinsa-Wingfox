#1. Create a flat entity that could be our floor
#2. Create a player first person controller
#3. Convert a 2D text file maxe into a real 3D maze that the player can navigate

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.size = (1280,720)

floor = Entity(model = 'plane', collider = 'box', scale = (42,1,42), texture='white_cube', texture_scale = (21,21))

maze_file = open('rainbowmaze1.txt', encoding = 'utf-8')

x = -20
for line in maze_file:
    z = -22
    x += 2
    print(line)
    for c in line:
        z += 2
        if c == '║' or c == '═':
            Entity(model = 'cube', collider = 'box', scale = (2,2,2), position = (x,1,z), color = color.red)



player = FirstPersonController(model = 'cube')


def input(key):
    if key == 'q':
        application.quit()

app.run()