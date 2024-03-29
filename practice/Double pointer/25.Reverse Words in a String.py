'''
tpoic:
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

'''
'''
example:
    Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

'''

'''
dismantling approach:

1.delete the empty space
2.reverse the whole string
3. reverse the every words to make sure the the order of every words is normal

'''
'''
'''
# dismantling approach2:
# 1.dismantle the string to every single word
# 2.there are two pointers, the first one is point to the head of the stting 
# another is point to the end fo the string
# 3,change the based please of every word 
# '''
class Solution:
    def reverseWords(self, s: str):
        s=s.strip()
        s=s[::-1]
        s=' '.join(word[::-1] for word in s.split())
        return s

    def reverseWords2(self, s: str):
        s=s.split()
        left,right=0,len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        ' '.join(s)


