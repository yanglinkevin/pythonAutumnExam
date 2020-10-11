matrix = []
for i in range(6):
    matrix.append(input())
print(matrix)
visited = [[False for _ in range(8)] for _ in range(8)]
res = 1
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        if matrix[i][j]=='*':
            continue
        x = i + 1
        y = j + 1
        visited[x][y] = True
        tmp = 6
        if visited[x-1][y]==True:
            tmp -= 1
        if visited[x][y-1]==True:
            tmp -= 1
        res *= tmp
print(res)
        
        