def dls(graph, node, goal, depth, visited=None):
    if visited is None:
        visited = set()

    print(node, end=" ")
    visited.add(node)

    if node == goal:
        return True

    if depth <= 0:
        return False

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dls(graph, neighbor, goal, depth - 1, visited):
                return True

    return False
graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")
limit = int(input("Enter depth limit: "))

print("DLS traversal:")
found = dls(graph, start, goal, limit)

if found:
    print("\nGoal found within depth limit")
else:
    print("\nGoal not found within depth limit")