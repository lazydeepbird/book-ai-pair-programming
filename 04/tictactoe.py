# pygame을 이용해서 tic-tac-toe 게임을 만들어 보자.
import pygame
import sys
import numpy as np
import time
from pygame.locals import *
# 초기화
pygame.init()
# 색 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
# 화면 크기 설정
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
# 화면 설정
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(WHITE)
# 보드 초기화
board = np.zeros((BOARD_ROWS, BOARD_COLS))
# 선 그리기 함수
def draw_lines():
    # 수평선
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # 수직선
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
# 원 그리기 함수
def draw_circle(row, col):
    pygame.draw.circle(screen, BLUE, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
# X 그리기 함수
def draw_cross(row, col):
    pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
    pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
# 승리 확인 함수

def check_winner(player):
    # 수평 확인
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    # 수직 확인
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # 대각선 확인
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False
# 무승부 확인 함수
def check_draw():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True
# 게임 초기 설정
draw_lines()
player = 1
game_over = False
# 메인 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)
            if board[clicked_row][clicked_col] == 0:
                board[clicked_row][clicked_col] = player
                if player == 1:
                    draw_cross(clicked_row, clicked_col)
                    if check_winner(player):
                        print("Player X wins!")
                        game_over = True
                    player = 2
                else:
                    draw_circle(clicked_row, clicked_col)
                    if check_winner(player):
                        print("Player O wins!")
                        game_over = True
                    player = 1
                if check_draw() and not game_over:
                    print("It's a draw!")
                    game_over = True
    pygame.display.update()
