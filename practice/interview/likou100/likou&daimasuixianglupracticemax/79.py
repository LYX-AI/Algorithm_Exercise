from typing import List


class Solution:
    def Backtrackin(self,i:int,j:int,StartIndex:int,board:List[List[str]],target:str):
        if StartIndex == len(target):
            return True
        if i<0 or j<0 or i>=len(board) or j>=len(board[0])or board[i][j]!=target[StartIndex]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        found=(self.Backtrackin(i+1, j, StartIndex+1, board, target) or
        self.Backtrackin(i-1, j, StartIndex+1, board, target) or
        self.Backtrackin(i, j+1, StartIndex+1, board, target) or
        self.Backtrackin(i, j-1, StartIndex+1, board, target))
        board[i][j]=temp
        return found



    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.Backtrackin(i,j,0,board,word):
                    return True
        return False