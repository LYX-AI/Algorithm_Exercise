'''
The example of the issue:
     

示例 1：

输入: password = "s3cur1tyC0d3", target = 4
输出: "r1tyC0d3s3cu"

示例 2：

输入: password = "lrloseumgh", target = 6
输出: "umghlrlose"

'''
class Solution:
    def dynamicPassword(self, password: str, target: int):
        return password[target:]+password[:target]
        
    def reversed(l:list[str]):
        for i in len(l)/2:
            l[i],l[len(l)-i-1]=l[len(l)-i-1],l[i]
        return l
    def dynamicPassword2(self, password: str, target: int):
        s=list(password)
        s[:target]=self.reversed(s[:target])
        s[target:]=self.reversed(s[target:])
        return ''.join(reversed(s))