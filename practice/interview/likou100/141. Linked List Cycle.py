# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=[]
        current = head
        while current:
            temp.append(current)
            current =current.next
            if current in temp:
                return True
        return False
    #最优解法快慢指针
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        slow,faster= head,head
        while faster and faster.next:
            slow=slow.next
            faster=faster.next.next
            if slow == faster:
                return True
        return False
