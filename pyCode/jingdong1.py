n = int(input())

res = [2,3,5]
def findN(n):
    if n<=3:
        return res[n-1]
    list = [2,3,5]
    for i in range(3, n):
        for j in list:
            res.append(res[i-3]*10+j)
    return res

result = findN(n)
print(result)
        