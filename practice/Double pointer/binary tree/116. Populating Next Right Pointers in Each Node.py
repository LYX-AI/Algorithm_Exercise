# Definition for a Node.
import collections
from typing import Optional
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return []
        queue=collections.deque([root])
        while queue:
            level_len=len(queue)
            private=None
            for _ in range(level_len):
                node=queue.popleft()
                if private:
                    private.next=node
                private=node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root