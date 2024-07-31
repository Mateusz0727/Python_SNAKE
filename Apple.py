import random
from tkinter import SEL
from turtle import update
import pygame


class Apple():
    def __init__(self):
        self.x = random.choice(range(75, 451, 50))
        self.y = random.choice(range(75, 451, 50))
        self.body = (self.x, self.y)
        
    def collision(self,snake):       
        if snake.head.center == (self.x,self.y):
            snake.body.append(pygame.Rect(snake.body[-1].center[0]-25,snake.body[-1].center[1]-25,50,50))
            self.update()
    
    def update(self):
        self.x = random.choice(range(75, 451, 50))
        self.y = random.choice(range(75, 451, 50))
        self.body = (self.x, self.y)

