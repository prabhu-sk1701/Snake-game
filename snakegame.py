import pygame
import time
import random

pygame.init()

color_1 = (255,255,255)
color_2 = (255,255,255)
color_3 = (255,255,255)
color_4 = (255,255,255)
color_5 = (255,255,255)
color_6 = (255,255,255)

screen_length = 900
screen_height = 900
add_caption = pygame.display.set_mode((screen_length, screen_height))

pygame.display.set_caption('Snake Game')

timer = pygame.time.Clock()

snake_block = 10
snake_speed = 10


