from collections import deque

def water_jug_bfs(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        a, b = queue.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(a, b)
        if a == target or b == target:
            print("Target reached:", a, b)
            return True
        queue.extend([
            (jug1, b),
            (a, jug2),
            (0, b),
            (a, 0),
            (a - min(a, jug2 - b), b + min(a, jug2 - b)),
            (a + min(b, jug1 - a), b - min(b, jug1 - a))
        ])
    return False

jug1 = 4
jug2 = 3
target = 2
water_jug_bfs(jug1, jug2, target)
