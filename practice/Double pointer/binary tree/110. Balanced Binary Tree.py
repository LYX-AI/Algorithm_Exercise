# Definition for a binary tree node.
from typing import  Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.get_height(root)==-1:
            return False
        else:
            return True

    def get_height(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_height=self.get_height(root.left)
        if left_height == -1:
            return -1
        right_height=self.get_height(root.right)
        if right_height==-1:
            return -1
        if abs(right_height - left_height) > 1:
            return -1
        else:
            return 1 + max(right_height, left_height)