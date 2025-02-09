#Definition for a binary tree node.
from typing import Optional
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        queue=collections.deque([root])
        result=[]
        while queue:
            level_len=len(queue)
            max_val=float('-inf')
            for _ in range(level_len):
                cur=queue.popleft()
                max_val=max(cur.val,max_val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(max_val)
        return result

