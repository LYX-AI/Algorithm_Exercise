from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # left, right = 0, len(nums) - 1
        # result = []
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         start,end = mid,mid
        #         while nums[start] == target:
        #             start -= 1
        #         while nums[end] == target:
        #             end += 1
        #         result.append(start+1)
        #         result.append(end-1)
        #         return result
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     elif nums[mid] > target:
        #         right = mid - 1
        # return [-1, -1]
        def find_left():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return left
        def find_right(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    left = mid+1
            return right
        First=find_left(nums, target)
        Last=find_right(nums, target)
        if First <= Last and 0<=First<len(nums) and nums[First] == target:
            return [First, Last]
        return [-1, -1]

if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8))
