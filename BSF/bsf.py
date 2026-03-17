from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Shuffled adjacency list
graph = {
    'C': ['F', 'A'],
    'A': ['C', 'B'],
    'F': [],
    'B': ['E', 'D'],
    'E': ['F'],
    'D': []
}

# Start BFS from node 'A'
bfs(graph, 'A')