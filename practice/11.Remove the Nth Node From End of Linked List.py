'''
topic:
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：

输入：head = [1], n = 1
输出：[]

示例 3：

输入：head = [1,2], n = 1
输出：[1]

'''
'''
train of though
1.How to find the Nth Node from the end of linked 
   need to pointer from the dammy head "faster"&"lower"
   let the faster pointer move the next step and make sure the distance between the faster header and the lower pointer is n+1
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(head:ListNode, n: int):
        dammy_head=ListNode(next=head)
        faster=dammy_head
        lower=dammy_head
        n+=1
        while n!=0 and faster:
            faster=faster.next
            n-=1
        while faster:
            faster=faster.next
            lower=lower.next
        lower.next=lower.next.next
        return dammy_head.next

head = ListNode(2, ListNode(4, ListNode(5,ListNode(6))))
head2=ListNode(1,None)
n=1
current=Solution.removeNthFromEnd(head2,n)
while current:
    print(current.val,end=" ")
    current=current.next
        