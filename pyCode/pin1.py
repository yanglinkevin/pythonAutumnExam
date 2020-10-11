target, steps = map(int, input().split(' '))
step_list = list(map(int, input().split(' ')))
res = 0
back_numbers = 0
for i in range(steps):
    res += step_list[i]
    if res==target:
        print('paradox')
    elif res>target:
        back_numbers += 1
        res -= step_list[i]
print(target-res, back_numbers)