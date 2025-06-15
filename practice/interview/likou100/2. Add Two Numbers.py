# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    #以下是我第一次这么写的，这么写题目理解是有问题的，思路也不太对
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     current1=l1
    #     current2=l2
    #     temp_second=0
    #     while current1 and current2:
    #         temp_N=current1.val+current2.val
    #         total=temp_N % 10+temp_second
    #         current1.val = total % 10
    #         temp_second = total // 10
    #         mark=current1
    #         current1=current1.next
    #         current2=current2.next
    #     if current1:
    #         current1.val=current1.val+temp_second
    #     if current2:
    #         current2.val=current2.val+temp_second
    #         mark.next=current2
    #     return l1
    class Solution:
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy=ListNode(0)
            current=dummy
            carry=0

            while l1 or l2 or carry:
                val1=l1.val if l1 else 0
                val2=l2.val if l2 else 0
                total=val1+val2+carry

                carry=total//10
                current.next=ListNode(total%10)
                current=current.next

                if l1:l1=l1.next
                if l2:l2=l2.next

            return dummy.next
