from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        self.backtracking(n,0,k,1,[],result)
        return result

    def backtracking(self,TargetSum,CurrentSum,k,StartIndex,path,result):
        if CurrentSum > TargetSum :#减枝
            return
        if len(path)==k:
            if CurrentSum == TargetSum:
                result.append(path[:])
        for i in range(StartIndex,9-(k-len(path))+2):#减枝
                CurrentSum+=i
                path.append(i)
                self.backtracking(TargetSum,CurrentSum,k,i+1,path,result)
                CurrentSum-=i
                path.pop()

if __name__=="__main__":
    solution=Solution()
    k = 3
    n = 7
    print(solution.combinationSum3(k,n))