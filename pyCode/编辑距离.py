#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param a string字符串 字符串1
# @param b string字符串 字符串2
# @return int整型
#
class Solution:
    def minDistance(self , a , b ):
        # write code here
        m = len(a)
        n = len(b)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if a[0]!=b[0]:
            dp[0][0] = 1
        else:
            dp[0][0] = 0
        for i in range(1, m):
            dp[i][0] = i + dp[0][0]
        for j in range(1, n):
            dp[0][j] = j + dp[0][0]
        for i in range(1, m):
            for j in range(1, n):
                if a[i]!=b[j]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = dp[i-1][j-1]                
        return dp[-1][-1]

a = "horse"
b = "rose"
solution = Solution()
print(solution.minDistance(a, b))