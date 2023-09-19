import pygame
import sys
import numpy as np

pygame.init()
WIDTH = 600
HEIGHT = WIDTH
BOARD_ROWS = 3
BOARD_COLS = 3
SQURE_SIZE = WIDTH // BOARD_COLS
LINE_WIDTH = 15
RED = (255, 0, 0)
LINE_COLOR = (23, 185, 135)
tic_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Let's Play Tic Tac Toe")
Background_color = (28, 170, 156)
tic_screen.fill(Background_color)
CIRCLE_RADIUS = SQURE_SIZE // 3
CIRCLE_WIDTH = SQURE_SIZE //13
CIRCLE_COLOR = (239, 234, 200)
CROSS_WIDTH = SQURE_SIZE //8
SPACE = SQURE_SIZE // 4
CROSS_COLOR = (66, 66, 66)
board = np.zeros((BOARD_ROWS, BOARD_COLS))


def draw_lines():
    pygame.draw.line(tic_screen, LINE_COLOR, (0, SQURE_SIZE), (WIDTH, SQURE_SIZE), LINE_WIDTH)
    pygame.draw.line(tic_screen, LINE_COLOR, (0, SQURE_SIZE * 2), (WIDTH, SQURE_SIZE * 2), LINE_WIDTH)
    pygame.draw.line(tic_screen, LINE_COLOR, (0, SQURE_SIZE), (HEIGHT, SQURE_SIZE), LINE_WIDTH)
    pygame.draw.line(tic_screen, LINE_COLOR, (SQURE_SIZE, 0), (SQURE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(tic_screen, LINE_COLOR, (SQURE_SIZE * 2, 0), (SQURE_SIZE * 2, HEIGHT), LINE_WIDTH)


def draw_figuers():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(tic_screen, CIRCLE_COLOR, (int(col * SQURE_SIZE + SQURE_SIZE / 2), int(row * SQURE_SIZE + SQURE_SIZE/2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(tic_screen, CROSS_COLOR, (col * SQURE_SIZE + SPACE, row * SQURE_SIZE + SQURE_SIZE - SPACE),
                                 (col * SQURE_SIZE + SQURE_SIZE - SPACE, row * SQURE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(tic_screen, CROSS_COLOR, (col * SQURE_SIZE + SPACE, row * SQURE_SIZE + SPACE),
                                 (col * SQURE_SIZE + SQURE_SIZE - SPACE, row * SQURE_SIZE + SQURE_SIZE - SPACE), CROSS_WIDTH)


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
gameOver = False


def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            draw_verticl_winning_line(col, player)
            return True
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            draw_horizal_winning_line(row, player)
            return True

        if board[2][0] == board[1][1] == board[0][2] == player:
            draw_asc_diagonal(player)
            return True

        if board[0][0] == board[1][1] == board[2][2] == player:
            draw_desc_diagnoal(player)
            return True


def draw_verticl_winning_line(col, player):
    posX = col * SQURE_SIZE + SQURE_SIZE // 2
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR

    pygame.draw.line(tic_screen, color, (posX, 15), (posX, HEIGHT - 15), 20)


def draw_horizal_winning_line(row, player):
    posY = row * SQURE_SIZE + SQURE_SIZE //2
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    pygame.draw.line(tic_screen, color, (15, posY), (WIDTH - 15, posY), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR

    pygame.draw.line(tic_screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagnoal(player):
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    pygame.draw.line(tic_screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 20)


def restart():
    tic_screen.fill(Background_color)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
    draw_figuers()


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // SQURE_SIZE)
            clicked_col = int(mouseX // SQURE_SIZE)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                gameOver = check_win(player)
                if player == 1:
                    player = 2
                elif player == 2:
                    player = 1
                draw_figuers()


    pygame.display.update()
