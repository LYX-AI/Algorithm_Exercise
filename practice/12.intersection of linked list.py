'''
topic:
具体描述：https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/
'''
'''
train of though:
linked list A and B
1.get the length of the two linked list;
2.set the A or B is the longest of the linked list(we need to make sure one linked list is the longest link of these two)
3.calulate the difference of the two linked lists,align at the tail of the tow linked list 
3.Traverse the linked list from the overlapping part of a linked list and compareed them to find the same val if same will return thsi Node
'''

# Definition for singly-linked list.
from typing import Counter


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        lenA,lenB=0,0
        # get the length of the linked list A & B
        current=headA
        while current:
            lenA+=1
            current=current.next
        current=headB
        while current:
            lenB+=1
            current=current.next
        #set the A or B is the longest of the linked list(we need to make sure one linked list is the longest link of these two)
        #here we select the linked listB as the longest linked list
        currentA , currentB=headA,headB
        if lenA>lenB:
            currentA,currentB=currentB,currentA
            lenB,lenA=lenA,lenB
        for _ in range(lenB-lenA):
            currentB=currentB.next
        while currentB:
            if currentB==currentA:
                return currentB
            else:
                currentA=currentA.next
                currentB=currentB.next
        return None

