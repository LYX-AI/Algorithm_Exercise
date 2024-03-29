'''
topic::
Given two (singly) linked lists, determine if the two lists intersect. Return the inter­ secting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
'''
'''
for example:
    Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
Example 2:

Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
Example 3:

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
'''
'''
The most import thing we should know is that the secting node is not mean that the value of them is same , 
it's shoule be that the node is same (means the node.value and the node.next both them are same)
'''
class ListNode:
    def __init__(self,val,next):
        self.val=val
        self.next=next
        
class Soultion:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        #Count the length of the ListA and the listB
        CurrentA,CurrentB=headA,headB
        lenA,lenB=0,0
        while CurrentA:
            lenA+=1
            CurrentA=CurrentA.next
        while CurrentB:
            lenB+=1
            CurrentB=CurrentB.next
        # Make the ListNodeA is the longer ListNode
        if lenA<lenB:
            CurrentA,CurrentB=headB,headA
            lenA,lenB=lenB,lenA
        #Move the currentA to the next of the tail of the ListNodeB
        for _ in range(lenA-lenB):
            CurrentA=CurrentA.next
        while CurrentA:
            if CurrentA==CurrentB:
                return CurrentA
            else:
                CurrentA=CurrentA.next
                CurrentB=CurrentB.next
        return None
 