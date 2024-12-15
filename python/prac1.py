from collections import deque

def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize queue with the start node
    result = []  # To store the BFS traversal order

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            visited.add(node)  # Mark node as visited
            result.append(node)  # Add it to the result list
            # Add all unvisited neighbors to the queue
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return result

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}

print("BFS Traversal:", bfs(graph, 'A'))

def dfs_recursive(graph, node, visited=None, result=None):
    if visited is None:
        visited = set()  # To keep track of visited nodes
    if result is None:
        result = []  # To store the DFS traversal order

    visited.add(node)  # Mark node as visited
    result.append(node)  # Add it to the result list

    # Visit all unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)

    return result

# Example usage
print("DFS Recursive Traversal:", dfs_recursive(graph, 'A'))
