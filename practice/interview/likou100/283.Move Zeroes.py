class Solution:
    def moveZeroes(self, nums: list[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
    #这道题我的第一思路是能不能使用冒泡排序的方法来做
        n = len(nums)
        for i in range(n-1):
            sweep = False
            for j in range (n-i-1):
                if nums[j] == 0:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]
                    sweep = True
            if not sweep:
                break
        return nums

if __name__ == '__main__':
    solution = Solution()
    nums1 = [0, 1, 0, 3, 12]
    print(solution.moveZeroes(nums1))