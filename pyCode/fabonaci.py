n = int(input())
res = []
res.append(1)
res.append(1)
for i in range(2, n*n):
    res.append(res[i-1]+res[i-2])
result = [[0 for _ in range(n)] for _ in range(n)]
up = 0
down = n-1
left = 0
right = n-1
n = n * n
cnt = n-1
i = 0
j = 0
while left<=right and up<=down and cnt>=0:
    while i<=right and left<=right:
        result[up][i] = res[cnt]
        i += 1
        cnt -= 1
    up += 1
    j = up
    while j<=down and up<=down:
        result[j][right] = res[cnt]
        j += 1
        cnt -= 1
    right -= 1
    i = right
    while i>=left and left<=right:
        result[down][i] = res[cnt]
        i -= 1
        cnt -= 1
    down -= 1
    j = down
    while j>=up and up<=down:
        result[j][left] = res[cnt]
        j -= 1
        cnt -= 1
    left += 1
    i = left
for i in range(len(result)):
    for j in range(len(result)):
        print(result[i][j], end=' ')
    print('')
