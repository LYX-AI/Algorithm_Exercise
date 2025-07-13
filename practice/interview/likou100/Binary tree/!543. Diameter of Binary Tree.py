# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_result=0
        def dsf(node: Optional[TreeNode])->int:
            if not node:
                return 0
            left=dsf(node.left)
            right=dsf(node.right)
            self.max_result=max(self.max_result,left+right)
            return max(left,right)+1

        dsf(root)
        return self.max_result
