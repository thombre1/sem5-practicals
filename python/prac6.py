from itertools import permutations

def traveling_salesman_problem(distances):
    cities = range(len(distances))
    shortest_path = None
    min_cost = float('inf')
    
    for path in permutations(cities):
        cost = sum(distances[path[i]][path[i + 1]] for i in range(len(path) - 1))
        cost += distances[path[-1]][path[0]]  # Return to the start city
        if cost < min_cost:
            min_cost = cost
            shortest_path = path
    
    return min_cost, shortest_path

# Example usage
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
cost, path = traveling_salesman_problem(distance_matrix)
print(f"Shortest path: {path} with cost: {cost}")
