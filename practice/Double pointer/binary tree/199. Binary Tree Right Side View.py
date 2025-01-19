'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
https://leetcode.cn/problems/binary-tree-right-side-view/description/
'''


import collections
from typing import Optional
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root:Optional[TreeNode]):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root == None:
            return []
        right_sight=[]
        queue=collections.deque([root])
        while queue:
            queue_length=len(queue)
            for i in range(queue_length):
                cur=queue.popleft()
                if i == queue_length-1:
                    right_sight.append(cur.val)
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
        return right_sight


