import itertools

# Function to calculate total distance of a given route
def total_distance(route, graph):
    distance = 0
    for i in range(len(route) - 1):
        distance += graph[route[i]][route[i + 1]]
    # Return to the starting city
    distance += graph[route[-1]][route[0]]
    return distance


# Function to solve the TSP problem using brute force
def travelling_salesman(graph):
    cities = list(graph.keys())
    best_route = None
    min_distance = float('inf')

    # Generate all possible city permutations (routes)
    for perm in itertools.permutations(cities):
        current_distance = total_distance(perm, graph)
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = perm

    return best_route, min_distance


# Example graph: distances between cities
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

# Run the algorithm
best_route, min_distance = travelling_salesman(graph)

# Display result
print("Optimal Route:", " → ".join(best_route))
print("Minimum Distance:", min_distance)
