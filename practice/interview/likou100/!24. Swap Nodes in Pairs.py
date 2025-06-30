# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy=ListNode(0,head)
        prv=dummy
        while prv.next and prv.next.next:
            slow=prv.next
            fast= slow.next

            prv.next=fast
            slow.next = fast.next
            fast.next=slow

            prv=slow#这一步最关键了写的时候没想出来
        return dummy.next


#下面是看了代码随想录的视频后写的
    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(next=head)
        cur=dummy
        #判断遍历终止条件，如果是偶数的话是cur.next==Null如何是奇数的话cur.next.next=Null
        while cur.next is not None or cur.next.next is not None:
            temp1=cur.next
            temp2=cur.next.next.next
            cur.next=temp1.next
            cur.next.next=temp1
            temp1.next=temp2
            cur = cur.next.next
        return dummy.next