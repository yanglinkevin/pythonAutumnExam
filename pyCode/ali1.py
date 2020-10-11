m, n = map(int, input().split(' '))
matrix = [[False for _ in range(m)] for _ in range(4)]
visited = [[False for _ in range(m)] for _ in range(4)]
res = []
def helper(i, j, cnt):
    if i>3 or j>m-1 or visited[i][j]:
        return
    if cnt+1==n:
        res.append(1)
        return
    visited[i][j] = True
    helper(i+1, j, cnt+1)
    helper(i, j+1, cnt+1)
    helper(i, j-1, cnt+1)
    visited[i][j] = False
for i in range(m):
    helper(i, 0, 0)
print(len(res))


    