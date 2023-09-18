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

board = np.zeros((BOARD_ROWS, BOARD_COLS))


def draw_lines():
    pygame.draw.line(tic_screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(tic_screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(tic_screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(tic_screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


draw_lines()


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


mark_square(0, 0, 1)

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()
