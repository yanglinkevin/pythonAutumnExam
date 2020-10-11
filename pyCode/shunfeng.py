# 3
# 1 2 5
# 2 7 3
# 5 10 1


n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split(' '))))

dp = [i[-1] for i in data]

res = 0
for i in range(n):
    for j in range(i):
        if data[i][0]>data[j][1]:
            dp[i] = max(dp[i], dp[j]+data[i][-1])
print(max(dp))
