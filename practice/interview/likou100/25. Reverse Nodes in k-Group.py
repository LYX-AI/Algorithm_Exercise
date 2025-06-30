# Definition for singly-linked list.
from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self,head: Optional[ListNode])-> Tuple[Optional[ListNode],Optional[ListNode]]:
         if not head or not head.next:
             return head,head

         prv=None
         cur=head
         while cur:
            temp=cur.next
            cur.next=prv
            prv= cur
            cur=temp
         return prv , head


#主要思路是吧链表分为三个部分，前面翻转完的，当前的和之后要处理的三部分
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       dummy=ListNode(next=head)
       prev_tail=dummy
       while True:
           old_head=prev_tail.next
           count_node=prev_tail
           for i in range(k):
               count_node=count_node.next
               if not count_node:
                   return dummy.next
           next_group_head=count_node.next
           count_node.next=None
           new_head,new_tail=self.reverseList(old_head)

           prev_tail.next=new_head
           new_tail.next=next_group_head
           prev_tail=new_tail


