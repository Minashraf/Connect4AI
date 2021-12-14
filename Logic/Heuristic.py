from copy import deepcopy

LENGTH = 6 
WIDTH = 7
EMPTY = 0
AI_AGENT = 2
HUMAN = 1

def calculate_heuristic(grid):
    agent = 0
    human = 0
    for i in range(LENGTH):
        for j in range(WIDTH):
            if grid[i][j] == AI_AGENT:
                if j == 3:
                    agent+= 2  
                agent += calculate_horizontal(grid, i, j, AI_AGENT)
                agent += calculate_vertical(grid, i, j, AI_AGENT)
                agent += calculate_sym_diagonal(grid, i, j, AI_AGENT)
                agent += calculate_asym_diagonal(grid, i, j, AI_AGENT)
            elif grid[i][j] == HUMAN:
                if j == 3:
                    human+= 2
                human += calculate_horizontal(grid, i, j, HUMAN)
                human += calculate_vertical(grid, i, j, HUMAN)
                human += calculate_sym_diagonal(grid, i, j, HUMAN)
                human += calculate_asym_diagonal(grid, i, j, HUMAN)
    return agent-human

def calculate_horizontal(grid, row, col, player):
    start = col-3
    while start < 0:
        start+= 1
    end = start+3
    score = 0
    while end < WIDTH:
        line_score = 0
        window = grid[row][start:end+1]
        count_player = window.count(player)
        count_empty = window.count(EMPTY)
        if count_player == 4:
            line_score+= 100
        if count_player == 3 and count_empty == 1:
            line_score+= 10
        if count_player == 2 and count_empty == 2:
            line_score+= 2
        start+= 1
        end+=1
        score+= line_score
    return score

def calculate_vertical(grid, row, col, player):
    start = row+3
    while start >= LENGTH:
        start-= 1
    end = start-3
    score = 0
    while end >= 0:
        line_score = 0
        window = []
        for i in range(end, start+1):
            window.insert(0,grid[i][col])
        count_player = window.count(player)
        count_empty = window.count(EMPTY)
        if count_player == 4:
            line_score+= 100
        if count_player == 3 and count_empty == 1:
            line_score+= 10
        if count_player == 2 and count_empty == 2:
            line_score+= 2
        start-= 1
        end-=1
        score+= line_score
    return score

def calculate_sym_diagonal(grid, row, col, player):
    startI = row-3
    startJ = col-3
    while startI < 0 or startJ < 0:
        startI+= 1
        startJ+= 1
    endI = startI+3
    endJ = startJ+3
    score = 0
    while endI < LENGTH and endJ < WIDTH:
        line_score = 0
        window = []
        for i in range(4):
            window.append(grid[i+startI][i+startJ])
        count_player = window.count(player)
        count_empty = window.count(EMPTY)
        if count_player == 4:
            line_score+= 100
        if count_player == 3 and count_empty == 1:
            line_score+= 10
        if count_player == 2 and count_empty == 2:
            line_score+= 2
        startI+= 1
        startJ+= 1
        endI+= 1
        endJ+= 1
        score+= line_score
    return score

def calculate_asym_diagonal(grid, row, col, player):
    startI = row-3
    startJ = col+3
    while startI < 0 or startJ >= WIDTH:
        startI+= 1
        startJ-= 1
    endI = startI+3
    endJ = startJ-3
    score = 0
    while endI < LENGTH and endJ >= 0:
        line_score = 0
        window = []
        for i in range(4):
            window.append(grid[i+startI][startJ-i])
        count_player = window.count(player)
        count_empty = window.count(EMPTY)
        if count_player == 4:
            line_score+= 100
        if count_player == 3 and count_empty == 1:
            line_score+= 10
        if count_player == 2 and count_empty == 2:
            line_score+= 2
        startI+= 1
        startJ-= 1
        endI+= 1
        endJ-= 1
        score+= line_score
    return score