import pygame
import random
import math

# Character object
class Character(object):
    def __init__(self, x, y, colour, speed, hp):
        self.hp = hp
        self.x = x
        self.y = y
        self.width = (20 + self.hp)
        self.height = 1.3 * self.width
        self.colour = colour
        self.speed = speed

    def draw(self, win):
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height))  

    def display_params(self):
        print("hp:", self.hp)
        print("x:", self.x)
        print("y:", self.y)
        print("width:", self.width)
        print("height:", self.height)
        print("colour:", self.colour)
        print("speed:", self.speed)

# Ball object
class Ball(object):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, scaler):
        self.scaler = scaler
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.exists = True
        self.type = random.randint(1,30)
        if self.type > 3:
            self.type = 4
        if self.type == 4:
            self.radius = self.scaler * (random.random()* 5 + 3) ** 2
            self.x = (65 + (self.WINDOW_WIDTH - 130) * random.randint(0,1))
            self.y = (65 + (self.WINDOW_HEIGHT - 130) * random.randint(0,1))
            self.colour = (255, 255, 255)
        else:
            self.radius = self.scaler * 20
            self.x = (65 + (self.WINDOW_WIDTH - 130) * random.random())
            self.y = (65 + (self.WINDOW_HEIGHT - 130) * random.random())
            if self.type == 1:
                self.colour = (255, 0, 0)
            if self.type == 2:
                self.colour = (0, 255, 0)
            if self.type == 3:
                self.colour = (0, 0, 255)
        self.speed_x = self.scaler * (random.random() * 3 + 1) ** 2
        self.speed_y = self.scaler * (random.random() * 3 + 1) ** 2
        self.hp = math.sqrt(self.speed_x * self.speed_y * self.radius) 

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)