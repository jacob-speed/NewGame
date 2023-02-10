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
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed

# Ball object
class Ball(object):
    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT, scaler):
        self.radius = min(scaler * abs(random.normalvariate(40, 15)) + 5, 65)
        self.speed = scaler * random.normalvariate(math.log(100 - self.radius) * 2.5, 2.5)
        self.speed_x = self.speed * (random.normalvariate(0.5, 0.2)) * random.choice([-1, 1])
        self.speed_y = math.sqrt(abs(self.speed**2 - self.speed_x**2)) * random.choice([-1, 1])
        self.hp = random.normalvariate(self. radius + self.speed, self.speed)
        self.type = random.randint(1,20)
        if self.type > 3:
            self.type = 4
        if self.type == 4:
            self.x = (65 + (WINDOW_WIDTH - 130) * random.randint(0,1))
            self.y = (65 + (WINDOW_HEIGHT - 130) * random.randint(0,1))
            self.colour = (255, 255, 255)
        else:
            self.x = (65 + (WINDOW_WIDTH - 130) * random.random())
            self.y = (65 + (WINDOW_HEIGHT - 130) * random.random())
            if self.type == 1:
                self.colour = (255, 0, 0)
            if self.type == 2:
                self.colour = (0, 255, 0)
            if self.type == 3:
                self.colour = (0, 0, 255)

    def draw(self, win):
        pygame.draw.circle(win, self.colour, (self.x, self.y), self.radius)