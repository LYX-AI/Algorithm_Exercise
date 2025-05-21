class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result_set = set()
        result = 0
        left = 0
        for right in range(len(s)):
            while s[right] in result_set:
                result_set.remove(s[left])
                left += 1
            result_set.add(s[right])
            result = max(result,right-left+1)
        return result

