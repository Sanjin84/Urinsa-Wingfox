#1. Track all empty spaces in the maze
#2. Randomly place N coins in empty spaces
#3. Collect coins and increase score

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

app = Ursina()
window.size = (1280,720)

coins = []
num_coins = 20
empty_spaces = []
score = 0

floor = Entity(model = 'plane', collider = 'box', scale = (42,1,42), texture='grass', texture_scale = (42,42))

maze_file = open('rainbowmaze1.txt', encoding = 'utf-8')

x = -20
for line in maze_file:
    z = -22
    x += 2
    print(line)
    for c in line:
        z += 2
        if c == '║' or c == '═':
            Entity(model = 'cube', collider = 'box', scale = (2,2,2), position = (x,1,z), color = color.red, texture = 'brick', texture_scale = (2,2), shader = lit_with_shadows_shader )
        else:
            empty_pos = (x,3,z)
            empty_spaces.append(empty_pos)

for i in range(num_coins):
    coin_pos = random.choice(empty_spaces)
    empty_spaces.remove(coin_pos)
    coins.append(Entity(model = 'sphere', collider = 'box', position = coin_pos, color = color.yellow, shader = lit_with_shadows_shader ))


player = FirstPersonController(model = 'cube', collider = 'box')

score_text = Text(text = 'SCORE: ' + str(score), origin = (4.65, -18.3))

def update():
    global score
    hit_info = player.intersects()
    if hit_info.entity in coins:
        coins.remove(hit_info.entity)
        destroy(hit_info.entity)
        score += 1
        score_text.text = 'SCORE: ' + str(score)




def input(key):
    if key == 'q':
        application.quit()


sky = Sky()
sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-2))

app.run()