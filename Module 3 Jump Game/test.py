from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

camera.orthographic = True
camera.fov = 10

ground = Entity(model='cube', color=color.white33, origin_y=.5, scale=(20, 10, 1), collider='box')
wall = Entity(model='cube', color=color.azure, origin=(-.5,.5), scale=(5,10), x=10, y=.5, collider='box')
wall_2 = Entity(model='cube', color=color.white33, origin=(-.5,.5), scale=(5,10), x=10, y=5, collider='box')
ceiling = Entity(model='cube', color=color.white33, origin_y=-.5, scale=(1, 1, 1), y=1, collider='box')

def input(key):
    if key == 'c':
        wall.collision = not wall.collision
        print(wall.collision)


player_controller = PlatformerController2d(scale_y=2, jump_height=4, x=3)
camera.add_script(SmoothFollow(target=player_controller, offset=[0,1,-30], speed=4))

EditorCamera()

app.run()