n = int(input())
res = []
cnt = 0
for i in range(1,10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i!=j!=k:
                if i*100+j*10+k==n-i*100-k*10-k:
                    cnt += 1
                    res.append([i*100+j*10+k, i*100+k*10+k])

print(cnt)
for i in res:            
    print(i[0], i[1])