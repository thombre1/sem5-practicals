from queue import PriorityQueue

def is_solvable(puzzle):
    inversions = 0
    flat_puzzle = [num for row in puzzle for num in row if num != 0]
    for i in range(len(flat_puzzle)):
        for j in range(i + 1, len(flat_puzzle)):
            if flat_puzzle[i] > flat_puzzle[j]:
                inversions += 1
    return inversions % 2 == 0

def a_star_8_puzzle(start, goal):
    def find_pos(state, value):
        for i, row in enumerate(state):
            if value in row:
                return i, row.index(value)

    def heuristic(state):
        dist = 0
        for i, row in enumerate(state):
            for j, value in enumerate(row):
                if value != 0:
                    goal_i, goal_j = find_pos(goal, value)
                    dist += abs(goal_i - i) + abs(goal_j - j)
        return dist

    pq = PriorityQueue()
    pq.put((0, start, []))
    visited = set()

    while not pq.empty():
        cost, current, path = pq.get()
        if current == goal:
            return path + [current]
        visited.add(tuple(tuple(row) for row in current))
        i, j = find_pos(current, 0)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_state = [row[:] for row in current]
                new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                if tuple(tuple(row) for row in new_state) not in visited:
                    pq.put((cost + 1 + heuristic(new_state), new_state, path + [current]))

# Example usage
start = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
if is_solvable(start):
    solution = a_star_8_puzzle(start, goal)
    for step in solution:
        print(step)
else:
    print("Puzzle is unsolvable")
