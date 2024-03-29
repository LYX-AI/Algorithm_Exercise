'''
topic：
    Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

example:
    Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:

Input: s = "abcd", k = 2
Output: "bacd"

'''
'''
trace of though is same like String Reverse ,the most important is to pay 
attention to how large is the next step
'''
# more pythonic
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        p=0
        while p<len(s):
            p2=p+k
            s=s[:p]+s[p:p2][::-1]+s[p2:]
            p=p+2*k
        return s

# Using the reverse function
    def reverseString(self, s: list[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        i=0 
        j=len(s)-1
        while i < len(s)/2:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return s

    def reverseStr(self, s: str, k: int) -> str:
        res=list(s)
        for cur in range(0,len(s),2*k):
            res[cur:cur+k]=self.reverseString(res[cur:cur+k])
        return ''.join(res)
