from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        row=len(grid)
        cols=len(grid[0])
        Island=0

        def dsf(i,j):
            if i<0 or j>cols or j<0 or i>row or grid[i][j]!="1" :
                return
            grid[i][j]="0"
            dsf(i+1,j)
            dsf(i,j+1)
            dsf(i-1,j)
            dsf(i,j-1)

        for r in range(row):
           for c in range(cols):
               if grid[r][c]=="1":
                   Island+=1
                   dsf(r,c)

        return Island