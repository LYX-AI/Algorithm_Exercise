from collections import defaultdict
result=[]
path=[]
#使用递归的方法：
# '''
# 递归三步法
# 1. 确定 递归函数
# 2. 确定终止条件
# 3. 确定回退函数
# '''
def dsf(graph,x,n):
    if x==n: #2.判断终止条件
        result.append(path.copy())
        return
    for i in graph[x]: #找到当前节点指向的下一个节点
        path.append(i)
        dsf(graph,i,n)#进入下一层递归
        path.pop()#回退
def main():
    # create the adjacency list
    n,m=map(int,input().split())
    graph=defaultdict(list)
    for _ in range(m):
        s,t=map(int,input().split())
        graph[s].append(t)

    path.append(1)
    dsf(graph,1,n)

    if result is None:
        print(-1)
    for i in result:
        print(' '.join(map(str,i)))

if __name__=='__main__':
    main()
