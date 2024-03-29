'''
topic:
    Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
'''
'''
example:
Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 
'''

class Solution:
    #Function of Violence
    def repeatedSubstringPatternViolence(self, s):
        n=len(s)
        if n<=1:
            return False
        for i in range(1,n//2+1):
            if n%i==0:
                SubString=s[:i]
                if SubString*(n//i)==s:
                    return True
        return False
    # function of using find
    def repeatedSubstringPatternUsingFind(self, s:str):
        n=len(s)
        if n<=1:
            return False
        ss=s[1:]+s[:-1]
        return ss.find(s)!=-1
    
    # function of using KMP:
    def GetNext(self,s):
        next=[0]
        j=0
        for i in range(1,len(s)):
            while j>0 and s[i]!=s[j]:
                 j=next[j-1]
            if s[i]==s[j]:
                 j+=1
            next.append(j)
        return next
    def  repeatedSubstringPatternKMP(self, s):
        n=len(s)
        if n<=0:
            return False
        next=self.GetNext(s)
        if next[-1]!=0 and n%(n-next[-1])==0:
            return True
        return False