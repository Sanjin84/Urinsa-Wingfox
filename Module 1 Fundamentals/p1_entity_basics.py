#goals
#1 Run Ursina

from ursina import *
app = Ursina()
#2 create some entities: square, circle and a plane

square = Entity(model = 'quad', scale = (2,2))

circle = Entity(model = 'circle', scale = 1, position = (-2,0,0), color = color.yellow)

plane = Entity(model = 'plane', scale = (5,6), position = (0,-3,0), color = color.green)

EditorCamera()

app.run()


#3 View entities from 3 dimensions
