#goals
#1 Sense a collision between 2 entities
#2 Create bounce animation (ball bouncing off a rectangle)

from ursina import *

app = Ursina()

square = Entity(model = 'quad', collider = 'box', scale = (2,2), position = (4,0,0))
circle = Entity(model = 'circle',collider = 'box', scale = 1, position = (-2,0,0), color = color.yellow, dx = 0.02)

def update():
    circle.x += circle.dx
    hit_info = circle.intersects()
    if hit_info.hit:
        circle.dx = -circle.dx
        print('BOUNCE')

app.run()