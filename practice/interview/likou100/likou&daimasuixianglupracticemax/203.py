from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode],val:int)->Optional[ListNode]:
        if head == None:
            return head
        dummy_head=ListNode(next=head)
        cur=dummy_head
        while cur.next:
            if cur.next.val==val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy_head.next

if __name__=='__main__':
    s=Solution()
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next=ListNode(6)
    head.next.next.next=ListNode(3)
    head.next.next.next.next=ListNode(4)
    head.next.next.next.next.next=ListNode(5)
    head.next.next.next.next.next.next=ListNode(6)
    val =6
    head=s.removeElements(head,val)
    while head:
        print(head.val)
        head=head.next