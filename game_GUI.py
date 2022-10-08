import pygame
from board import *
import math
import numpy as np
import matplotlib.pyplot as plt


BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)

pygame.init()
screen = pygame.display.set_mode((700, 650))
state = True
background = pygame.image.load('board.png')
background = pygame.transform.scale(background,(491,422))
rect = background.get_rect()

rect = rect.move((100,150))
def pygame_drop_piece():
    pass
"""
r = 28 
column 1: 107<x<164, 23<y<569
column 2: [177,239]
column 3: [248,306]
column 4: [318,376]
column 5: [389,446]
column 6: [459,514]
column 7: [529,586]

"""
columns_range = [(107,164),(177,239),(248,306),(318,376),(389,446),(459,514),(529,586)]
row_range = (23,569)
(x0,y0) = (137,186)
target_pos = []
for i in range(0,6):
    sub = []
    for j in range(0,7):
        sub.append((x0+j*70,y0+i*70))
    target_pos = target_pos + [sub]


b = create_board()
col = -1
y = 80
piece = 1
red_pieces = []
blue_pieces = []
done = False

myfont = pygame.font.SysFont("monospace", 75)
font = pygame.font.SysFont(None, 48)
blueWin = font.render('Yellow Won', True, (0,0,255))
redWin = font.render('Red Won', True, (255,0,0))
wrong = font.render('Something Wrong', True, (0,0,0))
while state:

    screen.fill((255, 255, 255))
    screen.blit(background, rect)

    if done:
        if check_win(b) == 1:
            screen.blit(redWin, (40,10))
        elif check_win(b) == -1:
            screen.blit(blueWin,(40,10))
        else:
            screen.blit(wrong, (300, 70))


    for each in red_pieces:
        pygame.draw.circle(screen, (255, 0, 0), each, 28)
    for each in blue_pieces:
        pygame.draw.circle(screen, (255,255,0), each, 28)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           state = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            y = 80
            piece = piece * (-1)
            moving_flag = False
            for c in range(0,len(columns_range)):
                if pos[1]>row_range[0] and pos[1]<row_range[1] and pos[0]>columns_range[c][0] and pos[0]<columns_range[c][1]:
                    col = c
                    break
    if col != -1:
        moving_flag = True
        r = avail_row(b,col)
        x = target_pos[r][col][0]
        if piece == 1:
            pygame.draw.circle(screen, (255, 0, 0), (x, y), 28)
        elif piece ==-1:
            pygame.draw.circle(screen, (255,255,0), (x, y), 28)
        if y<target_pos[r][col][1]:
            y = y + 5
        else:
            y = target_pos[r][col][1]
            if piece == 1:
                red_pieces = red_pieces + [target_pos[r][col]]
                b = drop_piece(b, col, piece)
                col = -1
            else:
                blue_pieces = blue_pieces + [target_pos[r][col]]
                b = drop_piece(b, col, piece)
                y = 80
                piece = piece * (-1)
                [col,score] = minimax(b,3,-100000,1000000,True)
            moving_flag = False

            if check_win(b) == 1 or check_win(b) == -1:

                done = True

    pygame.display.update()




    #pygame.draw.circle(screen, (255,0,0), (137,186), 28)
    #pygame.draw.circle(screen, (255, 0, 0), (137, 256), 28)
    #pygame.draw.circle(screen, (255, 0, 0), (137, 80), 28)
    #pygame.draw.circle(screen, (255, 0, 0), (207, 186), 28)
    #pygame.draw.circle(screen,(255, 0, 0),target_pos[5][5],28)


