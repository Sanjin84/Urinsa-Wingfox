#goals
#1. Create difficulty Escalation
#2. Create a losing condition / test scoring system

from ursina import * 
app = Ursina()
camera.position = (0,0,-50)

top_wall = Entity(model = 'cube', collider = 'box', position = (0,5.5,0), scale = (10, 1, 50), texture = 'white_cube', texture_scale = (5,5))
bottom_wall = Entity(model = 'cube', collider = 'box', position = (0,-5.5,0), scale = (10, 1, 50), texture = 'white_cube', texture_scale = (5,5))
left_wall = Entity(model = 'cube', collider = 'box', position = (-5.5,0,0), scale = (1, 10, 50), texture = 'white_cube', texture_scale = (5,5))
right_wall = Entity(model = 'cube', collider = 'box', position = (5.5,0,0), scale = (1, 10, 50), texture = 'white_cube', texture_scale = (5,5))
front_wall = Entity(model = 'cube', collider = 'box', position = (0,0,26),
 scale = (10, 10, 3), texture = 'white_cube', texture_scale = (5,5), color=color.white50)
back_wall = Entity(model = 'cube', collider = 'box', position = (0,0,-27),
 scale = (12, 12, 3), texture = 'white_cube', texture_scale = (5,5), color=color.white10)

ball = Entity(model = 'sphere', collider = 'sphere', color = color.yellow, scale = 0.7, dx = 0.05, dy = 0.05, dz = 0.3)

player = Entity(model = 'cube', collider = 'box', texture = 'pong_p.png', scale =(2.5,2.5, 1), position = (0,0,-24))
opponent = Entity(model = 'cube', collider = 'box', texture = 'pong_e.png', scale =(2.5,2.5, 1), position = (0,0,24), dx = 0, dy = 0)

def update():
    ball.x += ball.dx
    ball.y += ball.dy
    ball.z += ball.dz

    #player movement
    if held_keys['a'] and player.x > -3.5: player.x-= 0.1
    if held_keys['d'] and player.x < 3.5: player.x+= 0.1
    if held_keys['w'] and player.y < 3.5: player.y+= 0.1
    if held_keys['s'] and player.y > -3.5: player.y-= 0.1

    #enemy movement
    if ball.x > opponent.x+1 and opponent.x < 4:
        opponent.dx = 0.05
    elif opponent.x > ball.x-1 and opponent.x > -4:
        opponent.dx = -0.05
    else:
        opponent.dx = 0
    if ball.y > opponent.y+1 and opponent.y < 4:
        opponent.dy = 0.05
    elif opponent.y > ball.y-1 and opponent.y > -4:
        opponent.dy = -0.05
    else:
        opponent.dy = 0

    opponent.x += opponent.dx
    opponent.y += opponent.dy


    #ball colisions with floor, ceiling and walls
    if ball.x > 5.5 or ball.x < -5.5:
        ball.dx = -ball.dx
    if ball.y > 4.8 or ball.y < -4.8:
        ball.dy = -ball.dy


    hit_info = ball.intersects()
    if hit_info.hit:
        if hit_info.entity == player:
            ball.dx *= 1.02
            ball.dy *= 1.02
            ball.dz *= 1.02
            ball.dz = -ball.dz
            print(ball.dx,ball.dy,ball.dz)
        if hit_info.entity == opponent:
            ball.dz = -ball.dz

        if hit_info.entity == top_wall or hit_info.entity == bottom_wall:
            ball.dy = -ball.dy
        if hit_info.entity == left_wall or hit_info.entity == right_wall:
            ball.dx = -ball.dx

EditorCamera()

app.run()