# Definition for singly-linked list.
from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head=ListNode(next=head)
        cur=dummy_head
        while cur.next and cur.next.next:
            temp1=cur.next
            temp2=cur.next.next.next
            cur.next=cur.next.next
            cur.next.next=temp1
            cur.next.next.next=temp2
            cur=cur.next.next
        return dummy_head.next
