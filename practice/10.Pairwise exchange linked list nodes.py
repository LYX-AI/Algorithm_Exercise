'''
topic:
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）


示例 1：

输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：

输入：head = []
输出：[]

示例 3：

输入：head = [1]
输出：[1]

'''
'''
train of though:
there are two parts are very important to think
 1.the condition in the while loop:
    current.next!=None and current.next.next!=None(the sequence of these two condions are very import)
      
2.How to change the two Node after the current Node 
    Need to know two parameters:temp and temp1
'''
# Definition for singly-linked list.
from typing import Counter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(head:ListNode):
        dammy_header=ListNode(next=head)
        current=dammy_header
        while(current.next !=None and current.next.next !=None):
            temp=current.next.next
            temp1=current.next.next.next
            current.next.next=temp1
            temp.next=current.next
            current.next=temp
            current=current.next.next
        return dammy_header.next


head = ListNode(2, ListNode(4, ListNode(5,ListNode(6))))
head2=ListNode(None)
head3=ListNode(1)
current=Solution.swapPairs(head2)
while current:
    print(current.val, end=' ')
    current=current.next