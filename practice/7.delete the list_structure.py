'''
topic:
删除链表中等于给定值 val 的所有节点。

示例 1： 输入：head = [1,2,6,3,4,5,6], val = 6 输出：[1,2,3,4,5]

示例 2： 输入：head = [], val = 1 输出：[]

示例 3： 输入：head = [7,7,7,7], val = 7 输出：[]
'''

'''
There are two type of list_structure:
    1.with the dummy_head
    2.without the dummy_head
'''
#first we need to create a data structure:list_structure
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val 
        self.next=next
        pass


class Solution:
    def removeElements(head: ListNode, val: int):
        dammy_head=ListNode(next=head)
        current=dammy_head
        while current.next:
            if current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next
        return dammy_head.next
#自己写的辣鸡方法
    def removeElements2(head: ListNode,val:int):
        head=head(val=head.val,next=head.val)
        current=head
        if head is None:
             return None
        if head.next is None and head.val==val:
             return None
        if head.next is None and head.val!=val:
             return head
        else:
            while current.next:
                if head.val==val:
                    head=head.next
                    current=head
                if current.next.val==val:
                    current.next=current.next.next
                else:
                     current=current.next
            if current.val==val:
                return None
            else:
                return head

#GTP给的牛逼的方法
def removeElements3(head: ListNode,val:int):
      # 处理头节点为空的情况
        while head and head.val == val:
            head = head.next
        
        current = head
        while current:
            if current.next and current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head

   

head = ListNode(7, ListNode(2, ListNode(7, ListNode(7, ListNode(7, ListNode(7, ListNode(7)))))))
val = 7
head2=ListNode(6,None)
head3=None
a=Solution.removeElements2(head=head,val=val)
current=a
while current:
    print(current.val, end=' ')
    current=current.next

'''
这里为什么不带dammy_header的的方法while循环是current而不是current.next
举个例子如果head就是目标值
比如 [1] targer 1
这种再执行完
while head and head.val == val:
    head = head.next
    这里的操作后head就以及是None了再进行current=head current.next 不存在这个current.next这个值会报错因为 None没有next这个元素

但是带dammy的就不一样上述这种情况的时候current指向的是dammy dammy是又next这个元素的所以是可以pass的
同理上面带dammy也不能是while current， 应为如果这样current.next是不存在的也不会存在current.next.val这个值所以下面的if语句会报错
        

'''