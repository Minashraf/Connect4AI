def score_calculator(grid, row, col, player):
    score = 0
    if row - 4 >= 0:
        score += vertical(grid, row - 4, col, player)
    if col - 4 >= 0:
        score += horizontal(grid, row, col - 4, player)
    if col - 3 >= 0 and col + 1 < 8:
        score += horizontal(grid, row, col - 3, player)
    if col - 2 >= 0 and col + 2 < 8:
        score += horizontal(grid, row, col - 2, player)
    if col - 1 >= 0 and col + 3 < 8:
        score += horizontal(grid, row, col - 1, player)
    if col + 4 < 8:
        score += horizontal(grid, row, col, player)
    if row - 4 >= 0 and col - 4 >= 0:
        score += lower_diagonal(grid, row - 4, col - 4, player)
    if row - 3 >= 0 and col - 3 >= 0 and row + 1 < 7 and col + 1 < 8:
        score += lower_diagonal(grid, row - 3, col - 3, player)
    if row - 2 >= 0 and col - 2 >= 0 and row + 2 < 7 and col + 2 < 8:
        score += lower_diagonal(grid, row - 2, col - 2, player)
    if row - 1 >= 0 and col - 1 >= 0 and row + 3 < 7 and col + 3 < 8:
        score += lower_diagonal(grid, row - 1, col - 1, player)
    if row + 4 < 7 and col + 4 < 8:
        score += lower_diagonal(grid, row, col, player)
    if row - 4 >= 0 and col + 4 < 8:
        score += upper_diagonal(grid, row - 4, col + 4, player)
    if row - 3 >= 0 and col + 3 < 8 and row + 1 < 7 and col - 1 >= 0:
        score += upper_diagonal(grid, row - 3, col + 3, player)
    if row - 2 >= 0 and col + 2 < 8 and row + 2 < 7 and col - 2 >= 0:
        score += upper_diagonal(grid, row - 2, col + 2, player)
    if row - 1 >= 0 and col + 1 < 8 and row + 3 < 7 and col - 3 >= 0:
        score += upper_diagonal(grid, row - 1, col + 1, player)
    if row + 4 < 7 and col - 4 >= 0:
        score += upper_diagonal(grid, row, col, player)
    return score


def vertical(grid, start, col, player):
    if player == 1:
        return 1 if sum(grid[start: start + 4][col]) == 4 else 0
    elif player == 2:
        return 1 if sum(grid[start: start + 4][col]) == 8 else 0


def horizontal(grid, row, start, player):
    if player == 1:
        return 1 if sum(grid[row][start: start + 4]) == 4 else 0
    elif player == 2:
        return 1 if sum(grid[row][start: start + 4]) == 8 else 0


def lower_diagonal(grid, start_row, start_col, player):
    sum = 0
    for _ in range(4):
        sum += grid[start_row][start_col]
        start_row += 1
        start_col += 1
    return 1 if sum == 4 and player == 1 else 1 if sum == 8 and player == 2 else 0


def upper_diagonal(grid, start_row, start_col, player):
    sum = 0
    for _ in range(4):
        sum += grid[start_row][start_col]
        start_row -= 1
        start_col += 1
    return 1 if sum == 4 and player == 1 else 1 if sum == 8 and player == 2 else 0