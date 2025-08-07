import collections
from typing import List


class Solution:
    # 构造图
    def build_grap(self,numCourses: int, prerequisites: List[List[int]]):
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            in_degree[course] += 1
        return graph, in_degree

    #DSF
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        grap,in_degree= self.build_grap(numCourses,prerequisites)
        queue=collections.deque([i for i in range(numCourses) if in_degree[i]==0])
        token=0

        while queue:
            u=queue.popleft()
            token+=1
            for v in grap[u]:
                in_degree[v]-=1
                if in_degree[v]==0:
                    queue.append(v)
        return token == numCourses

