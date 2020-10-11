m, n = map(int, input().split(' '))
feature = []
for i in range(n):
    feature.append(int(input()))
result = set()
for i in feature:
    for j in range(1, m+1):
        if j%i==0:
            result.add(j)
print(len(result))
