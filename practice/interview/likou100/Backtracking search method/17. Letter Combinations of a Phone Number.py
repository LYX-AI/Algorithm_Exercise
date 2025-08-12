from typing import List


class Solution:
    def __init__(self):
        self.LetterMap=[
            "", #0
            "", #1
            "abc", #2
            "def", #3
            "ghi", #4
            "jkl", #5
            "mno", #6
            "pqrs", #7
            "tuv",  #8
            "wxyz"  #9

        ]
        self.result=[]
        self.path=""
    def backtracking(self,digits:str,index:int):
        if index ==len(digits):
            self.result.append(self.path)
            return
        digit=int(digits[index])
        letter=self.LetterMap[digit]
        for i in range(len(letter)):
            self.path+=letter[i]
            self.backtracking(digits,index+1)
            self.path=self.path[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        self.backtracking(digits,0)
        return self.result


if __name__=="__main__":
    solution=Solution()
    digits = "23"
    print(solution.letterCombinations(digits))