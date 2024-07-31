
import pygame
import pygame_menu
from Apple import Apple


from Snake import Snake
canvas = pygame.display.set_mode((500, 500)) 
pygame.init() 
pygame.display.set_caption("Snake game") 
def end(snake):
    if (snake.xdir==1 and snake.head.right==500)or(snake.xdir==-1 and snake.head.left==0):
        print(len(snake.body))
        print("koniec")
        return True
    elif (snake.ydir==-1 and snake.head.top==0)or(snake.ydir==1 and snake.head.bottom==500):
        print(len(snake.body))
        print("koniec")
        return True
    elif snake.selfColissions():
        return True
    else:
        return False
def play_function():

    exit = False
    
   
    clock=pygame.time.Clock()
    snake = Snake()
    apple = Apple();


    while not exit: 
        for event in pygame.event.get(): 
           
            if event.type == pygame.KEYDOWN:            
                if event.key==  pygame.K_s and snake.ydir==0:
                    snake.ydir=1
                    snake.xdir=0                
                elif event.key==  pygame.K_w and snake.ydir==0:              
                    snake.ydir=-1
                    snake.xdir=0
                elif event.key==  pygame.K_a and snake.xdir==0:
                    snake.ydir=0
                    snake.xdir=-1                
                elif event.key==  pygame.K_d and snake.xdir==0:
                    snake.ydir=0
                    snake.xdir=1
       
            
   
   
        apple.collision(snake)
    
        snake.update()
        canvas.fill('black')
        pygame.draw.circle(canvas, "yellow", apple.body, 25)
        pygame.draw.rect(canvas,"red",snake.head)        
        for segments in snake.body:
            pygame.draw.rect(canvas,"green",segments)
    
        pygame.display.update()
        if end(snake):
            exit = True
    
    
        clock.tick(3)
menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('Play', play_function)
menu.add.button('Quit', pygame_menu.events.EXIT)


menu.mainloop(canvas)
