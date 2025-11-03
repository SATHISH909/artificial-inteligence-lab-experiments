# Map Coloring Problem using CSP and Backtracking

# Define the map (graph)
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V':  ['SA', 'NSW', 'T'],
    'T':  ['V']
}

# Define available colors
colors = ['Red', 'Green', 'Blue']

# Initialize an empty dictionary to store color assignments
assignment = {}

# Check if the color assignment is valid
def is_valid(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking algorithm
def backtrack(assignment):
    # If all states are assigned, return the solution
    if len(assignment) == len(neighbors):
        return assignment

    # Choose an unassigned state
    unassigned = [state for state in neighbors if state not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color  # Assign color

            # Recursive call
            result = backtrack(assignment)
            if result:
                return result

            # If it didn't lead to a solution, remove the assignment (backtrack)
            del assignment[unassigned]

    return None


# Main Program
if __name__ == "__main__":
    solution = backtrack(assignment)

    if solution:
        print("✅ Map Coloring Solution Found:\n")
        for state, color in solution.items():
            print(f"{state}: {color}")
    else:
        print("❌ No solution found.")
