from collections import deque

PROBLEM_GRAPH = {
    ('👴🥬🐑🐺', ''): {
        '->️👴🐑': ('🥬🐺', '👴🐑'),
    },
    ('👴🥬🐑', '🐺'): {
        '->️👴🐑': ('🥬', '👴🐑🐺'),
        '->️👴🥬': ('🐑', '👴🥬🐺'),
    },
    ('👴🥬🐺', '🐑'): {
        '->️👴🥬': ('🐺', '👴🥬🐑'),
        '->️👴🐺': ('🥬', '👴🐑🐺'),
        '->️👴': ('🥬🐺', '👴🐑'),
    },
    ('👴🐑🐺', '🥬'): {
        '->️👴🐑': ('🐺', '👴🥬🐑'),
        '->️👴🐺': ('🐑', '👴🥬🐺'),
    },
    ('🥬🐺', '👴🐑'): {
        '<-️👴': ('👴🥬🐺', '🐑'),
        '<-️👴🐑': ('👴🥬🐑🐺', ''),
    },
    ('👴🐑', '🥬🐺'): {
        '->️👴🐑': ('', '👴🥬🐑🐺'),
        '->️👴': ('🐑', '👴🥬🐺'),
    },
    ('🥬', '👴🐑🐺'): {
        '️<-👴🐑': ('👴🥬🐑', '🐺'),
        '️<-👴🐺': ('👴🥬🐺', '🐑'),
    },
    ('🐑', '👴🥬🐺'): {
        '️<-👴🥬': ('👴🥬🐑', '🐺'),
        '️<-👴🐺': ('👴🐑🐺', '🥬'),
        '️<-👴': ('👴🐑', '🥬🐺'),
    },
    ('🐺', '👴🥬🐑'): {
        '️<-👴🐑': ('👴🐑🐺', '🥬'),
        '️<-👴🥬': ('👴🥬🐺', '🐑'),
    },
    ('', '👴🥬🐑🐺'): {
        '<-️👴🐑': ('👴🐑', '🥬🐺'),
    },
}


def dfs(graph, initial, is_goal):
    stack = deque()
    visited = set()
    stack.append((initial, []))
    visited.add(initial)
    while stack:
        node, path = stack.pop()
        if is_goal(node):
            return node, path
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
        if is_goal(node):
            return node, path
        node_edges = graph[node]
        for edge_label, target_node in node_edges.items():
            if target_node not in visited:
                visited.add(target_node)
                queue.append((target_node, path + [edge_label]))
    return None


def is_goal(node):
    return node == ('', '👴🥬🐑🐺')


print(dfs(PROBLEM_GRAPH, ('👴🥬🐑🐺', ''), is_goal))

print(bfs(PROBLEM_GRAPH, ('👴🥬🐑🐺', ''), is_goal))
