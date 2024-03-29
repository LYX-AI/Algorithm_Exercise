'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''
from types import prepare_class
from typing import Counter


class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val=val
        self.next=next
class Solution:
    def Reverse_Linked_List(self,head):
        if head==None or head.next==None:
            return head
        slow=head
        fast=slow.next
        head.next=None
        while fast:
            temp=fast.next
            fast.next=slow
            slow=fast
            fast=temp
        return slow

    def reverseList(self,head):
        return self.reverse(head,None)

    def reverse(self,cur,pre):
        if cur is None:
            return pre
        temp=cur.next
        cur.next=pre
        return self.reverse(temp,cur)
head=ListNode(3,ListNode(4,ListNode(5)))
a=Solution()
print(a.reverseList(head))