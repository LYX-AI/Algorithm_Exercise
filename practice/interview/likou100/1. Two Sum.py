class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        result=[]
        for i in range(n-1):
            for j in range(i+1,n):
                total = nums[i]+nums[j]
                if total == target:
                    result.extend([i,j])
                else:
                    continue
        return result

    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i , num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],i]
            seen[num] = i

if __name__=="__main__":
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums,target))