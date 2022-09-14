#goals
#1 Sense a collision between 2 entities
#2 Create bounce animation (ball bouncing off a rectangle)

from ursina import *

app = Ursina()

right_wall = Entity(model = 'quad', collider = 'box', scale = (0.5,9), position = (7,0,0), color = color.orange)
left_wall = Entity(model = 'quad', collider = 'box', scale = (0.5,9), position = (-7,0,0), color = color.orange)
bottom = Entity(model = 'quad', collider = 'box', scale = (15,0.5), position = (0,-3.8,0), color = color.orange)
top = Entity(model = 'quad', collider = 'box', scale = (15,0.5), position = (0,3.8,0), color = color.orange)


ball = Entity(model = 'circle',collider = 'box', scale = 0.5, position = (-2,0,0), color = color.yellow, dx = 0.02, dy = 0.02)


def update():
    ball.x += ball.dx
    ball.y += ball.dy
    hit_info = ball.intersects()

    if hit_info.hit:
        if hit_info.entity == top or hit_info.entity == bottom:
            ball.dy = -ball.dy
        if hit_info.entity == left_wall or hit_info.entity == right_wall:
            ball.dx = -ball.dx


app.run()