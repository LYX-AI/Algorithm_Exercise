# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dsf(self,root: Optional[TreeNode]):
        if not root:
            return []
        result=[]
        result.append(root.val)
        result+=self.dsf(root.left)
        result+=self.dsf(root.right)
        return result
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        temp=sorted(self.dsf(root))
        n=len(temp)
        for i in range(n):
            if k-1==i:
                return temp[i]









