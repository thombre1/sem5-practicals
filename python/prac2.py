from collections import deque

def water_jug_problem(m, n, d):
    # Check if the target is achievable
    if d > max(m, n) or d % gcd(m, n) != 0:
        return "Solution not possible"
    
    # BFS queue: (current state of jugs)
    queue = deque([(0, 0)])  # (jug1, jug2)
    visited = set()  # To track visited states
    steps = []

    while queue:
        jug1, jug2 = queue.popleft()

        # If we reach the target
        if jug1 == d or jug2 == d:
            steps.append((jug1, jug2))
            return steps

        # Mark the current state as visited
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        steps.append((jug1, jug2))

        # Possible moves
        moves = [
            (m, jug2),  # Fill Jug1
            (jug1, n),  # Fill Jug2
            (0, jug2),  # Empty Jug1
            (jug1, 0),  # Empty Jug2
            (min(jug1 + jug2, m), jug1 + jug2 - min(jug1 + jug2, m)),  # Pour Jug2 -> Jug1
            (jug1 + jug2 - min(jug1 + jug2, n), min(jug1 + jug2, n))   # Pour Jug1 -> Jug2
        ]

        # Add all possible moves to the queue
        for move in moves:
            if move not in visited:
                queue.append(move)

    return "No solution"

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
m, n, d = 4, 3, 2  # Jug capacities and target
solution = water_jug_problem(m, n, d)
print("Steps to solve the problem:", solution)
