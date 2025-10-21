from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        # 计算两个链表的长度
        curA, curB = headA, headB
        lenA = lenB = 0
        
        while curA:
            lenA += 1
            curA = curA.next
        
        while curB:
            lenB += 1
            curB = curB.next
        
        # 重置指针
        curA, curB = headA, headB
        
        # 让长链表先走，使两个指针到尾部的距离相等
        if lenA > lenB:
            lenA, lenB = lenB, lenA
            curA, curB = curB, curA
        
        diff = lenB - lenA
        while diff > 0 and curB:  # 添加 curB 的空值检查
            curB = curB.next
            diff -= 1
        
        # 同时移动两个指针，直到找到相交点
        while curA and curB:  # 添加两个指针的空值检查
            if curA == curB:
                return curA
            curA = curA.next
            curB = curB.next
        
        return None


if __name__ == '__main__':
    # 测试用例
    s = Solution()
    
    # 创建相交链表
    # listA: 4->1->8->4->5
    # listB: 5->6->1->8->4->5
    # 相交点在值为8的节点
    
    intersect = ListNode(8)
    intersect.next = ListNode(4)
    intersect.next.next = ListNode(5)
    
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = intersect
    
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = intersect
    
    result = s.getIntersectionNode(headA, headB)
    if result:
        print(f"相交节点的值: {result.val}")
    else:
        print("没有相交节点")