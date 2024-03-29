'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
'''
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        i,j=0,len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return s
    def reverseString2(self, s):
        stack=[]
        for i in s:
            stack.append(i)
        for j in range(len(s)):
            s[j]=stack.pop()
        return s