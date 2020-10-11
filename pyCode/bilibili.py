class Solution:
    def GetCoinCount(self , N ):
        # write code here
        N = 1024 - N
        res = 0 
        while N>0:
            if N>=64:
                N -= 64
            elif N>=16:
                N -= 16
            elif N>=4:
                N -= 4
            elif N>=1:
                N -= 1
            elif N==0:
                return res
            res += 1
        return res                

N = 200
solution = Solution()
print(solution.GetCoinCount(N))