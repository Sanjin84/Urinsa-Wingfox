#goals
#1. create a re-set point for when the ball goes beyond the player or the opponent
#2. Track score for player and the opponent
#3. Display score for player and the opponent
#4. Create a winner when either the player or the opponent reaches 3 points

from ursina import * 
app = Ursina()
camera.position = (0,0,-50)

top_wall = Entity(model = 'cube', collider = 'box', position = (0,5.5,0), scale = (10, 1, 50), texture = 'white_cube', texture_scale = (5,5))
bottom_wall = Entity(model = 'cube', collider = 'box', position = (0,-5.5,0), scale = (10, 1, 50), texture = 'white_cube', texture_scale = (5,5))
left_wall = Entity(model = 'cube', collider = 'box', position = (-5.5,0,0), scale = (1, 10, 50), texture = 'white_cube', texture_scale = (5,5))
right_wall = Entity(model = 'cube', collider = 'box', position = (5.5,0,0), scale = (1, 10, 50), texture = 'white_cube', texture_scale = (5,5))
front_wall = Entity(model = 'cube', collider = 'box', position = (0,0,26),
 scale = (10, 10, 3), texture = 'white_cube', texture_scale = (5,5), color=color.white50)

ball = Entity(model = 'sphere', collider = 'sphere', color = color.yellow, scale = 0.7, dx = 0.05, dy = 0.05, dz = 0.3)

player = Entity(model = 'cube', collider = 'box', texture = 'pong_p.png', scale =(2.5,2.5, 1), position = (0,0,-24), score = 0)
opponent = Entity(model = 'cube', collider = 'box', texture = 'pong_e.png', scale =(2.5,2.5, 1), position = (0,0,24), dx = 0, dy = 0, score = 0)

player_score = Text(text = 'PLAYER: ' + str(player.score), origin = (-6.4,0), background = True)
opponent_score = Text(text = 'OPPONENT: ' + str(opponent.score), origin = (4.6,0), background = True)

def update():
    #player movement
    if held_keys['a'] and player.x > -3.5: player.x-= 0.1
    if held_keys['d'] and player.x < 3.5: player.x+= 0.1
    if held_keys['w'] and player.y < 3.5: player.y+= 0.1
    if held_keys['s'] and player.y > -3.5: player.y-= 0.1

    #enemy movement
    if ball.x > opponent.x+1 and opponent.x < 4:
        opponent.dx = 0.05
    elif opponent.x > ball.x-1 and opponent.x > -4:
        opponent.dx = -0.05
    else:
        opponent.dx = 0
    if ball.y > opponent.y+1 and opponent.y < 4:
        opponent.dy = 0.05
    elif opponent.y > ball.y-1 and opponent.y > -4:
        opponent.dy = -0.05
    else:
        opponent.dy = 0

    opponent.x += opponent.dx
    opponent.y += opponent.dy

    #ball movement
    ball.x += ball.dx
    ball.y += ball.dy
    ball.z += ball.dz

    #ball reset
    if ball.z > 28:
        ball.position = (0,0,-25)
        ball.dx = 0.05 
        ball.dy = 0.05 
        ball.dz = 0.3
        player.score += 1
        player_score.text = 'PLAYER: ' + str(player.score)
        if player.score >= 3: 
            Text(text = 'YOU WIN', origin = (0,0), background = True, color = color.green)
            application.pause()
    if ball.z <-28:
        ball.position = (0,0,25)
        ball.dx = 0.05 
        ball.dy = 0.05 
        ball.dz = -0.3
        opponent.score += 1
        opponent_score.text = 'OPPONENT: ' + str(opponent.score)
        if opponent.score >= 3: 
            Text(text = 'OPPONNENT WINS', origin = (0,0), background = True, color = color.red)
            application.pause()
        

    #ball colisions with floor, ceiling and walls
    if ball.x > 5.5 or ball.x < -5.5:
        ball.dx = -ball.dx
    if ball.y > 4.8 or ball.y < -4.8:
        ball.dy = -ball.dy

    hit_info = ball.intersects()
    if hit_info.hit:
        if hit_info.entity == player:
            ball.dx *= 1.02
            ball.dy *= 1.02
            ball.dz *= 1.02
            ball.dz = -ball.dz
        if hit_info.entity == opponent:
            ball.dz = -ball.dz

        if hit_info.entity == top_wall or hit_info.entity == bottom_wall:
            ball.dy = -ball.dy
        if hit_info.entity == left_wall or hit_info.entity == right_wall:
            ball.dx = -ball.dx

EditorCamera()

app.run()