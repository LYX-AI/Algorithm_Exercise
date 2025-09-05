from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.backbracking(nums,0,result,[])
        return result
    def backbracking(self,nums: List[int],StartIndex:int,result: List[List[int]],path:List[int]):
        result.append(path[:])
        for i in range(StartIndex,len(nums)):
            path.append(nums[i])
            self.backbracking(nums,i+1,result,path)
            path.pop()
if __name__=="__main__":
    nums = [1, 2, 3]
    solution= Solution()
    print(solution.subsets(nums))