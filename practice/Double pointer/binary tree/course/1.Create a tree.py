class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None



    def insert(self,value):
        if value<self.value:
            if self.left:
                self.left.inert(value)
            else:
                self.left=Node(value)
        if value>self.value:
            if self.right:
                self.right.inert(value)
            else:
                self.right=Node(value)
#满二叉树
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
#二叉排序树
root=Node(5)
root.insert(3)
root.insert(7)
root.insert(2)
root.insert(4)
root.insert(6)
root.insert(8)