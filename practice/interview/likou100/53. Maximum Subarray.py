class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        #两个变量很重要
        current_sum = nums[0]#到当前元素为止子列表中和最大的值(不包括当前元素)
        max_result = nums[0]#到目前位置之前所有的值的和最大结果
        for num in nums[1:]:
            current_sum = max(current_sum+num,num)
            max_result = max(current_sum,max_result)
        return max_result
if __name__ == "__main__":
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums))