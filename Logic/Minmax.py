import math
from copy import deepcopy

from pygame.sprite import GroupSingle

from Heuristic import calculate_heuristic

LENGTH = 6 
WIDTH = 7
Agent = 2
Human = 1


class Node:
    parent = None
    children = []
    state = []
    depth = 0
    value = None
    terminal = False
    move_coordinates = []
    minimize = False


def decision(state, maximum_depth, alpha_beta):
    root = Node()
    root.minimize = False
    root.state = state
    return maximize(root, maximum_depth, alpha_beta, -math.inf, math.inf), root


def maximize(node, maximum_depth, alpha_beta, alpha, beta):
    if maximum_depth == 0:
        node.terminal = True
        return None, calculate_heuristic(node.state)
    maximum_value = -math.inf
    maximum_child = None
    for child in make_children(node, Agent):
        move, score = minimize(child, maximum_depth-1, alpha_beta, alpha, beta)
        if score > maximum_value:
            maximum_value = score
            maximum_child = child.move_coordinates
        if alpha_beta:
            if maximum_value >= beta:
                break
            if maximum_value > alpha:
                alpha = maximum_value
    node.value = maximum_value
    return maximum_child, maximum_value


def minimize(node, maximum_depth, alpha_beta, alpha, beta):
    if maximum_depth == 0:
        node.terminal = True
        return None, calculate_heuristic(node.state)
    minimum_value = math.inf
    minimum_child = None
    for child in make_children(node, Human):
        move, score = maximize(child, maximum_depth-1, alpha_beta, alpha, beta)
        if score < minimum_value:
            minimum_value = score
            minimum_child = child.move_coordinates
        if alpha_beta:
            if minimum_value <= alpha:
                break
            if minimum_value < beta:
                beta = minimum_value
    node.value = minimum_value
    return minimum_child, minimum_value


def make_children(node, player):
    children = []
    for j in range(0, WIDTH):
        i = LENGTH-1
        while i >= 0 and node.state[i][j] != 0:
            i-=1
        if i < 0:
            continue
        new_state = deepcopy(node.state)
        new_state[i][j] = player
        child = Node()
        child.parent = node
        child.state = new_state
        child.minimize = not node.minimize
        child.depth = node.depth + 1
        child.move_coordinates = []
        child.move_coordinates.append(i)
        child.move_coordinates.append(j)
        children.append(child)
    node.children = children
    return children
