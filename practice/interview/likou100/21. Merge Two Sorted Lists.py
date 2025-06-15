# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        if list1.val<list2.val:
            list3=list1
            list1=list1.next
        else:
            list3=list2
            list2=list2.next
        current3=list3
        while list1 and list2:
                if list1.val<list2.val:
                    current3.next=list1
                    list1=list1.next
                else:
                    current3.next=list2
                    list2=list2.next
                current3=current3.next
        if list1:
                current3.next=list1
        if list2:
                current3.next=list2
        return list3



