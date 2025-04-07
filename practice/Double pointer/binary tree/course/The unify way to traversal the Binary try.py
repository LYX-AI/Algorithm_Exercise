class Node:
    def __init__(self,value=0,right=None,left=None)->None:
        self.value=value
        self.right=right
        self.left=left

class solution:
    def preprdertraversal(self,root:Node)->list[int]:#中左右
        if root is None:
            return []
        result=[]
        stack=[]
        stack.append(root)
        while stack:
            cur=stack.pop()
            if cur is not None:#遍历节点
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
                stack.append(cur)
                stack.append(None)
            else:#对节点的处理
                 cur=stack.pop()
                 result.append(cur.value)
        return result
    def inordertraversal(self,root:Node)->list[int]:# 左中右
        if root is None:
            return []
        result=[]
        stack=[]
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur is not None:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                stack.append(None)
                if cur.left:
                    stack.append(cur.left)
            else:
                cur=stack.pop()
                result.append(cur.value)
        return result

    def postordertraversal(self,root:Node)->list[int]:# 左右中
        if root is None:
            return []
        result=[]
        stack=[]
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur is not None:
                stack.append(cur)
                stack.append(None)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
            else:
                cur=stack.pop()
                result.append(cur.value)
        return result


TestTree=Node(value=1,right=Node(value=3,right=None,left=None),left=Node(value=2,right=None,left=None))
testway=solution()
print(testway.preprdertraversal(TestTree))
print(testway.inordertraversal(TestTree))
print(testway.postordertraversal(TestTree))