'''
topic:
    Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

example:
    Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''
'''
Trace of thought:
    double pointer:
        the first pointer point the first of the string , the second pointer point to the end of the String
        the every elements changed one by one  
        
'''
class Solution:
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

# Solution2 Using the list

    def reverseString2(self, s: list[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        stock=[]
        for char in s:
            stock.append(char)
        for i in range(len(s)):
            s[i]=stock.pop()
# Solution3 Using the range
    def reverseString3(self, s: list[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range (len(s)//2):
            s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]
#Solution4 Using the reversed function
    def reverseString3(self, s: list[str]):
        s[:]=reversed(s)
#Solution4 Using the reversed function
    def reverseString3(self, s: list[str]):
        s[:]=reversed(s)
# Solution5 Using the slicing
    def reverseString4(self, s: list[str]):
        s[:]=s[::-1]
# Solution6 Using the slicing
    def reverseString5(self, s: list[str]):
        s[:]=[s[i] for i in range(len(s)-1,-1,-1)]