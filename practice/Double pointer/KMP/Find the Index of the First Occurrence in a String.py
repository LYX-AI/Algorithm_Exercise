'''
topic:
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
'''
example:
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''
class Solution:
    def getNext(self,s):
# initialize
        next=[0]
        j=0
        for i in range(1,len(s)):
            while s[i]!=s[j] and j>0:
                    j=next[j-1]
            if s[j]==s[i]:
                j+=1
            next.append(j)
        return next
    
    def strStr(self, haystack: str, needle: str): 
        if len(needle)==0:
            return 0 
        j=0
        next=self.getNext(needle)
        for i in range(len(haystack)):
            while j>0 and needle[j]!=haystack[i]:
                 j=next[j-1]
            if needle[j]==haystack[i]:
                j+=1
            if j==len(needle):
                return i-len(needle)+1
        return -1


a=Solution()
print(a.strStr(haystack = "sadbutsad", needle = "sad"))