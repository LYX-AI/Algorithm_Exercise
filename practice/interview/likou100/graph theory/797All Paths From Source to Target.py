from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target=len(graph)-1
        result=[]
        path=[0]

        def dfs(x):
            if x==target:
                result.append(path.copy())
            for nei in graph[x]:
                path.append(nei)
                dfs(nei)
                path.pop()
        dfs(0)
        return result
#         result = []
#         def dsf(graph: List[List[int]],x,n,path:List[int],result:List[List[int]]):
#             if x==n:
#                 result.append(path.copy())
#                 return
#             for i in range(1,n+1):
#                 if graph[x][i]==1:
#                     path.append(i)
#                     dsf(graph,i,n,path,result)
#                     path.pop()
#
#         dsf(graph,1,n,[1],result)
#         if not result:
#             return -1
#         else:
#             return result
#
#
#
#
# def main():
# #构造图，输入节点数和边数 n是节点数 m是边数
#    n,m=map(int,input().split())
#    grap=[[0]*(n+1) for _ in range(n+1)]
#    for _ in range(m):
#     s,t=map(int,input().split())
#     grap[s][t]=1
#     return grap
#
#





