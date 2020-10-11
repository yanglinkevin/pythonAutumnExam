#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 找到输入字符串中连续不含重复字符的最长子串。如果有多个相同长度的，只需取第一个。
# @param str string字符串 非空字符串
# @return string字符串
#
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 找到输入字符串中连续不含重复字符的最长子串。如果有多个相同长度的，只需取第一个。
# @param str string字符串 非空字符串
# @return string字符串
#
class Solution:
    def findMaxSubstr(self , str ):
        # write code here
        n = len(str)
        res = 0
        tmpres = 0
        for i in range(n):
            for j in range(i+1, n):
                if len(set(str[i:j]))==j-i:
                    if j-i!=tmpres:
                        tmpres = max(tmpres, j-i)
                        if j-i==tmpres:
                            res = str[i:j]
        return res
                    
                
                    
                
a = "The Linux kernel is an open source software project of fairly large scope."
solution = Solution()
print(solution.findMaxSubstr(a))