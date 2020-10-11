n = int(input())
inlist = input().split()
v = []
for i in range(n):
    inlist[i] = int(inlist[i])
    v.append(inlist[i])
v.sort()
big = v[n//2]
small = v[n//2-1]
for i in range(n):
    if inlist[i]<big:
        print(big)
    else:
        print(small)
