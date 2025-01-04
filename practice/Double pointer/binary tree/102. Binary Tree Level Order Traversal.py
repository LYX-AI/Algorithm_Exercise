'''

title:
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

'''
#Change the git user to LYX-AI
import collections
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root:Optional[TreeNode]):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        queue = collections.deque([root])
        result=[]
        while queue:
            level = []
            for _ in range(len(queue)):
                cur=queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result

'''
tip:
queue = collections.deque([root])
初始化一个队列元素并且把里面塞入一个root元素

还有就是这里的
root:Optional[TreeNode]
Optional的意思就是这个root元素可以是TreeNode 类型也可以是None类型
'''