n = int(input())
nums = []
for i in range(n):
    ele = list(map(int, input().split(' ')))
    nums.append(ele[1:])

def helper(ele):
    ele.sort()
    if sum(ele)%4!=0:
        print('NO')
    else:
        target = sum(ele)//4
        mDict = {}
        for i in ele:
            if i not in mDict:
                mDict[i] = 1
            else:
                mDict[i] += 1
        i = 0
        while ele:
            if (target-ele[i]) in mDict:
                ele.pop(index(target-ele[i]))
                ele.pop(i)



        print('YES')

for ele in nums:
    helper(ele)




# def helper(ele):
#     dp = [0 for _ in range(ele[-1]+1)]
#     dp[0] = ele[0]
#     dp[1] = ele[1]
#     for i in range(2, ele[-1]+1):
#         dp[i] = dp[i-2]+dp[i-1]
#     if dp[-1]%3==0:
#         print('YES')
#     else:
#         print('NO')
# n = int(input())
# nums = []
# for i in range(n):
#     ele = list(map(int, input().split(' ')))
#     helper(ele)