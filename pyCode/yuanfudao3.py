n = int(input())
# res = 1
# for i in range(1, n+1):
#     res *= i
result = 0

def helper(n):
    if n==0:
        return 1
    if n==1:
        return n
    return helper(n%2)*helper(n//2)*helper(n//2)
res = helper(n)
print(res)
for i in str(res)[::-1]:
    if i=='0':
        result += 1
    else:
        break
print(result)
