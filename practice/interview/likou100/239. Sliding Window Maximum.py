from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        n = len(nums)
        for i in range(n-k+1):
            result.append(max(nums[i:i+k]))
        return  result
    #用上述的方法出现了超时的情况
    def maxSlidingWindow2(self, nums: list[int], k: int) -> list[int]:
        reslut = []
        n = len(nums)
        q = deque()
        for i , num in enumerate(nums):
            #当前双端队列力的值已经不在滑动窗口范围内了就pop出去
            if q and q[0]<i-k+1:
                q.popleft()
            while q and nums[q[-1]]<=num:
                q.pop()
            q.append(i)

            if i >=k-1:
                reslut.append(nums[q[0]])
        return reslut


if __name__ == "__main__":
    solution = Solution()
    nums = [7,2,4]
    k = 2
    print(solution.maxSlidingWindow2(nums,k))