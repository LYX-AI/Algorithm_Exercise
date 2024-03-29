'''
Topic:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item =='{':
                 stack.append('}')
            elif not stack or stack[-1]!=item:
                return False
            else:
                stack.pop()
            
        return True if not stack else False
    def isValid2(self,s: str):
        stack=[]
        mapping={
            '(':')',
            '[':']',
            '{':'}'
        }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1]!=item:
                return False
            else:
                stack.pop()
        return True if not stack else False

sol=Solution()
sol.isValid(s="{[]}")