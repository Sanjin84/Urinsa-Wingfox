#Goals 
#1. Create a dynamic where the player jumps higher if you hold down the w key
#2. Detect a victory 

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from random import randint, choice, uniform

app = Ursina()
camera.orthographic = True
camera.fov = 20

ground =Entity(model = 'cube', scale = (100,10,1), collider='box', origin_y = 1, color = color.white33, texture='white_cube', texture_scale = (100,10))
player = PlatformerController2d(jump_height = 8)

x = 0
y = 0
for i in range(20):
    y += randint(3,5)
    side = choice(['left','right'])
    if side == 'left':
        x -= (3+ randint(3,6))
    else: 
        x += (3+ randint(3,6))
    if i < 19:
        Entity(model = 'cube', scale = (randint(3,6),1), color =color.yellow, collider = 'box', position = (x,y,0))
    else:
        finish = Entity(model = 'cube', scale = (randint(3,6),1), color =color.green, collider = 'box', position = (x,y,0))

camera.add_script(SmoothFollow(target=player, offset=[0,1,-30], speed=4))

EditorCamera()
app.run()