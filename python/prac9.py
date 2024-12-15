from constraint import Problem

# Example CSP: Assign colors to states with no adjacent states having the same color
def csp_example():
    problem = Problem()
    variables = ['A', 'B', 'C', 'D']
    domain = ['Red', 'Green', 'Blue']
    
    # Add variables and domain
    for variable in variables:
        problem.addVariable(variable, domain)
    
    # Add constraints
    problem.addConstraint(lambda a, b: a != b, ('A', 'B'))
    problem.addConstraint(lambda a, b: a != b, ('B', 'C'))
    problem.addConstraint(lambda a, b: a != b, ('C', 'D'))
    problem.addConstraint(lambda a, b: a != b, ('D', 'A'))
    
    solutions = problem.getSolutions()
    return solutions

print("Solutions:", csp_example())
