class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p = list(p)
        p.sort()
        len_P = len(p)
        s=list(s)
        result = []
        for i in range(len(s)-len_P+1):
            temp_list = s[i:i+len_P]
            temp_list.sort()
            if p == temp_list:
                result.append(i)
            else:
                continue
        return result
if __name__ == "__main__":
    s = "abab"
    p = "ab"
    solution = Solution()
    print(solution.findAnagrams(s,p))



