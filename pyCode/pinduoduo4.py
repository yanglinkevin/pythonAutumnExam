inlist = input().split()
n, m = int(inlist[0]), int(inlist[1])

dp = [[0]*(1<<n) for i in range(m+2)]

def dfs(i, j, state, nex):
    if j==n:
        dp[i][state] %= 1000000007
        dp[i+1][nex] += dp[i][state]
        dp[i+1][nex] %= 1000000007
        return
    if ((1<<j)&state)>0:
        dfs(i, j+1, state, nex)
    if ((1<<j)&state)==0:
        dfs(i, j+1, state, nex)
    if j+1<n and ((1<<j)&state)==0 and ((1<<(j+1))&state)==0:
        dfs(i, j+2, state, nex|((1<<j)+(1<<(j+1))))
    return

dp[1][0] = 1
for i in range(1, m+1):
    for j in range(1<<n):
        if dp[i][j]:
            dfs(i, 0, j, 0)
print(dp[m+1][0])



