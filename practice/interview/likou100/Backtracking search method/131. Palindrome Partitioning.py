from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtracking(s,result,StartIndex=0,path=[])
        return result

    def backtracking(self,s:str,resutl:List[List[str]],StartIndex:int,path:List[str]):
        if StartIndex == len(s):
            resutl.append(path[:])
            return
        for i in range(StartIndex,len(s)):
            if self.is_palindrome(s,StartIndex,i):
                path.append(s[StartIndex:i+1])
                self.backtracking(s,resutl,i+1,path)
                path.pop()

    def is_palindrome(self,s:str,start:int,end:int):
        i = start
        j = end
        while i < j:
            if s[start] != s[end]:
                return False
            i +=1
            j -=1
        return True
if __name__ == "__main__":
    solution = Solution()
    s = "aab"
    print(solution.partition(s))