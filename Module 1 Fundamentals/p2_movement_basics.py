#goals
#1 Move an entity by changing x and y values
#2 Rotate an entity


from ursina import *

app = Ursina()

square = Entity(model = 'quad', scale = (2,2))
circle = Entity(model = 'circle', scale = 1, position = (-2,0,0), color = color.yellow)

def update():
    square.x += 0.01
    circle.y -= 0.02
    square.rotation_x += 1
    square.rotation_y += 1
    square.rotation_z += 1



app.run()
