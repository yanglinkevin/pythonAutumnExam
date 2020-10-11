n = int(input())
nums = list(input().split(' '))
nums.sort()
nums = nums[::-1]
cnt = 0
for i in range(len(nums)):
    if nums[i]=='5':
        cnt += 1
    else:
        break
number_of_nine = cnt - cnt % 9
res = number_of_nine * '5' + (len(nums)-cnt) * '0'
print(int(res))


