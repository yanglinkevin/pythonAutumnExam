def helper(x, y, info1, info2):
    xs = [1, -1, 0, 0]
    ys = [0, 0, 1, -1]
    for i in range(4):
        nx = x+xs[i]
        ny = y+ys[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if not visited[nx][ny]:
            if mapped[nx][ny]=='1':
                visited[nx][ny] = True
                info2 += 1
                info1, info2 = helper(nx, ny, info1, info2)
            else:
                if (nx*m+ny) not in info1:
                    info1.append(nx*m+ny)
    return info1, info2
