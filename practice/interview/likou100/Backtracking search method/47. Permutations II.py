from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        used=[False]*n
        result=[]
        nums.sort()
        self.backtracking(nums,used,result,[])
        return result
    def backtracking(self,nums: List[int],used: List[float],result: List[List[int]],path:List[int]):
        if len(path)==len(nums):
            result.append(path[:])
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]and used[i-1]==False:
                continue
            if used[i]==True:
                continue
            used[i]=True
            path.append(nums[i])
            self.backtracking(nums,used,result,path)
            used[i]=False
            path.pop()

if __name__ == "__main__":
    nums=[1,1,2]
    solution=Solution()
    print(solution.permuteUnique(nums))