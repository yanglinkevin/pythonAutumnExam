#维持第yi个美味满足条件
#让第er个热量最小
m, n, target = map(int, input().split())
luch_energy_list = []
dinner_energy_list = []
for i in range(m):
    tmp = list(map(int, input().split()))
    luch_energy_list.append(tmp[::-1])
for i in range(n):
    tmp = list(map(int, input().split()))
    dinner_energy_list.append(tmp[::-1])
luch_energy_list.sort(key=lambda x:[-x[0], x[1]])
dinner_energy_list.sort(key=lambda x:[-x[0], x[1]])
min_hot_energy = float('inf')
tmp_hot_energy = 0
meiwei = 0
flag = 0
if target==0:
    print(0)
else:
    for i in range(len(luch_energy_list)):
        if luch_energy_list[i][0]+dinner_energy_list[0][0]<target:
            break
        meiwei = luch_energy_list[i][0]
        tmp_hot_energy = luch_energy_list[i][1]
        if meiwei>=target and tmp_hot_energy<min_hot_energy:
            flag = 1
            min_hot_energy = tmp_hot_energy
        for j in range(len(dinner_energy_list)):
            meiwei += dinner_energy_list[j][0]
            tmp_hot_energy += dinner_energy_list[j][1]
            if meiwei>=target and tmp_hot_energy<min_hot_energy:
                min_hot_energy = tmp_hot_energy
                flag = 1
            meiwei -= dinner_energy_list[j][0]
            tmp_hot_energy -= dinner_energy_list[j][1]

    for i in range(len(dinner_energy_list)):
        if dinner_energy_list[i][0]>=target and dinner_energy_list[i][1]<min_hot_energy:
            min_hot_energy = dinner_energy_list[i][1]
        else:
            if flag:
                print(min_hot_energy)
            else:
                print(-1)
