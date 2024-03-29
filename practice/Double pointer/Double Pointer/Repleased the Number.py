'''
topic:
Given a string s that contains lowercase letters and numeric characters, please write a function to keep the alphabetical characters unchanged while replacing each numeric character with the string "number".

For example, for the input string "a1b2c3", the function should transform it into "anumberbnumbercnumber".

For the input string "a5b", the function should transform it into "anumberb".

Input: A string s, containing only lowercase letters and numeric characters.

Output: Print a new string where each numeric character is replaced with "number".

Example Input: a1b2c3

Example Output: anumberbnumbercnumber

Data Constraints: 1 <= s.length < 10000.
'''
class Solution:
    def Replace_The_Number(s):
        ListS=list(s)
        count=0
        for i in ListS:
            if i>="0" and i<="9":
                count+=1
        ListS.extend([" "]*count*5)
        left,right=len(s)-1,len(ListS)-1
        while left>=0:
            if ListS[left]>='0' and ListS[left]<='9':
                ListS[right-5:right+1]="number"
                right-=6
            else:
                ListS[right]=ListS[left]
                right-=1
            left-=1

        return "".join(ListS)
    def Replace_The_Number2(s):
        ResultList=[]
        for i in s:
            if i>="0" and i<="9":
                ResultList.append("number")
            else:
                ResultList.append(i)
        return "".join(ResultList)

print(Solution.Replace_The_Number2("a1b2c3"))
