'''
这道题一开始我想的思路是用递归的方法来解但是思路错了
主要抓住一个公式
前缀和就是数组中从第一个元素开始，累加到当前位置的和。

比如有数组：

python
Copy
Edit
nums = [3, 4, 7, 2, -3, 1, 4, 2]
它的前缀和（pre_sum）是：

css
Copy
Edit
[3, 3+4, 3+4+7, 3+4+7+2, ...]
⟹ [3, 7, 14, 16, 13, 14, 18, 20]
我们用一个数组 pre_sum[i] 表示从 下标 0 到下标 i 的所有元素的和。

🌟 二、为什么要用前缀和？
我们可以用两个前缀和相减的方式，快速得到某一段子数组的和。

举个例子：
你想要快速求出 nums[2] 到 nums[4] 的和？

Copy
Edit
nums[2] + nums[3] + nums[4] = pre_sum[4] - pre_sum[1]
你会发现：

Copy
Edit
前缀和的差 = 某段子数组的和
所以我们不需要每次都去一个个加数字，只需要查一下前缀和的差值就行！


'''
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        #这道题我想到了用递归的方法来写,递归函数就是一个数字里找到所有能组成目标树
        profix_count = defaultdict(int)
        profix_count[0] = 1
        profix_sum = 0
        reslt = 0
        for num in nums:
            profix_sum += num
            reslt += profix_count[profix_sum-k]
            profix_count[profix_sum] += 1
        return reslt
