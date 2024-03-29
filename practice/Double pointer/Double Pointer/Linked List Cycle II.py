'''
142. Linked List Cycle II
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
'''
'''
There are two main steps we need to conisder in this issue

1.wheather there is a circle in the the list
2.if there is the circle how to finde the enter of the cycle
'''

'''
The question 1,
there are two pointer, faster slow
The faster evertime move two steps, if there is a cycle,they must meet
How to finde the enter of the cycle

'''
class ListNode:
    def __init__(self,val,next):
        self.val=val
        self.next=next
        
class Solution:
    def detecCycle(self,head:ListNode):
        #1.wheather there is a circle in the the list
        slower,faster=head,head
        while faster and faster.next:
              slower=slower.next
              faster=faster.next.next
              if slower==faster:
                 #2.if there is the circle how to finde the enter of the cycle
                    slower=head
                    while slower!=faster:
                        slower=slower.next
                        faster=faster.next
                    return slower
        return None
    
    def detecCyclewithSet(self,head:ListNode):
        vivisted=set()

        while head:
            if head in vivisted:
                return head
            vivisted.add(head)
            head=head.next

            return None