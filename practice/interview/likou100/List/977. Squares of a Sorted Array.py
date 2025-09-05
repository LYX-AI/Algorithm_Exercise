from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [float('inf')]*len(nums)
        k = len(nums)-1
        i = 0
        j = len(nums)-1
        while(i<=j):
            if pow(nums[i],2)>pow(nums[j],2):
                result[k]=pow(nums[i],2)
                k=k-1
                i+=1
            else:
                result[k] = pow(nums[j], 2)
                k=k-1
                j-=1
        return result

if __name__=="__main__":
    nums = [-4, -1, 0, 3, 10]
    solution=Solution()
    print(solution.sortedSquares(nums))
