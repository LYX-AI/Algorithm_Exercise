from collections import defaultdict
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map=defaultdict(lambda : Node(0))
        cur=head
        while cur:
            map[cur]=Node(cur.val)
            cur=cur.next
        cur = head
        while cur:
            map[cur].next=map.get(cur.next)
            map[cur].random=map.get(cur.random)
            cur = cur.next

        return map.get(head)