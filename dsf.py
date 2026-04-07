class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

# DFS function
def dfs(node, visited):
    if node is None:
        return
    
    # Visit node
    visited.append(node.value)
    
    # Visit all children
    for child in node.children:
        dfs(child, visited)


# Build the example tree
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

root.children = [node2, node3]
node2.children = [node4, node5]
node3.children = [node6, node7]

# Run DFS
visited_nodes = []
dfs(root, visited_nodes)

print("DFS Visited Order:", visited_nodes)