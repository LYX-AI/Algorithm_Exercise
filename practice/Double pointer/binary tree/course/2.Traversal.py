
class Treenode:
    def __init__(self,val=1,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def preorderTraversal(self,root:Treenode)->list[Treenode]:
        res=[]

        def dfspre(node):
            if node is None:
                return
            res.append(node.val)
            dfspre(node.left)
            dfspre(node.right)
        dfspre(root)
        return res
    def midorderTraversal(self,root:Treenode)->list[Treenode]:
        res=[]
        def dfsmid(node):
            if node is None:
                return
            dfsmid(node.left)
            res.append(node.val)
            dfsmid(node.right)
        dfsmid(root)
        return res
    def postorderTraversal(self,root:Treenode)->list[Treenode]:
        res=[]
        def dfsmid(node):
            if node is None:
                return
            dfsmid(node.left)
            dfsmid(node.right)
            res.append(node.val)
        dfsmid(root)
        return res


#构造二叉树
root1=Treenode(val=1)
root1.left=Treenode(val=2)
root1.right=Treenode(val=3)
root1.left.left=Treenode(val=4)
root1.left.right=Treenode(val=5)
root1.right.right=Treenode(val=6)

solution=Solution()
print(solution.preorderTraversal(root1))
print(solution.midorderTraversal(root1))
print(solution.postorderTraversal(root1))