## collection of functions used for newgame
import math
import pygame
import csv
from datetime import datetime


# Set Start Parameters
def set_start_parameters(Character, WINDOW_WIDTH, WINDOW_HEIGHT):
    frames_counter = 0
    timer = 0
    global_speed = 1.0
    scaler = 1
    print_score_counter = 0
    balls = []
    char = Character(x = WINDOW_WIDTH/2, y = WINDOW_HEIGHT/2, colour = (100, 100, 255), speed = 3, hp = 20)
    highscore = get_high_score()
    return frames_counter, timer, global_speed, scaler, print_score_counter, balls, char, highscore


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
def scale_screen(char, balls, scaler, amount):
    scaler *= amount
    char.height *= amount
    char.width *= amount
    char.speed *= amount
    for ball in balls:
        ball.radius *= amount
        ball.speed_x *= amount
        ball.speed_y *= amount
    
    return scaler


# Get High Score
def get_high_score():
    with open("scores.csv", "r") as file:
        reader = csv.reader(file)
        scores = [float(row[0]) for row in reader]
    return max(scores)


# Update highscore
def update_scores(preivous_time):
    with open("scores.csv", "r") as file:
        reader = csv.reader(file)
        scores = [tuple(row) for row in reader]
    scores.append((preivous_time, datetime.now()))
    with open("scores.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(scores)   


# blit main menu
def blit_main_menu(window, WINDOW_WIDTH, WINDOW_HEIGHT, FPS):
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 50)
    label1 = font.render(f'Ball Game', True, (255, 255, 255))
    label2 = font.render(f'Press Enter to play', True, (255, 255, 255))
    window.blit(label1, ((WINDOW_WIDTH - label1.get_width()) / 2, ((WINDOW_HEIGHT - label1.get_height()) / 2)))
    window.blit(label2, ((WINDOW_WIDTH - label2.get_width()) / 2, ((WINDOW_HEIGHT + label2.get_height()) / 2)))
    pygame.display.update()
    pygame.time.delay(1000 // FPS)