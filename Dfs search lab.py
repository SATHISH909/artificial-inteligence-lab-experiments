def dfs_search(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    visited.add(start)
    if start == goal:
        return path
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = dfs_search(graph, neighbor, goal, path + [neighbor], visited)
            if new_path:
                return new_path
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
goal = 'F'
result = dfs_search(graph, start, goal)

if result:
    print("Path found using DFS:", " -> ".join(result))
else:
    print("No path found.")
