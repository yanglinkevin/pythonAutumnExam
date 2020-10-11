class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

n = int(input())
nums1 = list(map(int, input().split(' ')))
head1 = None
for i in range(n):
    if not head1:
        head1 = Node(nums1[i])
        cursor1 = head1
    else:
        cursor1.next = Node(nums1[i])
        cursor1 = cursor1.next
m = int(input())
nums2 = list(map(int, input().split(' ')))
head2 = None
for i in range(m):
    if not head2:
        head2 = Node(nums2[i])
        cursor2 = head2
    else:
        cursor2.next = Node(nums2[i])
        cursor2 = cursor2.next

cursor1 = head1
cursor2 = head2
res = []
while cursor1 and cursor2:
    if cursor1.val == cursor2.val:
        res.append(cursor1.val)
        cursor1 = cursor1.next
        cursor2 = cursor2.next
    elif cursor1.val>cursor2.val:
        cursor1 = cursor1.next
    else:
        cursor2 = cursor2.next
for i in range(len(res)):
    print(res[i], end=' ')


        

    