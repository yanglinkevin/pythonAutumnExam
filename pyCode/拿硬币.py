# leetcode 1561. 你可以获得的最大硬币数目
class Solution:
    def maxCoins(self , piles ):
        # write code here
        piles.sort()
        piles = piles[len(piles)//3:]
        res = 0
        for i in range(len(piles)//2):
            res += piles[i*2]
        return res
            
solution = Solution()
piles = [9,8,7,6,5,1,2,3,4]
print(solution.maxCoins(piles))