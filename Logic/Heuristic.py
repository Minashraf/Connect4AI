LENGTH = 6
WIDTH = 7
EMPTY = 0
AI_AGENT = 2
HUMAN = 1
SCORE_4 = 1000
SCORE_3 = 50
SCORE_2 = 5
SCORE_MID = 2


def calculate_heuristic(grid):
    agent = 0
    human = 0
    for i in range(LENGTH):
        for j in range(WIDTH):

            def calculate(player, col_index):
                score = 0
                if col_index == 3:
                    score += SCORE_MID
                score += calculate_horizontal(grid, i, col_index, player)
                score += calculate_vertical(grid, i, col_index, player)
                score += calculate_sym_diagonal(grid, i, col_index, player)
                score += calculate_asym_diagonal(grid, i, col_index, player)
                return score

            if grid[i][j] == AI_AGENT:
                agent += calculate(AI_AGENT, j)
            elif grid[i][j] == HUMAN:
                human += calculate(HUMAN, j)

    return agent - human


def calculate_horizontal(grid, row, col, player):
    start = col - 3
    while start < 0:
        start += 1
    end = start + 3
    score = 0
    while end < WIDTH:
        window = grid[row][start:end + 1]
        line_score = count_score(window, player)
        start += 1
        end += 1
        score += line_score
    return score


def calculate_vertical(grid, row, col, player):
    start = row + 3
    while start >= LENGTH:
        start -= 1
    end = start - 3
    score = 0
    while end >= 0:
        window = []
        for i in range(end, start + 1):
            window.insert(0, grid[i][col])
        line_score = count_score(window, player)
        start -= 1
        end -= 1
        score += line_score
    return score


def calculate_sym_diagonal(grid, row, col, player):
    start_i = row - 3
    start_j = col - 3
    while start_i < 0 or start_j < 0:
        start_i += 1
        start_j += 1
    end_i = start_i + 3
    end_j = start_j + 3
    score = 0
    while end_i < LENGTH and end_j < WIDTH:
        window = []
        for i in range(4):
            window.append(grid[i + start_i][i + start_j])
        line_score = count_score(window, player)
        start_i += 1
        start_j += 1
        end_i += 1
        end_j += 1
        score += line_score
    return score


def calculate_asym_diagonal(grid, row, col, player):
    start_i = row - 3
    start_j = col + 3
    while start_i < 0 or start_j >= WIDTH:
        start_i += 1
        start_j -= 1
    end_i = start_i + 3
    end_j = start_j - 3
    score = 0
    while end_i < LENGTH and end_j >= 0:
        window = []
        for i in range(4):
            window.append(grid[i + start_i][start_j - i])
        line_score = count_score(window, player)
        start_i += 1
        start_j -= 1
        end_i += 1
        end_j -= 1
        score += line_score
    return score


def count_score(window, player):
    count_player = window.count(player)
    count_empty = window.count(EMPTY)
    if count_player == 4:
        return SCORE_4
    elif count_player == 3 and count_empty == 1:
        return SCORE_3
    elif count_player == 2 and count_empty == 2:
        return SCORE_2
    return 0
