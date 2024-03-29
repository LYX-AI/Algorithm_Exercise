# The core of this issue is double pointer

# nums=[3,2,2,3]
# class Solution:
#     def removeElement(nums:list[int],val:int):
#         faster=0
#         slower=0
#         while faster<len(nums):
#             if(nums[faster]!=val):
#                 nums[slower]=nums[faster]
#                 slower=slower+1
#             faster=faster+1
#         return slower


#Violent solution
class Solution:
    def  removeElement2(nums:list[int],val:int):
        i=0
        l=len(nums)
        while i<l:
            if nums[i]==val:
#when the two parameters in the  “for  in range(x,x)” the “for” loop will be skipped, so when the target vlue is the last one in the array will skip this part
                for j in range(i+1,l):
                    nums[j-1]=nums[j]
                l-=1
                i-=1
            i+=1
        return l
