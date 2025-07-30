import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #先找到所有的烂橘子
        queue=collections.deque()
        freshCount=0
        row=len(grid)
        clow=len(grid[0])
        directions=[(1,0),(-1,0),(0,-1),(0,1)]
        minute=0
        for i in range(row):
            for j in range(clow):
                if grid[i][j]==2:
                    queue.append((i,j,minute))
                elif grid[i][j]==1:
                    freshCount+=1
        if freshCount==0:
            return 0
        while queue:
            x, y, t = queue.popleft()
            minute=max(minute,t)
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<row and 0<=ny<clow and grid[nx][ny]==1:
                    queue.append((nx,ny,t+1))
                    grid[nx][ny]=2
                    freshCount-=1
        if freshCount==0:
            return minute
        else:
            return -1


