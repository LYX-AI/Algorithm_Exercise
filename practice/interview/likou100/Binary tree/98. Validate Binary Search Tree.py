# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.result=[]
        def inorder(root: Optional[TreeNode])->list[int]:
            if not root:
                return
            inorder(root.left)
            self.result.append(root.val)
            inorder(root.right)
        inorder(root)

        for i in range(1,len(self.result)):
            if self.result[i]<=self.result[i-1]:
                return False
        return True


