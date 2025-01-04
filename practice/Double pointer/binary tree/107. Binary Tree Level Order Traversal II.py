'''
107. Binary Tree Level Order Traversal II
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
这道题就是一个二叉树的广度遍历，就是在102的result基础上做了翻转
'''
import collections
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrderBottom(self, root:Optional[TreeNode]):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        #第一次写的时候忘记了可以root 是None的情况
        if root==None:
            return []
        #创建一个队列对象用来出来数据
        queue=collections.deque([root])
        #list result 用来存放结果
        result=[]
        while queue:
            level = []  # 每一层单独存放
            for _ in range(len(queue)):
                cur=queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        #当queue中没有元素存在说明整个树结构就遍历结束了对结果进行翻转
        return result[::-1]
'''
知识点
 1.result[::-1]
  不会改变result 本事而是会重新创建一个对象
 
 2.注意level这个对象定义的位置是在第一层循环下第二次循环外的
 
 3.和102题目比较，因为最终的结果是需要翻转的，在左右子树的插入顺序上是和102题正好相反的
 
'''

