# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
#翻转再翻转是我想出来的方法太复杂了
    def rever_ListNode(self, head: Optional[ListNode])-> Optional[ListNode]:
        if not head:
            return None
        prv = None
        cur=head
        while cur:
            cur_next=cur.next
            cur.next=prv
            prv=cur
            cur=cur_next
        return prv


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=1
        head_rev=self.rever_ListNode(head)
        dummy=ListNode(None,next=head_rev)
        pre=dummy
        current=head_rev
        while count != n:
            pre=pre.next
            current=current.next
            count+=1
        if count ==n:
            pre.next=current.next
            current.next=None
        head_final=self.rever_ListNode(dummy.next)
        return head_final
#官方建议方法使用快慢指针的方法来做
class Solution:
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None,head)
        slow=dummy
        fast=dummy
        while fast:
            for _ in range(n+1):
                fast=fast.next
            while fast:
                fast=fast.next
                slow=slow.next
            slow.next=slow.next.next
        return dummy.next


