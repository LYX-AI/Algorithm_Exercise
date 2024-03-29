# Definition for singly-linked list.
from _typeshed import Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#The solution of double pointer
class Solution:
    def reverseList(self, head: Optional[ListNode]):
        pre=None
        Current=head
        while Current:
            temp=Current.next
            Current.next=pre
            pre=Current
            Current=temp
        return pre        
# The solution of recursion
    def reverseList(self, head: Optional[ListNode]):
        return self.reverse(head,None)
    def reverse(self,Current, pre):
        if Current==None:
            return pre
        temp=Current.next
        Current.next=pre
        return self.reverse(temp,Current)

