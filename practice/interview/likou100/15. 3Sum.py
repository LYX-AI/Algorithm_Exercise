class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = n-1
            while left < right:
                total = nums[i]+nums[right]+nums[left]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    right = right-1
                    left = left+1
                elif  total > 0:
                    right-=1
                else :
                    left+=1
        return result

if __name__ == "__main__":
    solution = Solution()
    nums1 = [-1, 0, 1, 2, -1, -4]
    nums2 = [0, 1, 1]
    nums3 = [0, 0, 0]
    print(solution.threeSum(nums1))
    print(solution.threeSum(nums2))
    print(solution.threeSum(nums3))



