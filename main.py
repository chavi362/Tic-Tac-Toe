import pygame
import sys
import numpy as np


pygame.init()
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
RED = (255, 0, 0)
LINE_COLOR = (23, 185, 135)
tic_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Let's Play Tic Tac Toe")
Background_color = (28, 170, 156)
tic_screen.fill(Background_color)
CIRCLE_RADIUS =60
CIRCLE_WIDTH =15
CIRCLE_COLOR =(239, 234, 200)
CROSS_WIDTH = 25
SPACE = 45
CROSS_COLOR=(66,66,66)
board = np.zeros((BOARD_ROWS, BOARD_COLS))


def draw_lines():
    pygame.draw.line(tic_screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(tic_screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(tic_screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(tic_screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def draw_figuers():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(tic_screen, CIRCLE_COLOR, (int( col * 200 + 200/2), int (row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(tic_screen, CROSS_COLOR, (col*200 +SPACE, row*200+200-SPACE),(col*200 +200-SPACE, row* 200+SPACE),CROSS_WIDTH)
                pygame.draw.line(tic_screen, CROSS_COLOR, (col*200 + SPACE, row*200+SPACE),(col*200 +200- SPACE, row* 200+200- SPACE),CROSS_WIDTH)



def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

draw_lines()
player = 1
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row= int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row , clicked_col):
                mark_square(clicked_row,clicked_col,player)
                if player == 1:
                    player = 2
                elif player == 2:
                    player = 1
            draw_figuers()

    pygame.display.update()
