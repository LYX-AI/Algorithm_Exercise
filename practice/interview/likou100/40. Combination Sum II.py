from typing import List


class Solution:
    def backtracking(self,candidates: List[int], target: int, sum:int, path:List[int], result:List[List[int]],used:List[int],Index:int):
        if sum>target: return
        if sum == target:
            result.append(path[:])
            return
        for i in range(Index,len(candidates)):
            if i > Index and candidates[i] == candidates[i-1] and used[i-1] == 0:
                continue
            sum += candidates[i]
            path.append(candidates[i])
            used[i]=1
            self.backtracking(candidates,target,sum,path,result,used,i+1)
            sum -= candidates[i]
            path.pop()
            used[i] = 0
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        used = [0]*len(candidates)
        self.backtracking(candidates,target,0,[],result,used,0)
        return result

if __name__=="__main__":
    solution = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(solution.combinationSum2(candidates,target))
