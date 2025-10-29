import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    visited = set()
    pq = []
    heapq.heappush(pq, (heuristic[start], start, [start]))
    while pq:
        _, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (heuristic[neighbor], neighbor, path + [neighbor]))
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
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
result = greedy_best_first_search(graph, start, goal, heuristic)

if result:
    print("Path found using GBFS:", " -> ".join(result))
else:
    print("No path found.")
