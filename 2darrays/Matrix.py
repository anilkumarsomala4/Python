matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
r = len(matrix)
c=len(matrix[0])
sum = 0
for i in range(r):
    for j in range(c):
        sum = sum + matrix[i][j]
print(sum)