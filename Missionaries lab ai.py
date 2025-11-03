from collections import deque

# State representation: (missionaries_left, cannibals_left, boat_position)
# boat_position = 1 → left side, 0 → right side

def is_valid_state(m_left, c_left):
    """Check if a state is valid."""
    m_right = 3 - m_left
    c_right = 3 - c_left

    # No negative numbers
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False

    # Missionaries should not be outnumbered on either side
    if (m_left > 0 and c_left > m_left) or (m_right > 0 and c_right > m_right):
        return False

    return True


def get_successors(state):
    """Generate possible next states."""
    m_left, c_left, boat = state
    successors = []

    # Possible moves (M, C)
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    for m, c in moves:
        if boat == 1:  # Boat on left side
            new_state = (m_left - m, c_left - c, 0)
        else:           # Boat on right side
            new_state = (m_left + m, c_left + c, 1)

        if is_valid_state(new_state[0], new_state[1]):
            successors.append(new_state)

    return successors


def bfs():
    """Breadth-First Search for the solution."""
    start = (3, 3, 1)
    goal = (0, 0, 0)
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path

        for next_state in get_successors(state):
            queue.append((next_state, path + [next_state]))

    return None


def display_solution(path):
    """Display solution path."""
    print("Missionaries and Cannibals Solution:")
    for step, state in enumerate(path):
        m_left, c_left, boat = state
        m_right = 3 - m_left
        c_right = 3 - c_left
        boat_side = "Left" if boat == 1 else "Right"
        print(f"Step {step}: Left({m_left}M, {c_left}C) | Boat: {boat_side} | Right({m_right}M, {c_right}C)")


if __name__ == "__main__":
    solution = bfs()
    if solution:
        display_solution(solution)
    else:
        print("No solution found.")
