## collection of functions used for newgame
import math
import csv
from datetime import datetime


# Ball collsion
def ball_collision(ball, char):
    collision = False

    if ball.x < char.x:
        if ball.y < char.y and math.sqrt((ball.x - char.x)**2 + (ball.y - char.y)**2) < ball.radius:
            collision = True
        if ball.y > char.y + char.height and math.sqrt((ball.x - char.x)**2 + (ball.y - (char.y + char.height))**2) < ball.radius:
            collision = True
        if char.y <= ball.y <= char.y + char.height and char.x - ball.x < ball.radius:
            collision = True
    if ball.x > char.x + char.width:
        if ball.y < char.y and math.sqrt((ball.x - (char.x + char.width))**2 + (ball.y - char.y)**2) < ball.radius:
            collision = True
        if ball.y > char.y + char.height and math.sqrt((ball.x - (char.x + char.width))**2 + (ball.y - (char.y + char.height))**2) < ball.radius:
            collision = True
        if char.y <= ball.y <= char.y + char.height and ball.x - (char.x + char.width) < ball.radius:
            collision = True
    if char.x <= ball.x <= char.x + char.width:
        if abs(char.y - ball.y) < ball.radius or abs(ball.y - (char.y + char.height)) < ball.radius:
            collision = True
    
    return collision

# Scale Screen

def screen_shrink(char, balls, scaler, SCALE):
    scaler *= SCALE
    char.x *= SCALE
    char.y *= SCALE
    char.height *= SCALE
    char.width *= SCALE
    char.speed *= SCALE
    for ball in balls:
        ball.radius *= SCALE
        ball.x *= SCALE
        ball.y *= SCALE
        ball.speed_x *= SCALE
        ball.speed_y *= SCALE

# highscore
def highscore():
    with open("scores.csv", "r") as file:
        reader = csv.reader(file)
        scores = [tuple(row) for row in reader]
    scores1 = [x[0] for x in scores]
    highscore = 0
    for score in scores1:
        if float(score) > highscore:
            highscore = float(score)
    return(highscore)



def set_start_parameters(Character, WINDOW_WIDTH, WINDOW_HEIGHT):
    global frames_counter
    global timer
    global global_speed
    global scaler
    global print_score_counter
    global balls
    global char
    frames_counter = 0
    timer = 0
    global_speed = 1.0
    scaler = 1
    print_score_counter = 0
    balls = []
    char = Character(x = WINDOW_WIDTH/2, y = WINDOW_HEIGHT/2, colour = (100, 100, 255), speed = 3, hp = 20)

    return frames_counter, timer, global_speed, scaler, print_score_counter, balls, char


# Update highscore
def update_scores(preivous_time):
    with open("scores.csv", "r") as file:
        reader = csv.reader(file)
        scores = [tuple(row) for row in reader]
    scores.append((preivous_time, datetime.now()))
    with open("scores.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(scores)   