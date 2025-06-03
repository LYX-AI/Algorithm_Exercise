'''
 解题思路（核心技巧：原地哈希法）
这个问题的关键是——我们不能用额外空间，还要 O(n)，这就启发我们：能不能把元素放到它“该在”的位置上？

核心思想：
对于一个长度为 n 的数组，答案一定在 [1, n+1] 之间。

举个例子：
如果你有 nums = [3, 4, -1, 1]，那么它的长度是 4，最小缺失正数只能在 [1, 5] 之间。

🧠 解法步骤：
1️⃣：原地放置：把 nums[i] 放到索引为 nums[i] - 1 的位置（即 1 放第0位，2放第1位……）
例如：

cpp
Copy
Edit
nums = [3, 4, -1, 1]
步骤一：
nums[0] = 3，应该放在下标 2 => swap(nums[0], nums[2]) => [-1, 4, 3, 1]
nums[0] = -1，不是正数，不管
nums[1] = 4，应该放在下标 3 => swap(nums[1], nums[3]) => [-1, 1, 3, 4]
nums[1] = 1，应该放在下标 0 => swap(nums[1], nums[0]) => [1, -1, 3, 4]

最终结果：nums = [1, -1, 3, 4]
2️⃣：从头开始遍历，找第一个 nums[i] != i + 1 的位置，i + 1 就是答案。
这里结果是：nums[1] != 2，说明 2 缺失，所以返回 2
'''
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[nums[i]-1] != nums[i]:
                index = nums[i]-1
                nums[i],nums[index] = nums[index],nums[i]
        for j in range(n):
            if nums[j] != j+1:
                return j+1
            else:
                continue
        return n+1
if __name__=="__main__":
    solution = Solution()
    nums = [3, 4, -1, 1]
    print(solution.firstMissingPositive(nums))

