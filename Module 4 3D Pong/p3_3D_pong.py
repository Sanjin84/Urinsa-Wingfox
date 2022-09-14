#goals
#1. Complete the bounce so that it works in 3 dimensions
#2. Create a player entity (movable by w a s d) and bounce the ball off the player

from ursina import * 
app = Ursina()
camera.position = (0,0,-48)

top_wall = Entity(model = 'cube', collider = 'box', position = (0,5,0), scale = (10, 0.5, 50), texture = 'white_cube', texture_scale = (5,5))
bottom_wall = Entity(model = 'cube', collider = 'box', position = (0,-5,0), scale = (10, 0.5, 50), texture = 'white_cube', texture_scale = (5,5))
left_wall = Entity(model = 'cube', collider = 'box', position = (-5,0,0), scale = (0.5, 10, 50), texture = 'white_cube', texture_scale = (5,5))
right_wall = Entity(model = 'cube', collider = 'box', position = (5,0,0), scale = (0.5, 10, 50), texture = 'white_cube', texture_scale = (5,5))
front_wall = Entity(model = 'cube', collider = 'box', position = (0,0,25),
 scale = (10, 10, 2), texture = 'white_cube', texture_scale = (5,5), color=color.white50)
back_wall = Entity(model = 'cube', collider = 'box', position = (0,0,-27),
 scale = (12, 12, 2), texture = 'white_cube', texture_scale = (5,5), color=color.white10)

ball = Entity(model = 'sphere', collider = 'sphere', color = color.yellow, scale = 0.7, dx = 0.05, dy = 0.05, dz = 0.3)

player = Entity(model = 'cube', collider = 'box', texture = 'pong_p.png', scale =(2.5,2.5, 0.5), position = (0,0,-24))

def update():
    ball.x += ball.dx
    ball.y += ball.dy
    ball.z += ball.dz

    if held_keys['a'] and player.x > -3.5: player.x-= 0.1
    if held_keys['d'] and player.x < 3.5: player.x+= 0.1
    if held_keys['w'] and player.y < 3.5: player.y+= 0.1
    if held_keys['s'] and player.y > -3.5: player.y-= 0.1

    hit_info = ball.intersects()
    if hit_info.hit:
        if hit_info.entity == front_wall or hit_info.entity == player or hit_info.entity == back_wall:
            ball.dz = -ball.dz
        if hit_info.entity == top_wall or hit_info.entity == bottom_wall:
            ball.dy = -ball.dy
        if hit_info.entity == left_wall or hit_info.entity == right_wall:
            ball.dx = -ball.dx

EditorCamera()

app.run()