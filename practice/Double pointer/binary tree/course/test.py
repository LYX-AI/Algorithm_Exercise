# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.value=val
#         self.left=left
#         self.right=right
#
# class test1:
#     def PreOrder(self,root:TreeNode)->list[TreeNode]:
#         result = []
#         def dsf(node):
#             if root is None:
#                 return []
#             result.append(root.value)
#             dsf(root.left)
#             dsf(root.right)
#         dsf(root)
#         return result
#
#     def CpmareTree(self,root1:TreeNode,root2:TreeNode):
#         result1=test1.PreOrder(root1)
#         result2=test1.PreOrder(root2)
#         if result1 in result2 or result2 in result1:
#             return True
#         else:
#             return False
#     def EqualTree(self,root1:TreeNode,root2:TreeNode):
#
# if __name__=="main":
#     TreeNode1 = dsf(root1)
#     TreeNode2 = dsf(root2)
#     return EqualTree(TreeNode1,TreeNode2)
#
