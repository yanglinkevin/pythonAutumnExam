# 5 6
# X00100
# 00000X
# 01T000
# 0X1010
# 00000X

def helper(i, j, n, m, tmpres, start):
    if visited[i][j] or i<0 or i>n-1 or j<0 or j>m-1 or matrix[i][j]==1:
        return
        #  or matrix[i][j]=='X
    if matrix[i][j] == 'T':
        res.append([tmpres+1,start[0], start[1]])
    visited[i][j] = True
    helper(i+1, j, n, m, tmpres+1, start)
    helper(i-1, j, n, m, tmpres+1, start)
    helper(i, j+1, n, m, tmpres+1, start)
    helper(i, j-1, n, m, tmpres+1, start)
    visited[i][j] = False




n, m = map(int, input().split(' '))
matrix = []
for i in range(n):
    matrix.append(input())

visited = [[False for _ in range(m)] for _ in range(n)]

res = []
for i in range(n):
    for j in range(len(matrix[i])):
        if matrix[i][j]=='X':
            helper(i+1, j, n, m, 0, [i, j])
            helper(i-1, j, n, m, 0, [i, j])
            helper(i, j+1, n, m, 0, [i, j])
            helper(i, j-1, n, m, 0, [i, j])

print(res)
