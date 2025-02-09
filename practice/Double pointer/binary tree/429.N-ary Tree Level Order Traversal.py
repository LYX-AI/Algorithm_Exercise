"""
# Definition for a Node.

"""
import collections
from typing import Optional
import collections
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[list['Node']] = None):
        self.val = val
        self.children = children
class Solution:
    def levelOrder(self, root:Node) -> list[list[int]]:
        if root is None:
            return []
        queue=collections.deque([root])
        result=[]
        while queue:
            level_size=len(queue)
            level=[]
            for _ in range(level_size):
                cur=queue.popleft()
                level.append(cur.val)

                for child in cur.children:
                    queue.append(child)
            result.append(level)
        return result
