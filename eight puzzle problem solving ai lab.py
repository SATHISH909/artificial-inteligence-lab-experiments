from heapq import heappush, heappop

# Goal state configuration
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the blank tile

# Helper function to find the position of a number in a state
def find_pos(state, value):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j

# Manhattan distance heuristic function
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = find_pos(goal_state, val)
                distance += abs(goal_i - i) + abs(goal_j - j)
    return distance

# Generate possible moves from the current state
def get_neighbors(state):
    i, j = find_pos(state, 0)
    moves = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row[:] for row in state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
            moves.append(new_state)
    return moves

# Convert a 2D list state into a tuple for hashing
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

# A* Search algorithm
def solve_puzzle(start_state):
    pq = []
    heappush(pq, (manhattan_distance(start_state), 0, start_state, []))
    visited = set()

    while pq:
        f, g, current, path = heappop(pq)
        if current == goal_state:
            return path + [current]

        visited.add(state_to_tuple(current))

        for neighbor in get_neighbors(current):
            if state_to_tuple(neighbor) not in visited:
                heappush(pq, (g + 1 + manhattan_distance(neighbor),
                              g + 1,
                              neighbor,
                              path + [current]))
    return None

# Pretty-print a state
def print_state(state):
    for row in state:
        print(row)
    print()

# Example usage
if __name__ == "__main__":
    # Define initial state (0 = blank)
    start_state = [[1, 2, 3],
                   [4, 0, 6],
                   [7, 5, 8]]

    print("Initial State:")
    print_state(start_state)

    print("Solving...\n")
    solution = solve_puzzle(start_state)

    if solution:
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            print_state(state)
        print("Goal Reached!")
    else:
        print("No solution found.")
