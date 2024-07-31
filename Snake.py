from pygame import draw
import pygame


class Snake():
    def __init__(self):        
        self.x,self.y=50,50
        self.xdir=1
        self.ydir=0
        self.body = [pygame.Rect(self.x-50,self.y,50,50)]
        self.head = pygame.Rect(self.x,self.y,50,50,border_radius = 15)
        
    def update(self):
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x,self.body[i].y=self.body[i+1].x,self.body[i+1].y
        self.head.x+=self.xdir*50
        self.head.y+=self.ydir*50
        self.body.remove(self.head)
    def selfColissions(self):
        for segment in self.body[2:]:
           if pygame.Rect.colliderect(self.head, segment):
                
                return True