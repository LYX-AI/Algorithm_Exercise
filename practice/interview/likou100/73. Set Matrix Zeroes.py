class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        target_line = [0]*n
        mark_colum = []
        for i in range(m):
            for j in range(n) :
                if matrix[i][j] == 0:
                    mark_colum.append(j)
            if 0 in matrix[i]:
                matrix[i] = target_line
        for row in range(m):
            for col in mark_colum:
                matrix[row][col] = 0
        return matrix
if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print(solution.setZeroes(matrix))
    print(solution.setZeroes(matrix2))


