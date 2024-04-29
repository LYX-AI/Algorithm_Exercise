class TreeNode:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def preorderTraversal(self,root:TreeNode)->list[list]:
        res=[]

        def dfs(node):
            if node is None:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
    def inorderTraversal(self,root:TreeNode)->list[list]:
        res=[]

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
    def postorderTraversal(self,root:TreeNode)->list[list]:
        res=[]

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res       
    '''
    每次写递归，都按照这三要素来写，可以保证大家写出正确的递归算法！

确定递归函数的参数和返回值： 确定哪些参数是递归的过程中需要处理的，那么就在递归函数里加上这个参数， 并且还要明确每次递归的返回值是什么进而确定递归函数的返回类型。
 res.append(node.val)
 递归参数node的值除了这个不用再处理其他数据
确定终止条件： 写完了递归算法, 运行的时候，经常会遇到栈溢出的错误，就是没写终止条件或者终止条件写的不对，操作系统也是用一个栈的结构来保存每一层递归的信息，如果递归没有终止，操作系统的内存栈必然就会溢出。
 if node is None:
    return
确定单层递归的逻辑： 确定每一层递归需要处理的信息。在这里也就会重复调用自己来实现递归的过程。
    '''