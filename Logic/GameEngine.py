import pygame
import time

WIN_WIDTH   = 750
WIN_HEIGHT  = 650
BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
RED         = (255, 0, 0)
BLUE        = (0,0,205)
BLUE2       = (100,149,237)
YELLOW      = (255, 255, 0)
BOARD       = [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]
            ]

pygame.init()

def main():
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Connect 4')
    window.fill(WHITE)
    pygame.display.flip()
    run = True
    player1_turn = True

    while run:
        draw_board(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                j, i = pygame.mouse.get_pos()
                i-= 25
                i//= 100
                j-= 25
                j//= 100
                if i < 0 or j < 0 or i >= 6 or j >= 7:
                    continue
                played = insert_tile(window, player1_turn, j)
                if not played:
                    continue
                if player1_turn:
                    player1_turn = False
                else:
                    player1_turn = True

#Insert tile in column, if column is full return false indicating that no move was done. Else return true
def insert_tile(window, player1, col):
    i = 0
    val = 1 if player1 else 2
    while i<6 and BOARD[i][col] == 0:
        BOARD[i][col] = val
        if i > 0:
            BOARD[i-1][col] = 0
        draw_board(window)
        i+=1
        time.sleep(0.05)
    if i==0:
        #Could not play
        return False
    else:
        #Played
        return True
        

def draw_board(window):
    pygame.draw.rect(window, BLUE, pygame.Rect(25,25,700,600))
    for i in range(1, 7):
        pygame.draw.line(window, BLUE2, (25+i*100, 25),(25+i*100, 625), 3)
    for i in range(1, 6):
        pygame.draw.line(window, BLUE2, (25, 25+i*100),(725,25+i*100), 1)
    for i in range(0, 6):
        for j in range(0, 7):
            if BOARD[i][j] == 1:
                color = RED
            elif BOARD[i][j] == 2:
                color = YELLOW
            else:
                color = WHITE
            pygame.draw.circle(window, color, (75+j*100, 75+i*100), 50, 0)
    pygame.display.update()

if __name__ == '__main__':
    main()