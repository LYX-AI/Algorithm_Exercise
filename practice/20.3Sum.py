'''
topic:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

for example:
    Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
'''
'''
Train of though of 2 sum:

   The first step:
        when to us the hash table:
            1. Whether one element has apperred
            2. Whether the target element in the set
    
    This topic we need to have a set to store the elements,then traversal  the array at the same time to find whetner the elements we 
    have traversal now is in the set, so based on this we know that the we need to us the hash

    we need to store the value of the elements and the subscript of the elements so have two things we need to store :chose the map(dictionary in the python)

    then we need to make clear two things:
    1: what is the map using for
    2: what is the map's key and value

    1:the map is used to store the elements we have already traversal
    2:this topic we need to based on the value to find the subsctript: the key to store the vlaue of the elements and the value to store the subsript of the elements

then let us to see the 3sum：
This topic we are easy to think using the hash ,but the topic request us "Notice that the solution set must not contain duplicate triplets." the three elements should be different
So it's a little difficult to remove duplicates
so this question we chose to use the Two-Pointer 

Step1:
we should sort the array 

Step2:
Defined the three pointers:
i point to the subscript 0 of the array;
left is point to the subscript i+1
right is point to the end of the array(point to the tail of the array) 

Step3:
We should find the nums[i]+nums[left]+nums[right]
    if  nums[i]+nums[left]+nums[right]>0, so we need to move the right to left to make the sum smaller
        nums[i]+nums[left]+nums[right]<0, so we need to move the let to right to make sum bigger
    until the left meet the right

Step4:
The most important we need to consider to Remove Duplicates
  in this topic there are three elements a=nums[i] b=nums[left] c=nums[right] should be different
  Firstly , we should make sure that the number a:
    there are tow select here for the a: 1. judge the nums[i] with nums[i+1]
                                         2. judge the nums[i] with nums[i-1]
    we chose the   2. judge the nums[i] with nums[i-1]
        the reaseon: What we need to do is to have non-repeating triplets, but the elements within each triplet can be repeated!
        for example:{-1,-1,2} when we trversal the first elements then the next elements before this one is still -1, if we us the 
        first judge , the progress will be passed is false
    
    Secondly, we pay attention to the b and c:
      while (left < right && nums[right] == nums[right + 1]) right--
      while (left < right && nums[left] == nums[left - 1]) left++;

We need to Remove the Duplicates, so it's a little difficult to use hash
                
'''
class Solution:
    def threeSum(nums: list[int]):
        result=[]
        nums.sort()

        for i in range(len(nums)):
            if nums[i]>0:
                return result
            # Remove Duplicates a
            if i >0 and nums[i]==nums[i-1]:
                continue
            left=i+1 
            right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum>0:
                    right-=1
                elif sum<0:
                    left+=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
            # Remove Duplicate b , c 
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    right-=1
                    left+=1
        return result
            
print(Solution.threeSum([-1,0,1,2,-1,-4]))  
