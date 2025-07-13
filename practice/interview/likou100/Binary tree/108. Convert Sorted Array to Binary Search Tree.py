# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid_root=len(nums)//2
        root=TreeNode(nums[mid_root])
        root.left=self.sortedArrayToBST(nums[:mid_root])
        root.right=self.sortedArrayToBST(nums[mid_root+1:])
        return root


