# m, n = map(int, input().split(' '))
# nums = list(map(int, input().split(' ')))

'''
m, n = 5, 3
nums = [1,2,3,4,5]
def calc(nums, lenth, k):
    res = 0
    left = 0
    right = lenth
    tmpres = 0
    if lenth==1:
        for i in range(len(nums)):
            res += 1 if nums[i]%k==0 else 0
        return res
    for i in range(lenth):
        tmpres += nums[i]
    if tmpres%k==0 and lenth==len(nums):
        res += 1
    while left<=right and right<=len(nums) and right-left==lenth:
        if tmpres%k==0:
            res += 1
        tmpres -= nums[left]
        if right==len(nums):
            break
        tmpres += nums[right]
        left += 1
        right += 1
    return res

result = 0
for i in range(1, m+1):
    result += calc(nums, i, n)
print(result)
            
'''






# Q2:
n = 2
nums = [1,1,2,1,3,5,1,1,1,3,3,3]

dp = [[1 for _ in range(len(nums))] for _ in range(len(nums))]

for i in range(len(nums)):
    for j in range(i-1, -1, -1):
        if nums[i]==nums[j]:
            dp[j][i] = dp[j+1][i] + 1
        for k in range(n):
            dp[j][i] = max(dp[j][i], dp[j-k][i])
print(dp)
print(max(max(dp)))







'''




m, n = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
sortedNums = sorted(nums)
cntDict = {}
for i in range(len(sortedNums)):
    if sortedNums[i] in cntDict:
        cntDict[sortedNums[i]] += 1
    else:
        cntDict[sortedNums[i]] = 1
res = []
tmpnums = []
for i in range(len(sortedNums)):
    tmpnums.append(sortedNums[i]^nums[i])

res = {}
cnt = 0
for i in range(len(tmpnums)):
    if tmpnums[i]!=0:
        if sortedNums[i] in res:
            res[sortedNums[i]] += 1
        else:
            res[sortedNums[i]] = 1
result = 0
for i in res:
    if res[i]<=k:
        result = max(result, cntDict[i])
print(nums)
print(sortedNums)
print(tmpnums)
print(cntDict)
print(res)
print(result)


    '''