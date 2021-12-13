import math
from copy import deepcopy

from Logic.Heuristic import calculate_heuristic

LENGTH = 6 
WIDTH = 7
Agent = 'AGENT'
Human = 'HUMAN'


class Node:
    parent = None
    children = []
    state = []
    depth = 0
    value = None
    terminal = False
    human_score = 0
    agent_score = 0
    minimize = False
    change = None


def decision(state, maximum_depth, alpha_beta, human_score, agent_score):
    root = Node()
    root.minimize = False
    root.state = state
    root.human_score = human_score
    root.agent_score = agent_score
    return maximize(root, maximum_depth, alpha_beta, -math.inf, math.inf), root


def maximize(node, maximum_depth, alpha_beta, alpha, beta):
    if not (maximum_depth > 0 and 0 in node.state):
        node.terminal = True
        return None, calculate_heuristic(node.state, node.human_score, node.agent_score)
    maximum_value = -math.inf
    maximum_child = None
    for child in make_children(node, Agent):
        score = minimize(node, maximum_depth - 1, alpha_beta, alpha, beta)[1]
        if score > maximum_value:
            maximum_value = score
            maximum_child = child.state
        if alpha_beta:
            if maximum_value >= beta:
                break
            if maximum_value > alpha:
                alpha = maximum_value
    node.value = maximum_value
    return maximum_child, maximum_value


def minimize(node, maximum_depth, alpha_beta, alpha, beta):
    if not (maximum_depth > 0 and 0 in node.state):
        node.terminal = True
        return None, calculate_heuristic(node.state, node.human_score, node.agent_score)
    minimum_value = math.inf
    minimum_child = None
    for child in make_children(node, Human):
        score = maximize(node, maximum_depth - 1, alpha_beta, alpha, beta)[1]
        if score < minimum_value:
            minimum_value = score
            minimum_child = child.state
        if alpha_beta:
            if minimum_value <= alpha:
                break
            if minimum_value < beta:
                beta = minimum_value
    node.value = minimum_value

    return minimum_child, minimum_value


def make_children(node, player):
    children = []
    for i in range(LENGTH):
        for j in range(WIDTH):
            if node.state[i][j] == 0:
                if i < LENGTH - 1 and node.state[i + 1][j] != 0 or i == LENGTH - 1:
                    new_state = deepcopy(node.state)
                    new_state[i][j] = 1 if player == Human else 2
                    child = Node()
                    child.parent = node
                    child.state = new_state
                    child.minimize = not node.minimize
                    child.change = j
                    child.depth = node.depth + 1
                    children.append(child)
    node.children = children
    return children
