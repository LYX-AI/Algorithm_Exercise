from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #这道题一开始没思路，查了后还是感觉很难要关注
        need = Counter(t) #创建字典存放目标列表中各个元素出现的次数
        left,right = 0,0 #左右指针
        window = {} #用来存放滑动窗口中的元素
        start = 0 #满足最小覆盖的起始位置
        length = float("inf")#记录最小覆盖的长度
        value = 0#满足need中元素的个数

        #扩大滑动窗口
        while right < len(s):
            n = s[right] #记录当前指针指向的位置
            right +=1 #开始移动
            if n in need:
                window[n] = window.get(n,0)+1
                if window[n] == need[n]:
                    value +=1
        #收缩滑动窗口
            while value == len(need):
                if right-left < length:
                    start = left
                    length = right-left
                m = s[left]
                left +=1
                if m in need:
                    if window[m] == need[m]:
                        value-=1
                    window[m]-=1

        return "" if length == float('inf') else s[start:start+length]


    #用暴力的方法来解这道题更好理解一些,但是用暴力会超时

    def minWindow2(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        len_result = float("inf")
        t_count = Counter(t)
        result = ""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                window_str = s[i:j]
                window_str_count = Counter(window_str)
                if all(window_str_count[char] >= count for char , count in t_count.items()):
                    if j-i<len_result:
                        len_result =j-i
                        result = window_str
        return result


