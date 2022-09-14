#goals
#1 Create a player and opponent bats (convert from top and bottom)
#2 Move the player and opponent with arrow keys / other keys

from ursina import *

app = Ursina()

right_wall = Entity(model = 'quad', collider = 'box', scale = (0.5,9), position = (7,0,0), color = color.orange)
left_wall = Entity(model = 'quad', collider = 'box', scale = (0.5,9), position = (-7,0,0), color = color.orange)


player = Entity(model = 'quad', collider = 'box', scale = (3,0.3), position = (0,-3.8,0), color = color.blue, dx = 0)
opponent = Entity(model = 'quad', collider = 'box', scale = (3,0.3), position = (0,3.8,0), color = color.red, dx = 0)


ball = Entity(model = 'circle',collider = 'box', scale = 0.5, position = (-2,0,0), color = color.yellow, dx = 0.02, dy = 0.02)

def input(key):
    if key == 'q':
        application.quit()
    elif held_keys['left arrow'] and player.x > -5:
        player.dx = -0.1
    elif held_keys['right arrow']and player.x < 5:
        player.dx = 0.1
    elif held_keys['s'] and opponent.x > -5:
        opponent.dx = -0.1
    elif held_keys['d']and opponent.x < 5:
        opponent.dx = 0.1
    else:
        player.dx = 0
        opponent.dx = 0


def update():
    ball.x += ball.dx
    ball.y += ball.dy
    player.x += player.dx
    opponent.x += opponent.dx
    hit_info = ball.intersects()

    if hit_info.hit:
        if hit_info.entity == opponent or hit_info.entity == player:
            ball.dy = -ball.dy
        if hit_info.entity == left_wall or hit_info.entity == right_wall:
            ball.dx = -ball.dx


app.run()