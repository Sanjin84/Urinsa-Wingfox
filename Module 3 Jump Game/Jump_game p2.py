#Goals 
#1. Test out orthographic camera
#2. Test out a camera that follows the player
#3. Test out a platform we can jump on

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from random import randint

app = Ursina()
camera.orthographic = True
camera.fov = 20

ground =Entity(model = 'cube', scale = (100,10,1), collider='box', origin_y = 1, color = color.white33, texture='white_cube', texture_scale = (100,10))
player = PlatformerController2d(jump_height = 8)


for i in range(50):
    Entity(model = 'cube', scale = (5,1), color =color.yellow, collider = 'box', position = (randint(-50,50), randint(-2,10),0))

camera.add_script(SmoothFollow(target=player, offset=[0,1,-30], speed=4))

EditorCamera()
app.run()