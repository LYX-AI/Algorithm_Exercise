'''
前序遍历
'''
class TreeNode:
    def __init__(self,val=0,left=None,right=None)->None:
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def preorderTraversal(self,root:TreeNode)->list[int]:
        if not root:
            return []
        stack =[root]
        result=[]
        while stack:
          cur=stack.pop()
          result.append(cur.val)
          if cur.right:
              stack.append(cur.right)
          if cur.left:
              stack.append(cur.left)
        return result
    def midTraversal(self,root:TreeNode)->list[int]:
        if not root:
            return []
        stack =[root]
        result=[]
        cur=root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur=cur.left
            else:
                cur=stack.pop()
                result.append(cur.val)
                cur=cur.right
