import pygame,sys

pygame.init()
WIDTH = 600
HEIGHT = 600
LINE_WIDTH= 15
RED =(255, 0, 0)
LINE_COLOR=(23,185,135)
tic_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Let's Play Tic Tac Toe")
Back_ground_color = (28,170,156)
tic_screen.fill(Back_ground_color)


def draw_lines():
    pygame.draw.line(tic_screen,LINE_COLOR,(0 , 200),(600 , 200),LINE_WIDTH)
    pygame.draw.line(tic_screen, LINE_COLOR, (0,400), (600, 400), LINE_WIDTH)
    pygame.draw.line(tic_screen,LINE_COLOR,(200, 0),(200 , 600), LINE_WIDTH)
    pygame.draw.line(tic_screen, LINE_COLOR, (400,0), (400, 600), LINE_WIDTH)


draw_lines()
#mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    pygame.display.update()