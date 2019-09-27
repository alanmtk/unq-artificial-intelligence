import copy
import random
import json
from queue import PriorityQueue
from time import sleep

rows = 3
cols = 3


# trivial 85
# trivial con costo 23
# wrong numbers 79
# wrong numbers con costo 23
# manhattan 87
# manhattan con costo 23

def _goal():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]


def is_valid_state(state):
    # par = soluble
    # impar = no soluble
    list = [item for sublist in state for item in sublist]
    res = 0
    for i, ii in enumerate(list):
        for j, jj in enumerate(list[1 + 1:]):
            if jj < ii:
                res += 1
    return res % 2 == 0


def random_state():
    numbers = list(range(9))
    random.shuffle(numbers)
    state = []

    for i in range(rows):
        state.append([])
        for j in range(cols):
            state[i].append(numbers.pop())

    if not is_valid_state(state):
        print('Lista random es invalida! Genero otra...')
        return random_state()

    return state


def swap(s, o_r, o_c, d_r, d_c):
    state = copy.deepcopy(s)
    origin = state[o_r][o_c]
    destination = state[d_r][d_c]

    for r, row in enumerate(state):
        for c, column in enumerate(row):
            if (o_r, o_c) == (r, c):
                state[o_r][o_c] = destination
            elif (d_r, d_c) == (r, c):
                state[d_r][d_c] = origin

    return state


# FIXME corresponde que la mala posición del espacio vacío sume 1?
def number_of_wrong_numbers(state):
    goal = _goal()
    wrong_numbers = 0

    for r, row in enumerate(state):
        for c, column in enumerate(row):
            wrong_numbers += 1 if state[r][c] != goal[r][c] else 0

    return wrong_numbers


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def find(state, target):
    for r, row in enumerate(state):
        for c, column in enumerate(row):
            if state[r][c] == target:
                return (r, c)


def sum_of_manhattan_distances(state):
    goal = _goal()
    distance = 0

    for r, row in enumerate(goal):
        for c, column in enumerate(row):
            target = (r, c)
            counterpart = find(state, goal[r][c])
            distance += manhattan_distance(target, counterpart)

    return distance


#
# def trivial_heuristic(state):
#     0 if state == goal() else 0

def possible_moves(state):
    moves = {}
    blank_pos = find(state, 0)

    if blank_pos[0] > 0:  # move up
        label = '↓' + str(state[blank_pos[0] - 1][blank_pos[1]])
        swapped = swap(state, blank_pos[0], blank_pos[1], blank_pos[0] - 1, blank_pos[1])
        moves[label] = swapped
    if blank_pos[0] < (rows - 1):  # move down
        label = '↑️' + str(state[blank_pos[0] + 1][blank_pos[1]])
        swapped = swap(state, blank_pos[0], blank_pos[1], blank_pos[0] + 1, blank_pos[1])
        moves[label] = swapped
    if blank_pos[1] > 0:  # move to left
        label = '→' + str(state[blank_pos[0]][blank_pos[1] - 1])
        swapped = swap(state, blank_pos[0], blank_pos[1], blank_pos[0], blank_pos[1] - 1)
        moves[label] = swapped
    if blank_pos[1] < (cols - 1):  # move to right
        label = '←' + str(state[blank_pos[0]][blank_pos[1] + 1])
        swapped = swap(state, blank_pos[0], blank_pos[1], blank_pos[0], blank_pos[1] + 1)
        moves[label] = swapped

    return moves


def log(node):
    print(node[0])
    print(node[1])
    print(node[2])
    print('')


def gs(graph, initial, h):
    visited = set()
    pqueue = PriorityQueue()
    pqueue.put((h(initial), initial, []))

    while not pqueue.empty():
        priority, node, path = pqueue.get_nowait()
        node_repr = repr(node)

        if priority == 0:
            return node, len(path), len(visited) + 1

        if node_repr not in graph:
            graph[node_repr] = possible_moves(node)

        visited.add(node_repr)

        for label, move in graph[node_repr].items():
            move_repr = repr(move)
            if move_repr not in visited:
                visited.add(move_repr)
                pqueue.put((h(move), move, path + [label]))

    return None


initial_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
# initial_state = [[8, 7, 6], [3, 5, 4], [0, 2, 1]]
# initial_state = [[8, 7, 6], [3, 5, 4], [0, 2, 1]]
# initial_state = [[8, 3, 1], [5, 0, 6], [2, 7, 4]]
# initial_state = [[1, 2, 3], [6, 0, 7], [5, 8, 4]]

# print(gs({}, initial_state, number_of_wrong_numbers))
print(gs({}, initial_state, manhattan_distance))
