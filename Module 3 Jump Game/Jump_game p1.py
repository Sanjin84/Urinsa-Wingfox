#Goals 
#1. Import the PlatformerController
#2. Create a Player and Ground
#3. Test out the platformer environment

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

ground =Entity(model = 'cube', scale = (20,10,1), collider='box', origin_y = 0.6, color = color.white33)
player = PlatformerController2d()


EditorCamera()
app.run()