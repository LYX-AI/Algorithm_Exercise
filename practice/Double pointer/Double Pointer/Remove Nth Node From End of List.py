'''
descrpbe:
Given the head of a linked list, remove the nth node from the end of the list and return its head.

example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 
'''
class ListNode:
    def __init__(self,val=0,next=None) -> None:
        self.val=val
        self.next=next
class Solution:
    def removeNthFromEnd(self,head,n):
        dummy_head=ListNode(val=0,next=head)
        faster,slower=dummy_head,dummy_head
        for i in range(n):
            faster=faster.next
        while faster.next:
            faster=faster.next
            slower=slower.next
        if slower.next is not None:
            slower.next=slower.next.next
        return dummy_head.next
   
head=ListNode(val=1,next=None)
a=Solution()
print(a.removeNthFromEnd(head=head,n=1).val)

        