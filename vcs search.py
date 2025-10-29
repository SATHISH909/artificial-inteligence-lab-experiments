import heapq

def uniform_cost_search(graph, start, goal):
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start, [start]))
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

start = 'A'
goal = 'F'
path, cost = uniform_cost_search(graph, start, goal)

if path:
    print("Path found using UCS:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("No path found.")
