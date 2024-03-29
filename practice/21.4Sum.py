'''
topic:
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
'''
'''
Train of thought:
    it'S seem like the 3Sum, Compare with the  3Sum, we will have two for loop:
we will have A B C D  A+B+C+D=target
the first loop is for A 
the second loop is for B 
the first point is for C
the second point is for D

'''
class Solution:
    def fourSum(self, nums: list[int], target: int):
        nums.sort()
        n=len(nums)
        result=[]
        for i in range(len(nums)):
            # pruning process
            if nums[i]>target and nums[i]>0 and target>0:
                break
            # Remove the Duplicate of the A
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n):
                # pruning process
                if nums[i]+nums[j]>target and target>0:
                    break
                # Remove the Duplicate of the B 
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left,right=j+1,n-1
                while left<right:
                    s=nums[i]+nums[j]+nums[left]+nums[right]
                    if s==target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        # Remove the Duplicate of C & D:
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        left+=1
                        right-=1
                    elif s<target:
                        left+=1
                    else:
                        right-=1
        return result
                
                

