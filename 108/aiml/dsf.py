def dfs(graph, node, goal, visited):
    
    visited.add(node)
    print(node, end=" ")

    if node == goal:
        print("\nGoal node found!")
        return True

    
    for neighbor in graph[node]:
        if neighbor not in visited:
            found = dfs(graph, neighbor, goal, visited)
            if found:
                return True   

    return False




graph = {}


n = int(input("Enter number of nodes: "))


for i in range(n):
    node = input(f"Enter node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors


start = input("Enter starting node: ")


goal = input("Enter goal node: ")


visited = set()
print("DFS Traversal:")

found = dfs(graph, start, goal, visited)

if not found:
    print("\nGoal node not found in the graph.")

    