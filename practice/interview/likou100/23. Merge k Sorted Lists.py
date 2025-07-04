# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        for head in lists:
            cur.next=head
            while cur.next:
                cur=cur.next
        return self.SortListNode(dummy.next)
    def SortListNode(self,head:ListNode)->ListNode:
        if not head or not head.next:
            return head
        Mid=self.FindListMid(head)
        left_head=head
        right_head=Mid.next
        Mid.next=None

        left=self.SortListNode(left_head)
        right=self.SortListNode(right_head)

        return self.MergeTowList(left,right)

    def FindListMid(self,head:ListNode)->ListNode:
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def MergeTowList(self,l1:ListNode,l2:ListNode)->ListNode:
         dummy=ListNode()
         tail=dummy

         while l1 and l2:
             if l1.val<l2.val:
                 tail.next=l1
                 l1=l1.next
             else:
                tail.next=l2
                l2=l2.next
             tail=tail.next
         tail.next=l1 if l1 else l2
         return dummy.next


