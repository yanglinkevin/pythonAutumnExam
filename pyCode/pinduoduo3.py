
def test3():
    nums = []
    m, n = map(int, input().split(' '))
    for i in range(m):
        c, v = map(int, input().split(' '))
        nums.append([c, v])
    nums.sort()
    # m, n = 5, 5
    # nums = [[1, 1], [2, 2], [4, 4], [6, 6], [7, 7]]
    result = 0
    def helper(m, n, index, tmpc, tmpv):
        nonlocal result
        result = max(result, tmpv)
        for i in range(index, m):
            if nums[i][0]+tmpc<=n:
                helper(m, n, i+1, tmpc+nums[i][0], tmpv+nums[i][1])
            else:
                return
    helper(m, n, 0, 0, 0)
    print(result)

test3()