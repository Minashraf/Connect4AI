from tkinter.constants import FALSE, NONE
import pygame
import os
import time
import random
import Minmax
from Calculate_score import score_calculator
from Input_Window import popup_box
from Result_Window import print_result

WIN_WIDTH = 750
WIN_HEIGHT = 750
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (25, 25, 112)
BLUE2 = (100, 149, 237)
YELLOW = (255, 255, 0)
HUMAN = 1
AGENT = 2
DEPTH_K = 2
PRUNNING = False
HUMAN_SCORE = 0
AGENT_SCORE = 0
TREE_ROOT = None
NO_MOVES = False
BOARD = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

pygame.init()

font = pygame.font.SysFont('ariel.ttf', 32)

def main():
    global BOARD
    global TREE_ROOT
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Connect 4')
    pygame.display.flip()
    run = True
    player1_turn = random.randint(1, 1000000) % 2 == 0
    while run:
        draw_board(window)

        # AI turn
        if not player1_turn:
            player1_turn = True if agent_turn(window) else False
            def print_tree(root):
                if not root:
                    return
                s = [[str(e) for e in row] for row in root.state]
                lens = [max(map(len, col)) for col in zip(*s)]
                fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
                table = [fmt.format(*row) for row in s]
                print('\n'.join(table))
                print('-'*len(table[-1])*7)
                for child in root.children:
                    print_tree(child)

            os.system('cls' if os.name == 'nt' else 'clear')
            print_tree(TREE_ROOT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif player1_turn and event.type == pygame.MOUSEBUTTONDOWN:
                j, i = pygame.mouse.get_pos()
                i -= 25
                i //= 100
                j -= 25
                j //= 100
                if i < 0 or j < 0 or i >= 6 or j >= 7:
                    continue
                played = insert_tile(window, HUMAN, j)
                if not played:
                    continue
                else:
                    player1_turn = False


def agent_turn(window):
    global NO_MOVES, TREE_ROOT
    played = False
    if DEPTH_K == 0:
        pick_col = random.randint(0, 6)
    else:    
        move, TREE_ROOT = Minmax.decision(BOARD, DEPTH_K, PRUNNING)
        coordinates, score = move
        if not coordinates == None:
            pick_col = coordinates[1]
        else:
            pick_col = None
            NO_MOVES = True
    if not pick_col == None: 
        played = insert_tile(window, AGENT, pick_col)
    return played

# Insert tile in column, if column is full return false indicating that no move was done. Else return true
def insert_tile(window, player, col):
    i = 0
    while i < 6 and BOARD[i][col] == 0:
        BOARD[i][col] = player
        if i > 0:
            BOARD[i - 1][col] = 0
        draw_board(window)
        i += 1
        time.sleep(0.05)
    if i == 0:
        # Could not play
        return False
    else:
        # Played
        global AGENT_SCORE
        global HUMAN_SCORE
        if player == 1:
            HUMAN_SCORE += score_calculator(BOARD, i - 1, col, player)
        else:
            AGENT_SCORE += score_calculator(BOARD, i - 1, col, player)
        return True


def draw_board(window):
    window.fill(WHITE)
    pygame.draw.rect(window, BLUE, pygame.Rect(25, 25, 700, 600))
    for i in range(1, 7):
        pygame.draw.line(window, BLUE2, (25 + i * 100, 25), (25 + i * 100, 625), 3)
    for i in range(1, 6):
        pygame.draw.line(window, BLUE2, (25, 25 + i * 100), (725, 25 + i * 100), 1)
    for i in range(0, 6):
        for j in range(0, 7):
            if BOARD[i][j] == HUMAN:
                color = RED
            elif BOARD[i][j] == AGENT:
                color = YELLOW
            else:
                color = WHITE
            pygame.draw.circle(window, color, (75 + j * 100, 75 + i * 100), 45, 0)
    t1 = font.render("Your  Score: "+str(HUMAN_SCORE), 1, BLUE2)
    t2 = font.render("AI    Score: "+str(AGENT_SCORE), 1, RED)
    window.blit(t1, (25, 700))
    window.blit(t2, (380, 700))
    pygame.display.update()


if __name__ == '__main__':
    DEPTH_K, PRUNNING = popup_box()
    main()
    if HUMAN_SCORE > AGENT_SCORE:
        print_result('Congratulations! You won 😃😃', 'lightgreen')
    elif HUMAN_SCORE == AGENT_SCORE:
        print_result('It is a draw!', 'yellow')
    else:
        print_result('You lost 😭😭', 'red')
