class Solution:

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        #这个解法最应该学到的地方就是bisect
        import bisect
        for row in matrix:
            index=bisect.bisect_left(row,target)
            if index<len(matrix[0]) and row[index] == target:
                return True
        return False

    def searchMatrix2(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix:
            return False
        #推荐的解法就是Z字查找
        n,m = len(matrix),len(matrix[0])
        row,col = 0,m-1
        while row<n and col>=0:
            if matrix[row][col]==target:
                return True
            if matrix[row][col]>target:
                col-=1
            else:
                row+=1
        return False
