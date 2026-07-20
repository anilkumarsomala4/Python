matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
r = len(matrix)
c=len(matrix[0])
evencount = 0
oddcount = 0
for i in range(r):
    for j in range(c):
        if matrix[i][j] % 2 == 0:
            evencount =  evencount + 1
        else:
            oddcount = oddcount + 1
print("even Count",evencount)
print("odd count",oddcount)