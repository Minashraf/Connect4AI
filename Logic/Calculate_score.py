def score_calculator(grid, row, col, player):
    score = 0
    if row + 3 < 6:
        score += vertical(grid, row, col, player)
    if col - 3 >= 0:
        score += horizontal(grid, row, col - 3, player)
    if col - 2 >= 0 and col + 1 < 7:
        score += horizontal(grid, row, col - 2, player)
    if col - 1 >= 0 and col + 2 < 7:
        score += horizontal(grid, row, col - 1, player)
    if col + 3 < 7:
        score += horizontal(grid, row, col, player)
    if row - 3 >= 0 and col - 3 >= 0:
        score += lower_diagonal(grid, row - 3, col - 3, player)
    if row - 2 >= 0 and col - 2 >= 0 and row + 1 < 6 and col + 1 < 7:
        score += lower_diagonal(grid, row - 2, col - 2, player)
    if row - 1 >= 0 and col - 1 >= 0 and row + 2 < 6 and col + 2 < 7:
        score += lower_diagonal(grid, row - 1, col - 1, player)
    if row + 3 < 6 and col + 3 < 7:
        score += lower_diagonal(grid, row, col, player)
    if row - 3 >= 0 and col + 3 < 7:
        score += upper_diagonal(grid, row, col, player)
    if row - 2 >= 0 and col + 2 < 7 and row + 1 < 6 and col - 1 >= 0:
        score += upper_diagonal(grid, row + 1, col - 1, player)
    if row - 1 >= 0 and col + 1 < 7 and row + 2 < 6 and col - 2 >= 0:
        score += upper_diagonal(grid, row + 2, col - 2, player)
    if row + 3 < 6 and col - 3 >= 0:
        score += upper_diagonal(grid, row + 3, col - 3, player)
    return score


def vertical(grid, start, col, player):
    if player == 1:
        return 1 if grid[start][col] == 1 and grid[start + 1][col] == 1 and grid[start + 2][col] == 1 and grid[start + 3][col] == 1 else 0
    elif player == 2:
        return 1 if grid[start][col] == 2 and grid[start + 1][col] == 2 and grid[start + 2][col] == 2 and grid[start + 3][col] == 2 else 0

def horizontal(grid, row, start, player):
    if player == 1:
        return 1 if grid[row][start] == 1 and grid[row][start + 1] == 1 and grid[row][start + 2] == 1 and grid[row][start + 3] == 1 else 0
    elif player == 2:
        return 1 if grid[row][start] == 2 and grid[row][start + 1] == 2 and grid[row][start + 2] == 2 and grid[row][start + 3] == 2 else 0


def lower_diagonal(grid, start_row, start_col, player):
    sum = 0
    for i in range(4):
        if grid[start_row + i][start_col + i] == 0 or grid[start_row + i][start_col + i] != player:
            return 0
        sum += grid[start_row + i][start_col + i]
    return 1 if sum == 4 and player == 1 else 1 if sum == 8 and player == 2 else 0


def upper_diagonal(grid, start_row, start_col, player):
    sum = 0
    for i in range(4):
        if grid[start_row - i][start_col + i] == 0 or grid[start_row - i][start_col + i] != player:
            return 0
        sum += grid[start_row - i][start_col + i]
    return 1 if sum == 4 and player == 1 else 1 if sum == 8 and player == 2 else 0
