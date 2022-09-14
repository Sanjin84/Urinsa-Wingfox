#goals
#1. Build front and back walls that are semi transparent
#2. Have a ball bounce inside the 6 walls

from ursina import * 
app = Ursina()
camera.position = (0,0,-48)

top_wall = Entity(model = 'cube', collider = 'box', position = (0,5,0), scale = (10, 0.5, 50), texture = 'white_cube', texture_scale = (5,5))
bottom_wall = Entity(model = 'cube', collider = 'box', position = (0,-5,0), scale = (10, 0.5, 50), texture = 'white_cube', texture_scale = (5,5))
left_wall = Entity(model = 'cube', collider = 'box', position = (-5,0,0), scale = (0.5, 10, 50), texture = 'white_cube', texture_scale = (5,5))
right_wall = Entity(model = 'cube', collider = 'box', position = (5,0,0), scale = (0.5, 10, 50), texture = 'white_cube', texture_scale = (5,5),color=color.white10)

front_wall = Entity(model = 'cube', collider = 'box', position = (0,0,25),
 scale = (10, 10, 2), texture = 'white_cube', texture_scale = (5,5), color=color.white50)
back_wall = Entity(model = 'cube', collider = 'box', position = (0,0,-25),
 scale = (10, 10, 2), texture = 'white_cube', texture_scale = (5,5), color=color.white10)

ball = Entity(model = 'sphere', collider = 'sphere', color = color.yellow, scale = 0.7, dx = 0, dy = 0, dz = 0.3)

def update():
    ball.z += ball.dz

    hit_info = ball.intersects()
    if hit_info.hit:
        ball.dz = -ball.dz


EditorCamera()

app.run()