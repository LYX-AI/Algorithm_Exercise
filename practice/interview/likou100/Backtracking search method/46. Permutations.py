from typing import List


class Solution:
    def backtracking(self,nums: List[int],result: List[int],path: List[int],used: List[float]):
        n = len(nums)
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(n):
            if used[i] == True:
                continue
            used[i]=True
            path.append(nums[i])
            self.backtracking(nums,result,path,used)
            used[i]=False
            path.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        used=[False]*len(nums)
        self.backtracking(nums,result,[],used)
        return result

if __name__ == "__main__":
    solution=Solution()
    nums = [1, 2, 3]
    print(solution.permute(nums))



