# Definition for a binary tree node.
import collections
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #逆向先序遍历
        self.prev=None
        def dfs (Node:Optional[TreeNode]):
            if not Node:
                return
            dfs(Node.right)
            dfs(Node.left)
            Node.right=self.prev
            Node.left=None
            self.prev=Node
        dfs(root)



