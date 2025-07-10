# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result=1
        if root.right or root.left:
            result+max(self.maxDepth(root.left),self.maxDepth(root.right))
        else:
            return 1
        return result
