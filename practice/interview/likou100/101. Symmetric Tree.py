# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def left_Traver(self,root:Optional[TreeNode]):
        temp=[]
        if not root:
            return [None]
        temp.append(root.val)
        temp+=self.left_Traver(root.left)
        temp+=self.left_Traver(root.right)
        return temp
    def right_Traver(self,root:Optional[TreeNode]):
        temp=[]
        if not root:
            return [None]
        temp.append(root.val)
        temp += self.right_Traver(root.right)
        temp+=self.right_Traver(root.left)
        return temp

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if self.left_Traver(root)==self.right_Traver(root):
            return True
        return False
