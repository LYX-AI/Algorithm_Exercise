from typing import List


class Solution(object):
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        chessboard = ['.' * n for _ in range(n)]
        self.backtracking(n,0,chessboard,result)
        return [[''.join(row) for row in solution] for solution in result]

    def backtracking(self,n:int,row:int,chessboard:List[str],result:List[List[str]]):
        if row==n:
            result.append(chessboard[:])
            return
        for col in range(n):
            if self.isValid(row,col,chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]
                self.backtracking(n,row+1,chessboard,result)
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:]

    def isValid(self, row:int, clow:int,chessboard:List[str]) -> bool:
        for i in range(row):
            if chessboard[i][clow]=='Q':
                return False

        i,j= row-1,clow-1
        while i>=0 and j>=0:
            if chessboard[i][j]=='Q':
                return False
            i-=1
            j-=1

        i=row-1
        j=clow+1
        while i>=0 and j<len(chessboard):
            if chessboard[i][j]=='Q':
                return False
            i-=1
            j+=1
        return True



