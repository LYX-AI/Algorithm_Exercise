# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.dfs(root,targetSum)+self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum)

    def dfs(self,root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        count = 1 if root.val == targetSum else 0
        count += self.dfs(root.left, targetSum - root.val)
        count += self.dfs(root.right, targetSum - root.val)
        return count
