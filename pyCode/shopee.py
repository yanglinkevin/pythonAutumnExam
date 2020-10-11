# #
# # 
# # @param num1 string字符串 
# # @param num2 string字符串 
# # @return string字符串
# #
# class Solution:
#     def addStrings(self , num1 , num2 ):
#         # write code here
#         n1 = len(nums1)-1
#         n2 = len(nums2)-1
#         tmpres = ''
#         res = ''
#         flag = 0
#         while n1>=0 and n2>=0:
#             tmpres = int(nums1[n1])+int(nums2[n2])+flag
#             flag = 0
#             if tmpres>=10:
#                 flag = 1
#             tmpres = str(tmpres % 10)
#             res = tmpres + res
#             n1 -= 1
#             n2 -= 1
#         while n1>=0:
#             tmpres = int(nums1[n1])+flag
#             flag = 0
#             if tmpres>=10:
#                 flag = 1
#             tmpres = str(tmpres % 10)
#             res = tmpres + res
#             n1 -= 1
#         while n2>=0:
#             tmpres = int(nums2[n2])+flag
#             flag = 0
#             if tmpres>=10:
#                 flag = 1
#             tmpres = str(tmpres % 10)
#             res = tmpres + res
#             n2 -= 1
#         if flag:
#             res = '1' + res
#         return res

# solution = Solution()
# nums1 = "10009"
# nums2 = "990"
# print(solution.addStrings(nums1, nums2))







class Solution:
    def missingNumber(self , nums ):
        # write code here
        for i in range(len(nums)):
            while nums[i]!=i:
                tmp = nums[i]
                nums[i], nums[tmp] = nums[tmp], nums[i]


solution = Solution()
nums = [9,6,4,2,3,5,7,0,1]
print(solution.missingNumber(nums))








# class Solution:
#     def maxSubArray(self , nums ):
#         # write code here
#         res = float('-inf')
#         tmpres = 0
#         for i in range(len(nums)):
#             tmpres += nums[i]
#             res = max(tmpres, res)
#             if tmpres<0:
#                 tmpres = 0
#         return res
            
