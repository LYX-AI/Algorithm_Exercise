from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        self.backtracking(n,k,[],result,1)
        return result
    def backtracking(self,n:int,k:int,path,result,StartIndex:int):
        if len(path)==k:
            result.append(path[:])
            return
        for i in range(StartIndex,n+1):
            path.append(i)
            self.backtracking(n,k,path,result,i+1)
            path.pop()

if __name__=="__main__":
    solution=Solution()
    n = 4
    k = 2
    print(solution.combine(n,k))