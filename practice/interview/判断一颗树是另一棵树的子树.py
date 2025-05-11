class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def is_subTree(root:TreeNode,subTree:TreeNode):
    if not root:
        return False
    if is_same(root,subTree):
        return True
    return is_subTree(root.right,subTree) or is_subTree(root.left,subTree)

def is_same(root1:TreeNode,root2:TreeNode):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    return  is_same(root1.left,root2.left) and is_same(root1.right,root2.right)
