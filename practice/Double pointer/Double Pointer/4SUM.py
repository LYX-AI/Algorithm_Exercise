'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
'''
'''
example:
Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n=len(nums)
        result=[]
        for i in range(n):
            #pruning
            if nums[i]>0 and target>0 and nums[i]>target:
                break
            #Remove the duplicates
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                #pruning
                if nums[i]+nums[j]>0 and target>0 and nums[i]+nums[j]>target:
                    break
                # Remove the duplicates
                if j>1 and nums[j]==nums[j-1]:
                    continue


             