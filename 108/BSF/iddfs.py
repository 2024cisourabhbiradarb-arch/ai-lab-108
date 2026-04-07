# Iterative Deepening Depth First Search (IDDFS)

def dls(graph, node, goal, depth_limit, visited):
    # Depth-Limited Search
    if node == goal:
        return True
    
    if depth_limit <= 0:
        return False
    
    visited.add(node)
    
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dls(graph, neighbor, goal, depth_limit - 1, visited):
                return True
    
    return False


def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        print(f"Searching at depth: {depth}")
        
        if dls(graph, start, goal, depth, visited):
            print(f"Goal {goal} found at depth {depth}")
            return True
    
    print("Goal not found within depth limit")
    return False


# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Run IDDFS
iddfs(graph, 'A', 'G', 3)