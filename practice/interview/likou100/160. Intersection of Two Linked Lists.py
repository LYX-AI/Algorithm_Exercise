# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        currentA=headA
        currentB=headB
        while currentA != currentB:
            if currentA is not None:
                currentA=currentA.next
            else:
                currentA=headB
            if currentB is not None:
                currentB=currentB.next
            else:
                currentB=headA
        return currentA

