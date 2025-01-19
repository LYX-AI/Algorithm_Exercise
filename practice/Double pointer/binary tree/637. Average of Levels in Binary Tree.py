import  collections
from typing import Optional

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root:TreeNode)->list[float]:
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        if root==[]:
            return []

        queue=collections.deque([root])
        average=[]
        while queue:
            size=len(queue)
            level_sum=0
            for _ in range(size):
                cur=queue.popleft()
                level_sum+=cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            average.append(level_sum/size)
        return average

