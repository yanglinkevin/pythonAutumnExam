def findPivot(nums, left, right):
    mid = left + (right-left)//2
    if nums[left]>nums[right]:
        nums[left], nums[right] = nums[right], nums[left]
    if nums[left]>nums[mid]:
        nums[left], nums[mid] = nums[mid], nums[left]
    if nums[mid]>nums[right]:
        nums[right], nums[mid] = nums[mid], nums[right]
    nums[mid], nums[right-1] = nums[right-1], nums[mid]
    return nums[right-1]

def quickSort(nums):
    stack = [[0, len(nums)-1]]
    while stack:
        index = stack.pop()
        root_left, root_right = index[0], index[1]
        if root_right-root_left>=1:
            left = root_left
            flag = root_right-1
            pivot = findPivot(nums, root_left, root_right)
            right = root_right-2
            while left<right:
                while left<right and nums[left]<pivot:
                    left += 1
                while left<right and nums[right]>pivot:
                    right -= 1
                if left<right:
                    nums[left], nums[right] = nums[right], nums[left]
                else:
                    break
            nums[left], nums[flag] = nums[flag], nums[left]
            stack.append([root_left,left-1])
            stack.append([left+1,root_right])
    return nums

nums = [5,3,0,10]
res = quickSort(nums)
print(res)

