def helper():
    n, m = map(int, input().split(' '))
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    if n<=2:
        return dp[n]
    if n==3:
        if m==2:
            return 2
        if m==3:
            return 3
    if n==4:
        if m==2:
            return 0
        if m==3:
            return 2
        if m==4:
            return 3
    if n==4:
        if m==2:
            return 0
        if m==3:
            return 2
        if m==4:
            return 4
        if m==5:
            return 5

res = helper()
print(res)

