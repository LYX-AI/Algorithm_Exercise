# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        rest_list=[]
        if not root:
            return []
        if root.left:
            rest_list+=self.inorderTraversal(root.left)
        rest_list.append(root.val)
        if root.right:
             rest_list+=self.inorderTraversal(root.right)
        return rest_list

