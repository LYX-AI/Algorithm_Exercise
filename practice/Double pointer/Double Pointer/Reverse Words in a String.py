class Solution:
    def reverseWords(self, s):
        tempList=s.split()
        return " ".join(reversed(tempList))
a=Solution()
print(a.reverseWords(s="the sky is blue"))