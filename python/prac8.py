def union_fuzzy(set1, set2):
    return {x: max(set1.get(x, 0), set2.get(x, 0)) for x in set(set1) | set(set2)}

def intersection_fuzzy(set1, set2):
    return {x: min(set1.get(x, 0), set2.get(x, 0)) for x in set(set1) & set(set2)}

def complement_fuzzy(fuzzy_set):
    return {x: 1 - membership for x, membership in fuzzy_set.items()}

# Example fuzzy sets
set1 = {'a': 0.5, 'b': 0.7, 'c': 0.2}
set2 = {'a': 0.8, 'b': 0.4, 'd': 0.6}

print("Union:", union_fuzzy(set1, set2))
print("Intersection:", intersection_fuzzy(set1, set2))
print("Complement of set1:", complement_fuzzy(set1))
