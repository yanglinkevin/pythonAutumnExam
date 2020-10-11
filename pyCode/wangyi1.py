m, n = map(int, input().split(' '))   # 5 2
numbers = list(map(int, input().split(' ')))   # 4 100
result = [i for i in range(1, m+1)]
result_set = set(result)
for i in numbers:
    if i in result_set:
        result_set.remove(i)
result = list(result_set)[:m-n]    # [1,3,5]
result_set = set(result)

def insert(number, index):
    for j in range(index, len(result)):
        if number<result[j]:
            result.insert(j, number)
            return j+1
    result.append(number)
    return j+1
index = 0
for number in numbers:
    index = insert(number, index)
res = []
for i in result:
    res.append(str(i))

print(' '.join(res))

