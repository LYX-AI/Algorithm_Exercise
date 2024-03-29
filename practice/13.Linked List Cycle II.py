'''
topic:

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

example:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
'''

'''
train of though:
there are tow thing we need to make 
    1. make sure have the cycle in the linked list
    2. find the enter of the linked list

1. we can define two pointer one is fast anohter is slow pointer
    the faster pointer every step will move two nodes same like : fasters=faster.next.next
    the slower pointer every step will move one node  same like:  slower=slower.next

the reason is that we can see every step the faseter will move one step more than the slower pointer,so if there is a cycle in the linked list
the faster must can catch the slower

2.--x------------------
       |               |
       z               y
       |               |
        -point to meet--
we can have a  formal as this 
2(x+y)=x+y+n(y+z):
x+y=n(y+z)
x=n(y+z)-y
x=(n-1)(y+z)+y+z-y
x=(n-1)(y+z)+z
so we can get from formal that if the n=1  we can know that the x=z
so if there are two pointer one is index1 another is index2 the index1 start to move from the head of the linked list and index2 start
from the point to meet , every step they moved is just one node the they will meet at the enter of the cycle

so we can wirte code based on these two steps
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]):
        faster=head
        slower=head
        while faster and faster.next:
            slower=slower.next
            faster=faster.next.next
            #we can make sure there is a cycle in the linked list
            if slower==faster:
                slower=head
                while slower !=faster:
                    slower=slower.next
                    faster=faster.next
                return faster
        return None

# this solution we can lean a new function set()
    def detectCycle2(self, head: Optional[ListNode]):
        visited=set()

        while head:
            if head in visited:
                return head
            visited.add(head)
            head=head.next
        return None
        
