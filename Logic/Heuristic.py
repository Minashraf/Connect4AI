LENGTH = WIDTH = 7


def calculate_heuristic(grid, human_score, agent_score):
    heuristic = 0
    for i in range(LENGTH):
        for j in range(LENGTH):
            if 0 <= j < WIDTH - 3:
                human, agent = calculate_horizontal(grid, i, j)
                heuristic += agent - human

            if 0 <= i <= LENGTH - 3:
                human, agent = calculate_vertical(grid, i, j)
                heuristic += agent - human

            if 0 <= i <= LENGTH - 3 and 0 <= j <= WIDTH - 3:
                human, agent = calculate_down_diagonal(grid, i, j)
                heuristic += agent - human

            if 0 <= i <= LENGTH - 3 and 3 <= j <= WIDTH:
                human, agent = calculate_up_diagonal(grid, i, j)
                heuristic += agent - human
    return heuristic + agent_score - human_score


def calculate_horizontal(grid, row, col):
    if grid[row][col] == grid[row][col + 1] == grid[row][col + 2] == grid[row][col + 3] == 0:
        return 0, 0
    if grid[row][col] == grid[row][col + 1] == grid[row][col + 2] == grid[row][col + 3] == 1:
        return 10, 0
    if grid[row][col] == grid[row][col + 1] == grid[row][col + 2] == grid[row][col + 3] == 2:
        return 0, 10
    if grid[row][col] == grid[row][col + 1] == grid[row][col + 2] == 1:
        return 5, 0
    if grid[row][col] == grid[row][col + 1] == grid[row][col + 2] == 2:
        return 0, 5
    return 0, 0


def calculate_vertical(grid, row, col):
    if grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == grid[row + 3][col] == 0:
        return 0, 0
    if grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == grid[row + 3][col] == 1:
        return 10, 0
    if grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == grid[row + 3][col] == 2:
        return 0, 10
    if grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == 1:
        return 5, 0
    if grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == 2:
        return 0, 5
    return 0, 0


def calculate_down_diagonal(grid, row, col):
    if grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col + 3] == 0:
        return 0, 0
    if grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col + 3] == 1:
        return 10, 0
    if grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col + 3] == 2:
        return 0, 10
    if grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == 1:
        return 5, 0
    if grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == 2:
        return 0, 5
    return 0, 0


def calculate_up_diagonal(grid, row, col):
    if grid[row][col] == grid[row + 1][col - 1] == grid[row + 2][col - 2] == grid[row + 3][col - 3] == 0:
        return 0, 0
    if grid[row][col] == grid[row + 1][col - 1] == grid[row + 2][col - 2] == grid[row + 3][col - 3] == 1:
        return 10, 0
    if grid[row][col] == grid[row + 1][col - 1] == grid[row + 2][col - 2] == grid[row + 3][col - 3] == 2:
        return 0, 10
    if grid[row][col] == grid[row + 1][col - 1] == grid[row + 2][col - 2] == 1:
        return 5, 0
    if grid[row][col] == grid[row + 1][col - 1] == grid[row + 2][col - 2] == 2:
        return 0, 5
    return 0, 0
