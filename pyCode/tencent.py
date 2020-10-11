# n, k = map(int, input().split(' '))
# nums = list(map(int, input().split(' ')))
# nums_dict = {}
# for i in nums:
#     if i not in nums_dict:
#         nums_dict[i] = 1
#     else:
#         nums_dict[i] += 1
# nums_dict[nums[k-1]] -= 1
# for i in nums:
#     if i in nums_dict and nums_dict[i]!=0:
#         print(i, end=' ')
#         nums_dict[i] -= 1

# s = input()
# k = int(input())
# s = sorted(s)
# n = len(s)
# res = []
# def helper():
#     cnt = 0
#     for i in range(n):
#         for j in range(i+1,n+1):
#             if cnt==k:
#                 print(1)
#                 return res
#             tmpres = ''.join(s[i:j])
#             if tmpres not in res:
#                 res.append(tmpres)
#             cnt += 1
# helper()
# print(res[-1])

# 1
# 35  = 17 + 18
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

def helper(num):
    if num<=18:
        return num
    a = num//2
    str_a = str(a)
    while a>0 and str_a[-1]!='9':
        a -= 1
        str_a = str(a)
    b = num - a
    res = 0
    for i in str(b):
        res += int(i)
    for i in str(a):
        res += int(i)
    return res

res = []
for i in range(n):
    res.append(helper(nums[i]))
for i in res:
    print(i)