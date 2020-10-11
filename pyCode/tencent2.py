m, n = map(int, input().split(' '))
nums = []
flag_set = set()
for i in range(n):
    tmp = list(map(int, input().split()))[1:]
    if 0 in tmp:
        for j in tmp:
            flag_set.add(j)
    nums.append(tmp)
# print(nums)
for i in range(n):
    for j in range(n):
        tmp = nums[j]
        flag = False
        for k in tmp:
            if k in flag_set:
                flag = True
        if flag:
            for k in tmp:
                flag_set.add(k)
print(len(flag_set))

# res = {}
# i = 0
# while flag_list:
#     tmp = nums[i]
#     for j in tmp:
        