matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
r = len(matrix)
c=len(matrix[0])
target = 4
for i in range(r):
    for j in range(c):
        if matrix[i][j] == target:
            print("Element Found")
            break
        