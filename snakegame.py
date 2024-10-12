import pygame
import time
import random

pygame.init()

color_1 = (255,255,255)
color_2 = (255,255,102)
color_3 = (0,0,0)
color_4 = (255,200,80)
color_5 = (0,255,0)
color_6 = (255,0,0)

screen_length = 900
screen_height = 900
add_caption = pygame.display.set_mode((screen_length, screen_height))

pygame.display.set_caption('Snake Game')

timer = pygame.time.Clock()

snake_block = 10
snake_speed = 10

display_style = pygame.font.SysFont('arial', 30, 'bold')
score_font = pygame.font.SysFont('arial', 45, 'bold')

def final_score(score):
    value = score_font.render('Enjoy your game ------- Your score: ' + str(score), True, color_2)
    add_caption.blit(value, [0,0])
    
def make_snake(snake_block, list_snake):
    for x in list_snake:
        pygame.draw.rect(add_caption, color_3, [x[0], x[1], snake_block])


def display_msg(msg, color):
    message = display_style.render(msg, True, color)
    add_caption.blit(message, [screen_length/6, screen_height/6])
    
def game_start():
    game_over = False
    game_close = False
    
    value_x1 = screen_length/2
    value_y1 = screen_height/2
    
    new_x1 = 0
    new_y1 = 0
    
    list_snake = []
    snake_len = 1
    
    foodx_pos = round(random.randrange(0, screen_length - snake_block)/10.0)*10.0
    foodY_pos = round(random.randrange(0, screen_height - snake_block)/10.0)*10.0
    
    while not game_over:
        while game_close == True:
            add_caption.fill(color_6)
            display_msg('You Lost. Wanna play again? Play R else play Q.', color_4)
            final_score(snake_len-1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_start()
                        
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        new_x1 = -snake_block
                        new_y1 = 0
                    elif event.key == pygame.K_RIGHT:
                        new_x1 = snake_block
                        new_y1 = 0
                    elif event.key == pygame.K_UP:
                        new_x1 = 0
                        new_y1 = snake_block
                    elif event.key == pygame.K_DOWN:
                        new_x1 = 0
                        new_y1 = -snake_block