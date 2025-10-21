from typing import List


class Solution:
    def Jude(self,s:str)->bool:
        s=''.join(ch.lower() for ch in s if ch.isalnum())
        start=0
        end=len(s)-1
        while start<=end:
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                return False
        return True
    def backtracking(self,s:str,result:List[List[str]],path:List[str],StartIndex:int ) -> None:
        if StartIndex==len(s):
            result.append(path[:])
            return
        for i in range(StartIndex,len(s)):
            sub_str=s[StartIndex:i+1]
            if  self.Jude(sub_str):
                path.append(sub_str)
                self.backtracking(s,result,path,i+1)
                path.pop()

    def partition(self, s: str) -> List[List[str]]:
        result=[]
        self.backtracking(s,result,[],0)
        return result

if __name__=='__main__':
    s = "aab"
    solution=Solution()
    result = solution.partition(s)
    print(result)