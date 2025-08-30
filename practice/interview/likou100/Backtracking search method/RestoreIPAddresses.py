from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result=[]
        self.backtracking(s,0,0,"",result)
        return result

    def backtracking(self,s:str,StarIndex,PointSum:int,current,result:List[str]):
        if PointSum == 3:
            if self.is_valid(s,StarIndex,len(s)-1):
                current += s[StarIndex:]
                result.append(current)
            return
        for i in range(StarIndex,len(s)):
            if self.is_valid(s,StarIndex,i):
                sub = s[StarIndex:i+1]
                self.backtracking(s,i+1,PointSum+1,current+sub+".",result)
            else:
                break

    def is_valid(self,s:str,start:int ,end:int):
        if start > end:
            return False
        if s[start] == '0' and start != end:
            return False
        num = 0
        for i in range(start,end+1):
            if not s[i].isdigit():
                return False
            num = num*10+int(s[i])
            if num > 255:
                return False
        return True



if __name__=="__main__":
    solution=Solution()
    s = "25525511135"
    print(solution.restoreIpAddresses(s))