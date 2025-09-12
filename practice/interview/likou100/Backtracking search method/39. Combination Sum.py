from typing import List


class Solution:
    #First
    # def backtracking(self,candidates: List[int], target: int,total:int,StartIndex:int,result:List[List[int]],path:List[int]):
    #     if total >target:
    #         return
    #     if total == target:
    #         result.append(path[:])
    #         return
    #     for i in range(StartIndex,len(candidates)):
    #         total+=candidates[i]
    #         path.append(candidates[i])
    #         self.backtracking(candidates,target,total,i,result,path)
    #         total-=candidates[i]
    #         path.pop()
    #
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     result=[]
    #     self.backtracking(candidates,target,0,0,result,[])
    #     return result
    def backtracking(self,candidates: List[int],result:List[List[int]],path:List[int],StartIndex:int,sum:int,target:int):
        if sum>target:
            return
        if sum == target:
            result.append(path[:])
            return
        for i in range(StartIndex,len(candidates)):
            sum+=candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates,result,path,i,sum,target)
            sum-=candidates[i]
            path.pop()
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        self.backtracking(candidates,result,[],0,0,target)
        return result


if __name__=="__main__":
    solution=Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(solution.combinationSum(candidates,target))