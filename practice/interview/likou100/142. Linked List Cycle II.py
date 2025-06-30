# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional

'''
快指针一次走两步，慢指针一次走一步。

假设第一次相遇时，慢指针一共走了：

ini
Copy
Edit
slow = a + b
快指针走的路是慢指针的两倍：

ini
Copy
Edit
fast = 2 * (a + b)
但快指针实际上多绕了几圈环：

ini
Copy
Edit
fast = a + b + n * c（n ≥ 1）
所以我们可以列出方程：

r
Copy
Edit
2(a + b) = a + b + n * c
解这个式子得到：

ini
Copy
Edit
a = n * c - b
即：

r
Copy
Edit
a + b = n * c
✅ 步骤二：从头走 vs 从相遇点走
让一个指针从 head 开始走，它走 a 步就到环入口；

让另一个指针从相遇点出发，再走 c - b 步，也正好回到环入口。

因为根据上面的推导：

ini
Copy
Edit
a = c - b（因为 a = n * c - b, n = 1 的情况下）
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast == slow:
                break
        else:
            return None
        p1=head
        p2=slow
        while p1 != p2:
            p1=p1.next
            p2=p2.next
        return p1
###############################################
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow == fast:
                break
        else:
            return None
            index1=slow
            index2=head
            while index1!=index2:
                index1=index1.next
                index2=index2.next
            return index1

