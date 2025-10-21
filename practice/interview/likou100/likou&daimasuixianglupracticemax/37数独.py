from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(i,j,k,board: List[List[str]]) -> bool:
            for col in range(len(board)):
                if board[i][col] == k:
                    return False

            for row in range(len(board)):
                if board[row][j] == k:
                    return False

            start_row = (i//3)*3
            start_col = (j//3)*3
            for row in range(start_row,start_row+3):
                for col in range(start_col,start_col+3):
                    if board[row][col] == k:
                       return False

            return True

        def backtrack(board: List[List[str]]):
            board_size = len(board)
            for i in range(board_size):
                for j in range(board_size):
                    if board[i][j] == ".":
                        for k in "123456789":
                            if isValid(i, j, k, board):
                                board[i][j] = k
                                result =backtrack(board)
                                if result == True :
                                    return True
                                board[i][j] = "."
                        return False
            return True
        backtrack(board)
# 此题代码随想录上的方法可以过判断，但我感觉理解起来有点难度暂时先跳过