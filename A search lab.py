import heapq

def a_star_search(graph, start, goal, heuristic):
    visited = set()
    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, [start]))
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            return path, g
        if node not in visited:
            visited.add(node)
            for neighbor, cost in graph.get(node, []):
                if neighbor not in visited:
                    new_g = g + cost
                    new_f = new_g + heuristic[neighbor]
                    heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
    return None, float('inf')

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 7,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'
path, cost = a_star_search(graph, start, goal, heuristic)

if path:
    print("Path found using A* Search:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found.")
