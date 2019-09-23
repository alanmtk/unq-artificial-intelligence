from collections import deque


def sort(state):
    return ''.join(list(filter(lambda token: token in state, list('👴🥬🐑🐺'))))


def is_valid_move(side):
    return not ('🥬🐑' in side or '🐑🐺' in side)


def expand(state):
    moves = dict()
    _from = 0 if '👴' in state[0] else 1
    _to = 1 if '👴' in state[0] else 0
    _arrow = '->' if _from == 0 else '<-'
    _from_elements = list(state[_from])

    for a in _from_elements:
        moving = ''.join({'👴', a})
        key = _arrow + moving
        _new_origin = sort(''.join(list(filter(lambda e: e not in moving, _from_elements))))
        _new_destination = sort(state[_to] + moving)
        if is_valid_move(_new_origin):
            if _from == 0:
                moves[key] = (_new_origin, _new_destination)
            else:
                moves[key] = (_new_destination, _new_origin)
    return moves


def build_graph():
    graph = dict()
    queue = deque()
    queue.append(('👴🥬🐑🐺', ''))

    while queue:
        node = queue.popleft()
        if node not in graph:
            graph[node] = expand(node)
            neighbors = list(graph[node].values())
            for neighbor in neighbors:
                if neighbor not in graph:
                    queue.append(neighbor)
    return graph


def dfs(graph, initial, is_goal):
    stack = deque()
    visited = set()
    stack.append((initial, []))
    visited.add(initial)
    while stack:
        node, path = stack.pop()
        print(node, path)
        if is_goal(node):
            return path, len(path), len(visited)
        node_edges = graph[node]
        for edge_label, target_node in node_edges.items():
            if target_node not in visited:
                visited.add(target_node)
                stack.append((target_node, path + [edge_label]))
    return None


def bfs(graph, initial, is_goal):
    queue = deque()
    visited = set()
    queue.append((initial, []))
    visited.add(initial)
    while queue:
        node, path = queue.popleft()
        print(node, path)
        if is_goal(node):
            return path, len(path), len(visited)
        node_edges = graph[node]
        for edge_label, target_node in node_edges.items():
            if target_node not in visited:
                visited.add(target_node)
                queue.append((target_node, path + [edge_label]))
    return None


def is_goal(node):
    return node == ('', '👴🥬🐑🐺')


# knowledge representation
graph = build_graph()

print('DFS')
print(dfs(graph, ('👴🥬🐑🐺', ''), is_goal))
print('BFS')
print(bfs(graph, ('👴🥬🐑🐺', ''), is_goal))
