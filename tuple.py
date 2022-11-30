print({0, (1, 2)} | {(3, 4, 5)})
print({0, (1, 2)} & {(3, 4, 5)})

# tuple problem
# 1.15.14
S = {-4, -2, 1, 2, 5, 0}
print(([(i, j, k) for i in S for j in S for k in S if i + j + k == 0]))
print(
    ([(i, j, k) for i in S for j in S for k in S if i +
     j + k == 0 and (i, j, k) != (0, 0, 0)])
)

print(list(range(10)))
