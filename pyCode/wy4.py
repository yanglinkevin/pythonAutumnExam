m, n = map(int, input().split(' '))   # 3 5
jiedian_list = []
for i in range(n):
    jiedian_list.append(list(map(int, input().split(' '))))
jiedian_list.sort(key=lambda x:[x[2], x[0], x[1]])
# print(jiedian_list)

res = float('inf')
tmpres = float('inf')
for i in range(1, len(jiedian_list)-m+3):
    #bian1 = sorted(jiedian_list[i+m-2][:2])
    #bian2 = sorted(jiedian_list[i][:2])
    # print(jiedian_list)
    # print(bian1, bian2)
    #if bian1!=bian2:
    tmpres = jiedian_list[i+m-3][2]-jiedian_list[i-1][2]
    res = min(res, tmpres)
print(res)
# 5 5
# 1 2 10
# 1 3 5
# 3 1 12
# 2 3 19
# 1 2 74