
n = int(input())
matrix = []
for i in range(n):
    tmp_input = list(input().split(' '))[1:]
    matrix.append(tmp_input)
dp = [[float('-inf') for _ in range(n*2-1)] for _ in range(n)]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        dp[i][n-1-i+j] = int(matrix[i][j])
for i in range(n):
    dp[i] = dp[i]
print(dp)
m = len(dp[0])
for i in range(n-2, -1, -1):
    for j in range(1, m-1):
        dp[i][j] = max(dp[i+1][j], dp[i+1][j-1], dp[i+1][j+1]) + dp[i][j]
print(dp)
print(max(dp[0]))