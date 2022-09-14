#1. Modify colors and textures of all entities
#2. Modify dimensions
#3. Create sky, sun and shadows to make the maze feel more natural

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina()
window.size = (1280,720)

floor = Entity(model = 'plane', collider = 'box', scale = (42,1,42), texture='grass', texture_scale = (42,42))

maze_file = open('rainbowmaze1.txt', encoding = 'utf-8')

x = -20
for line in maze_file:
    z = -22
    x += 2
    print(line)
    for c in line:
        z += 2
        if c == '║' or c == '═':
            Entity(model = 'cube', collider = 'box', scale = (2,3,2), position = (x,1,z), color = color.red, texture = 'brick', texture_scale = (2,2), shader = lit_with_shadows_shader )

player = FirstPersonController(model = 'cube')


def input(key):
    if key == 'q':
        application.quit()


sky = Sky()
sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-2))

app.run()