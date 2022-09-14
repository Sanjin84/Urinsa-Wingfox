#1. Program minotaur movement so that the minotaur covers the entire maze
#2. Sense the collision between the minotaur and the player

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader

import time

start_time = time.time()
remaining_time  = 100
total_time = 100

def load_maze_coins(maze_txt_file, level_color):
    global coins, num_coins, empty_spaces, maze
    maze = Entity()
    maze_file = open(maze_txt_file, encoding = 'utf-8')
    x = -20
    for line in maze_file:
        z = -22
        x += 2
        print(line)
        for c in line:
            z += 2
            if c == '║' or c == '═':
                Entity(parent = maze, model = 'cube', collider = 'box', scale = (2,3,2), position = (x,1,z), color = level_color, texture = 'brick', texture_scale = (2,2), shader = lit_with_shadows_shader)
            if c == ' ':
                empty_pos = (x,2,z)
                empty_spaces.append(empty_pos)

    for i in range(num_coins):
        coin_pos = random.choice(empty_spaces)
        empty_spaces.remove(coin_pos)
        coins.append(Entity(model = 'sphere', collider = 'box', position = coin_pos, color = color.yellow, shader = lit_with_shadows_shader ))


def load_level(lvl):
    global player, empty_spaces, minotaur
    colors = [color.red, color.pink, color.blue]
    load_maze_coins('rainbowmaze'+str(lvl)+'.txt', colors[lvl-1])
    player_pos = random.choice(empty_spaces)
    player = FirstPersonController(model = 'cube', collider = 'box', jump_height = 3, position = player_pos)
    if lvl == 3:
        minotaur = Entity(model ='cube', collider = 'box', color=color.red,scale = (2,3,2), position = random.choice(empty_spaces))

def minotaur_movement(bull):
    global player
    origin_down = bull.position +(bull.down*0.3)
    project_forward = raycast(origin_down, bull.forward, distance = 1.05, ignore=[bull], debug= True)
    origin_back = bull.position +bull.back*0.45
    project_left = raycast(origin_back, bull.left, distance = 1.05, ignore=[bull], debug= True)
    #if you can turn left than turn left
    if not project_left.hit:
        bull.position += bull.left*1
        bull.rotation_y -=90
    #if cant turn left try going forward
    if not project_forward.hit:
        bull.position += bull.forward*0.01
    #if you cant go left or forward turn right
    else:
        bull.rotation_y += 90
    if bull.intersects(player):
        Text(text = ' YOU LOSE', origin = (0,0), scale = 3, background = True, color = color.red)
        application.pause()
        mouse.locked = False




app = Ursina()
window.size = (1280,720)

coins = []
num_coins = 50
empty_spaces = []
score = 0
level =3
load_level(level)

floor = Entity(model = 'plane', collider = 'box', scale = (42,1,42), texture='grass', texture_scale = (42,42))

score_text = Text(text = 'SCORE: ' + str(score), origin = (4.65, -18.3))
time_text = Text(text = '', origin = (4.65, -18.3))

def update():
    global score, maze, coins, empty_spaces, level, player, total_time
    remaining_time = total_time - round(time.time() - start_time)
    time_text.text = str(remaining_time)
    hit_info = player.intersects()
    if level == 3:
        minotaur_movement(minotaur)
    if hit_info.entity in coins:
        coins.remove(hit_info.entity)
        destroy(hit_info.entity)
        score += 1
        score_text.text = 'SCORE: ' + str(score)
        if score == num_coins:
            if level == 3:
                Text(text = 'YOU WIN', origin = (0,0), scale = 3, background = True, color = color.green)
                application.pause()
                mouse.locked = False
            else:
                score = 0
                level += 1
                total_time += 50
                destroy(maze)
                destroy(player)
                coins.clear()
                empty_spaces.clear()
                load_level(level)

    if remaining_time <= 0:
        Text(text = ' YOU LOSE', origin = (0,0), scale = 3, background = True, color = color.red)
        application.pause()
        mouse.locked = False
    
def input(key):
    if key == 'q':
        application.quit()


sky = Sky()
sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-2))

app.run()