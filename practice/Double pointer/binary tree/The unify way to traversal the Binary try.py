'''
在迭代遍历的(iteration)这部分讲了，但是前序遍历，中序遍历代码没有统一，这一章就是要把代码统一起来操作
重要概念:
整个代码是有关键的两部分：
    1.对节点的遍历：访问节点
      其实就是我们要找到目标节点这个过程中所经过的节点
    2.目标节点：
        我们需要把目标节点的值放入到最后的结果中
统一代码的核心思想就是在遍历到目标节点的时候在目标把目标节点加入到中间栈里，并且在目标节点后面再加上一个null
这一步的作用就是打上一个坐标，null后面的值是我们需要放入到最终的结果中
其中node就是指向我们需要处理的节点
'''
class TreeNode:
    def __init__(self,value=0,left=None,right=None)->None:
        self.value=value
        self.left=left
        self.right=right


class Solution:
    def preorderTraversal(self,root:TreeNode)->list[int]:
        result=[]
        stack=[]
        if root:
            stack.append(root)
        while stack:
            node=stack.pop()
            #遍历操作
            if node != None: #顺序刚好和前序相反：右左中
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                stack.append(node)
                stack.append(None)
            else:
                stack.pop()
                result.append(node.value)
        return result

    def inorderTraversal(self,root:TreeNode)->list[int]:
        result=[]
        stack=[]
        if root:
            stack.append(root)
        while stack:
             node=stack.pop()
             if node.right:
                 stack.append(node.right)
             stack.append(node.value)
             stack.append(None)
             if node.left:
                 stack.append(node.left)
             else:
                 stack.pop()
                 result.append(node.value)
        return result

    def postorderTracersal(self,root:TreeNode)->[int]:
        result=[]
        stack=[]
        if root:
            stack.append(root)
        while stack:
            node=stack.pop()
            stack.append(node.value)
            stack.append(None)
            if node.right:
                stack.append(node.right)
            if node.right:
                stack.append(node.left)
            else:
                stack.pop()
                result.append(node.value)
        return result


