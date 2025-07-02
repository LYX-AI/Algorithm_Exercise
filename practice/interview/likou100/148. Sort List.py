#这道题我想到的方法是冒泡排序加链表节点的交换
from typing import Optional

'''
正确思路
原始链表: 4 → 2 → 1 → 3

1. 找到中点，分割链表:
   左半部分: 4 → 2
   右半部分: 1 → 3

2. 递归排序左右两部分:
   左半部分排序后: 2 → 4
   右半部分排序后: 1 → 3

3. 合并两个有序链表:
   合并过程:
   比较 2 和 1 → 选 1
   比较 2 和 3 → 选 2
   比较 4 和 3 → 选 3
   最后剩下 4
   结果: 1 → 2 → 3 → 4
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid=self.FindMind(head)
        right_head=mid.next
        mid.next=None
        left=self.sortList(head)
        right=self.sortList(right_head)
        return self.MergeList(left,right)

    def FindMind(self,head:Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

    def MergeList(self,l1:ListNode,l2:ListNode)->ListNode:
        dummy=ListNode(None)
        cur=dummy

        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        cur.next=l1 if l1 else l2
        return dummy.next
