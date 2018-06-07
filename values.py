import pygame
import random

COLOR = {'player1': pygame.Color('#900382'),
        'player1tail': pygame.Color('#41ba00'),
        'player2': pygame.Color('#7c002d'),
        'player2tail': pygame.Color('#00ffba'),
        'black': pygame.Color('#000000'),
        'red': pygame.Color('#ba0027'),
        'dark_red': pygame.Color('#490815'),
        'gray': pygame.Color('#5c5c5c'),
        'blue': pygame.Color('#1d38c8'),
        'vibrant_green': pygame.Color('#43ee18'),
        'green': pygame.Color('#36bf14'),
        'yellow': pygame.Color('#fff500'),
        'black': pygame.Color('#000000')
}

FPS = 60
CAPTION = 'Znake'
SCREEN_SIZE = (960, 640)
#SCREEN_SIZE = (1920, 1080)
#scale shall have the prime factors 2³ and so shall the values of SCREEN_SIZE
scale = 32
if scale < 8:
    scale = 8
