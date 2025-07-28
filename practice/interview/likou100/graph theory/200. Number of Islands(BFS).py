import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        Island=0
        row=len(grid)
        clow=len(grid[0])
        driection=[(1,0),(-1,0),(0,-1),(0,1)]

        def bfs(r,c):
            queue=collections.deque()
            queue.append((r,c))
            grid[r][c]='0'
            while queue:
               x,y= queue.popleft()
               for dx,dy in driection:
                   nx,ny=x+dx,y+dy
                   if 0<=nx<row and 0<=ny<clow and grid[nx][ny]=='1':
                       queue.append((nx,ny))
                       grid[nx][ny]='0'

        for i in range(row):
            for j in range(clow):
                if grid[i][j]=='1':
                    bfs(i,j)
                    Island+=1
        return Island

