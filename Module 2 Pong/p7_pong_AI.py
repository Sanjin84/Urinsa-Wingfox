#goals
#1. Create an AI opponent
#2. Set speeds to levels that makes the game competitive

from ursina import *

app = Ursina()

right_wall = Entity(model = 'quad', collider = 'box', scale = (0.5,9), position = (7,0,0), color = color.orange)
left_wall = Entity(model = 'quad', collider = 'box', scale = (0.5,9), position = (-7,0,0), color = color.orange)

player = Entity(model = 'quad', collider = 'box', scale = (3,0.3), position = (0,-3.8,0), color = color.blue, dx = 0, score = 0)
opponent = Entity(model = 'quad', collider = 'box', scale = (3,0.3), position = (0,3.8,0), color = color.red, dx = 0, score = 0)

ball = Entity(model = 'circle',collider = 'box', scale = 0.5, position = (-2,0,0), color = color.yellow, dx = 0.05, dy = 0.05)

p1_score_label = Text(text ='P1 SCORE: 0', position = (-0.73,0.45,0))
p2_score_label  = Text(text ='P2 SCORE: 0', position = (0.6,0.45,0))

def input(key):
    if key == 'q':
        application.quit()
    elif held_keys['left arrow'] and player.x > -5:
        player.dx = -0.04
    elif held_keys['right arrow']and player.x < 5:
        player.dx = 0.04
    else:
        player.dx = 0
        opponent.dx = 0


def update():
    ball.x += ball.dx
    ball.y += ball.dy
    player.x += player.dx
    opponent.x += opponent.dx
    hit_info = ball.intersects()

    #collision logic
    if hit_info.hit:
        ball.dy = ball.dy*1.05
        if hit_info.entity == opponent:
            ball.dy = -ball.dy
            ball.dx = (ball.x - opponent.x)*0.05
        if hit_info.entity == player:
            ball.dy = -ball.dy
            ball.dx = (ball.x - player.x)*0.05 
        if hit_info.entity == left_wall or hit_info.entity == right_wall:
            ball.dx = -ball.dx
    #scoring logic
    if ball.y > 4:
        player.score += 1
        p1_score_label.text = 'P1 SCORE: '+  str(player.score)
        ball.position = (0,0,0)
        ball.dy = 0.05
        ball.dx = 0
    if ball.y < -4:
        opponent.score += 1
        p2_score_label.text = 'P2 SCORE: '+  str(opponent.score)
        ball.position = (0,0,0)
        ball.dy = -0.05
        ball.dx = 0
    #winning logic
    if player.score >= 3:
        Text(text = 'P1 WINS', scale = 2.5, background = True, position = (-0.1,0.1,0), origin = (0,-0), color = color.green)
        application.pause()
    if opponent.score >= 3:
        Text(text = 'P2 WINS', scale = 2.5, background = True, position = (-0.1,0.1,0), origin = (0,-0), color = color.green)
        application.pause()
    #opponent movement logic
    if ball.x > opponent.x + 1:
        opponent.dx = 0.06
    elif ball.x < opponent.x -1:
        opponent.dx = -0.06
    else:
        opponent.dx = 0


app.run()