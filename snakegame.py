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
    
