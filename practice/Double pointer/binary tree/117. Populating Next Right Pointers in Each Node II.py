# Definition for a Node.
import collections
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        queue=collections.deque([root])
        private=None
        while queue:
            level_len=len(queue)
            for _ in range(level_len):
                Node=queue.popleft()
                if private:
                    private.next=Node
                private=Node
                if Node.left:
                    queue.append(Node.left)
                if Node.right:
                    queue.append(Node.right)
            return root



