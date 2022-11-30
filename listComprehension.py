# Example 1. list comprehension

print([2*x for x in {1, 2, 3, 4, 5}])


# Example 2. Nested list Comprehension

print([x*y for x in [1, 2, 3] for y in [10, 20, 30]])
print([[x, y] for x in ['A', 'B', 'C'] for y in [1, 2, 3]])


# Example 3. List indexing

a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
# Suffix
print(a[1:])  # Start from Egg to lobster
# prefix
print(a[:5])

# Extended slices
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L[::2])  # result : [0, 2, 4, 6, 8]
print(L[1::2])  # index 1 two space
print(L[1:6:2])  # [1,3,5]
