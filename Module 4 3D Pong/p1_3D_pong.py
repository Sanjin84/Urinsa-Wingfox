#goals
#1. Build walls and ceiling and select a texture
#2. Experiment with camera field of view and camera position to optimise player perspetive

from ursina import * 
app = Ursina()
camera.position = (0,0,-48)

top_wall = Entity(model = 'cube', collider = 'box', position = (0,5,0), scale = (10, 0.5, 50), texture = 'white_cube', texture_scale = (5,5))
bottom_wall = Entity(model = 'cube', collider = 'box', position = (0,-5,0), scale = (10, 0.5, 50), texture = 'white_cube', texture_scale = (5,5))
left_wall = Entity(model = 'cube', collider = 'box', position = (-5,0,0), scale = (0.5, 10, 50), texture = 'white_cube', texture_scale = (5,5))
right_wall = Entity(model = 'cube', collider = 'box', position = (5,0,0), scale = (0.5, 10, 50), texture = 'white_cube', texture_scale = (5,5))

EditorCamera()

app.run()