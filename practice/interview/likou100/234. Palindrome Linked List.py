# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_num=[]
        current = head
        while current!=None:
            list_num.append(current.val)
            current=current.next
        i = 0
        j = len(list_num)-1
        while i<=j:
            if list_num[i] == list_num[j]:
                i+=1
                j-=1
            else:
                return False
        return True
