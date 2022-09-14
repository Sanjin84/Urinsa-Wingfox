#Goals 
#1. Have the platforms move right to left 
#2. Create friction between the player and the platforms
#3. Create an alternative jumping dynamic which requires timing


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
platforms = []
for i in range(20):
    y += randint(3,5)
    side = choice(['left','right'])
    if side == 'left':
        x -= (3+ randint(3,6))
    else: 
        x += (3+ randint(3,6))
    if i < 19:
        platforms.append(Entity(model = 'cube', scale = (randint(3,6),1), color =color.yellow, collider = 'box', position = (x,y,0)))
    else:
        finish = Entity(model = 'cube', scale = (randint(3,6),1), color =color.green, collider = 'box', position = (x,y,0))
        platforms.append(finish)
for platform in platforms:
    platform.dx = uniform(-0.1,0.1)

def update():
    if held_keys['w']:
        if player.jump_height < 20:
            player.jump_height +=0.1
        player.jump_duration = 1
        player.jump()
    else:
        player.jump_height = 4 
        player.jump_duration =0.5
    if player.intersects(finish):
        Text(text = 'YOU WIN', scale = 2, origin = (0,0), background = True, color = color.green)
        application.pause()

    #platform movement
    for platform in platforms:
        platform.x += platform.dx
        if platform.x > 49 or platform.x < -49:
            platform.dx = -platform.dx
        if player.intersects(platform):
            player.x += platform.dx

camera.add_script(SmoothFollow(target=player, offset=[0,1,-30], speed=4))

EditorCamera()
app.run()