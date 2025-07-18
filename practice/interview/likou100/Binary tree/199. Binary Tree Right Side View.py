# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        queue=collections.deque([root])
        result=[]
        while queue:
            level=[]
            for _ in range(len(queue)):
                cur=queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                level.append(cur.val)
            result.append(level[-1])
        return result

