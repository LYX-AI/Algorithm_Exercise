from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        resutl = []
        path = []
        self.backtracking(nums,resutl,path,0)
        return resutl

    def backtracking(self,nums: List[int],result: List[int],path: List[int],StartIndex: int):
        if len(path)>1:
            result.append(path[:])
        uset = set()
        for i in range(StartIndex,len(nums)):
            if path and nums[i]<path[-1] or nums[i] in uset:
                continue
            uset.add(nums[i])
            path.append(nums[i])
            self.backtracking(nums,result,path,i+1)
            path.pop()

if __name__ == "__main__":
    solution = Solution()
    nums = [4, 6, 7, 7]
    print(solution.findSubsequences(nums))