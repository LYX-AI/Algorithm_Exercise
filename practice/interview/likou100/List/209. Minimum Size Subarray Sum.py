from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result=float('inf')
        sum=0
        i=0
        for j in range(len(nums)):
           sum+=nums[j]
           while sum>=target:
               result=min(result,j-i+1)
               sum-=nums[i]
               i+=1
        return result if result!=float('inf') else 0

if __name__=="__main__":
    solution=Solution()
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(solution.minSubArrayLen(target,nums))
