class Solution:
    # def longestConsecutive(self, nums: list[int]) -> int:
    #     nums.sort()
    #     result=set()
    #     for i in range(len(nums)-1) :
    #         if nums[i+1]-nums[i] == 1:
    #             result.add(nums[i])
    #             result.add(nums[i+1])
    #         else:
    #             result.add(nums[i])
    #             break
    #     return len(list(result))
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set=set(nums)
        result=0
        for num in nums_set:
            if num-1 not in nums_set:
                current=num
                count=1
                while current+1 in nums_set:
                    current+=1
                    count+=1
                result=max(result,count)
        return result


if __name__ == "__main__":
    nums1 = [0,3,7,2,5,8,4,6,0,1]
    nums2 = [1,0,1,2]
    nums3 = [100,4,200,1,3,2]
    solution=Solution()
    # print(solution.longestConsecutive(nums1))
    # print(solution.longestConsecutive(nums2))
    print(solution.longestConsecutive(nums3))

