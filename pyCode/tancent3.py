inlist = input().split()
n, kk = int(inlist[0]), int(inlist[1])
d = {}
for i in range(n):
    tmp = input()
    if tmp in d:
        d[tmp] += 1
    else:
        d[tmp] = 1
k = list(d.keys())
v = list(d.values())
k2, v2 = [], []
for i in range(len(k)):
    k2.append(k[i])
    v2.append(v[i])
for i in range(kk):
    maxj = 0
    for j in range(1, len(k)):
        if v[j]>v[maxj] or (v[j]==v[maxj] and k[j]<k[maxj]):
            maxj = j
    print(k[maxj], end=' ')
    print(v[maxj])
    k.pop(maxj)
    v.pop(maxj)
k = k2
v = v2
for i in range(kk):
    minj = 0
    for j in range(1, len(k)):
        if v[j]<v[minj] or (v[j]==v[minj] and k[j]<k[minj]):
            minj = j
    print(k[minj], end=' ')
    print(v[minj])
    k.pop(minj)
    v.pop(minj)
