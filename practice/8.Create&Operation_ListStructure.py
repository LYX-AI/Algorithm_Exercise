from _typeshed import Self


class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        pass

class MyLinkedList:

    def __init__(self):
        self.dummy_head=ListNode()
        self.size=0


    def get(self, index: int) -> int:
        if index<0 or index>self.size:
            return -1
        
        Current=self.dummy_head.next
        for i in range(index):
            Current=Current.next
        
        return Current.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next=ListNode(val,self.dummy_head.next)
        self.size+=1

    def addAtTail(self, val: int) -> None:
        Current=self.dummy_head
        while Current.next:
            Current=Current.next
        Current.next=ListNode(val)
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.size:
            return
        Current=self.dummy_head
        for i in range(index):
            Current=Current.next
        Current.next=ListNode(val,Current.next)
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>self.size:
            return
        Current=self.dummy_head
        for i in range(index):
            Current=Current.next
        Current.next=Current.next.next
        self.size-=1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
