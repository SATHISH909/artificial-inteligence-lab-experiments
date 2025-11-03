import itertools

# Function to solve the crypt-arithmetic puzzle
def solve_cryptarithmetic():
    # Each unique letter in the puzzle
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    
    # Digits 0–9 will be assigned to letters
    digits = range(10)
    
    # Generate all possible digit assignments
    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))
        
        # Leading letters can't be zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue
        
        # Construct the numerical values based on letter–digit mapping
        send = mapping['S']*1000 + mapping['E']*100 + mapping['N']*10 + mapping['D']
        more = mapping['M']*1000 + mapping['O']*100 + mapping['R']*10 + mapping['E']
        money = mapping['M']*10000 + mapping['O']*1000 + mapping['N']*100 + mapping['E']*10 + mapping['Y']
        
        # Check if the equation holds
        if send + more == money:
            print("Solution Found:")
            print(f"SEND = {send}")
            print(f"MORE = {more}")
            print(f"MONEY = {money}")
            print("\nMapping:", mapping)
            return

    print("No solution found.")

# Run the solver
if __name__ == "__main__":
    solve_cryptarithmetic()
