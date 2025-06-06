class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # result = []
        # count = 0
        # m = len(matrix)
        # n = len(matrix[0])
        # while count<n:
        #     item = []
        #     for i in range(m):
        #         item.append(matrix[i][count])
        #     item.reverse()
        #     result.append(item)
        #     count +=1
        # return result
        #举证的行列互换方法，记住就好
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for row in matrix:
            row.reverse()

if __name__=='__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution = Solution()
    print(solution.rotate(matrix))
    print(solution.rotate(matrix2))