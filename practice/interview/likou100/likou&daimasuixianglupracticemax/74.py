from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened = [item for row in matrix for item in row]
        left, right = 0, len(flattened)-1
        middle=0
        while left<=right:
            middle = (left+right)//2
            if flattened[middle] == target:
                return True
            elif flattened[middle] > target:
                right = middle-1
            else:
                left = middle+1
        return False

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(s.searchMatrix(matrix, target))
